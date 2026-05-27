"""
generate_plan.py — College Planning Document Generator

Produces a formatted Word document (.docx) for a student's college plan.

Usage
-----
Populate the `generate_plan()` call at the bottom of this file with the
student's data, then run:

    pip install python-docx
    python tools/generate_plan.py

Output is written to:  output/<StudentName>_plan.docx

Data contracts
--------------
career_paths    : list[dict]  — keys: title, fit_label, major, grad_school,
                                      salary_start, salary_mid, outlook,
                                      why_fit, day_in_life
reach/match/safety_colleges : list[dict]  — keys: name, location, type,
                                      acceptance_rate, avg_gpa, sat_act_range,
                                      enrollment, program_notes, annual_coa,
                                      net_price, aid_notes, fit_reason
scholarships    : list[dict]  — keys: name, amount, eligibility, deadline, website
timeline_rows   : list[tuple] — (timeframe_label, action_items_string)
all other lists : list[str]
"""

import datetime
import os

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


# ---------------------------------------------------------------------------
# Low-level helpers
# ---------------------------------------------------------------------------

def _set_cell_bg(cell, hex_color: str):
    """Fill a table cell with a solid background colour (e.g. '1F3864')."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def _set_col_width(table, col_index: int, width_cm: float):
    for row in table.rows:
        row.cells[col_index].width = Cm(width_cm)


def _add_horizontal_rule(doc):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pb = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '1F3864')
    pb.append(bottom)
    pPr.append(pb)


# ---------------------------------------------------------------------------
# Document building blocks
# ---------------------------------------------------------------------------

def _add_cover_page(doc, student_name: str, grade: str,
                    city: str, state: str, intended_major: str):
    for _ in range(3):
        doc.add_paragraph()

    title = doc.add_paragraph('COLLEGE PLANNING GUIDE')
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.runs[0]
    run.bold = True
    run.font.size = Pt(28)
    run.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

    doc.add_paragraph()

    name_p = doc.add_paragraph(student_name)
    name_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = name_p.runs[0]
    r.bold = True
    r.font.size = Pt(20)
    r.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

    meta = doc.add_paragraph(
        f'Grade {grade}  |  {city}, {state}  |  Intended Major: {intended_major}'
    )
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    meta.runs[0].font.size = Pt(12)

    date_p = doc.add_paragraph(
        f'Prepared: {datetime.date.today().strftime("%B %d, %Y")}'
    )
    date_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_p.runs[0].font.size = Pt(11)
    date_p.runs[0].font.color.rgb = RGBColor(0x70, 0x70, 0x70)

    doc.add_page_break()


def _add_section_heading(doc, number: int | str, title: str):
    """Level-1 heading with section number in navy."""
    p = doc.add_heading(f'Section {number}: {title}', level=1)
    for run in p.runs:
        run.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)
    _add_horizontal_rule(doc)
    doc.add_paragraph()


def _add_sub_heading(doc, title: str):
    """Level-2 heading in blue."""
    p = doc.add_heading(title, level=2)
    for run in p.runs:
        run.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)


def _add_bullet(doc, text: str, level: int = 0):
    style = 'List Bullet' if level == 0 else 'List Bullet 2'
    doc.add_paragraph(text, style=style)


def _add_bold_label(doc, label: str, value: str):
    """One paragraph: bold label + normal value text."""
    p = doc.add_paragraph()
    r1 = p.add_run(f'{label}: ')
    r1.bold = True
    p.add_run(value)


def _add_career_path(doc, number: int, title: str, fit_label: str,
                     major: str, grad_school: str, salary_start: str,
                     salary_mid: str, outlook: str, why_fit: str,
                     day_in_life: str):
    _add_sub_heading(doc, f'{number}.  {title}  —  {fit_label}')
    _add_bold_label(doc, 'Recommended Major(s)', major)
    _add_bold_label(doc, 'Graduate School', grad_school)
    _add_bold_label(doc, 'Starting Salary', salary_start)
    _add_bold_label(doc, 'Mid-Career Salary', salary_mid)
    _add_bold_label(doc, 'Job Market Outlook', outlook)
    _add_bold_label(doc, 'Why This Fits You', why_fit)
    _add_bold_label(doc, 'Day in the Life', day_in_life)
    doc.add_paragraph()


def _add_college_table(doc, tier_label: str, tier_color_hex: str,
                       colleges: list[dict]):
    """
    Renders a colour-coded college table for one tier (Reach / Match / Safety).

    colleges keys: name, location, type, acceptance_rate, avg_gpa,
                   sat_act_range, enrollment, program_notes,
                   annual_coa, net_price, aid_notes, fit_reason
    """
    _add_sub_heading(doc, tier_label)

    if not colleges:
        doc.add_paragraph('No colleges in this tier.')
        return

    headers = [
        'College', 'Location', 'Accept %', 'Avg GPA',
        'SAT/ACT', 'Annual COA', 'Net Price', 'Why a Good Fit',
    ]
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        _set_cell_bg(cell, tier_color_hex)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run.font.size = Pt(9)

    col_keys = [
        'name', 'location', 'acceptance_rate', 'avg_gpa',
        'sat_act_range', 'annual_coa', 'net_price', 'fit_reason',
    ]
    for college in colleges:
        row = table.add_row()
        for i, key in enumerate(col_keys):
            cell = row.cells[i]
            cell.text = college.get(key, '')
            cell.paragraphs[0].runs[0].font.size = Pt(9)

    doc.add_paragraph()
    doc.add_paragraph(
        '* Net price shown is estimated for the household income range provided.'
    )
    doc.add_paragraph()


def _add_scholarship_table(doc, scholarships: list[dict]):
    """
    scholarships keys: name, amount, eligibility, deadline, website
    """
    headers = ['Scholarship', 'Amount', 'Eligibility', 'Deadline', 'Where to Apply']
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        _set_cell_bg(cell, '2E75B6')
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run.font.size = Pt(9)

    col_keys = ['name', 'amount', 'eligibility', 'deadline', 'website']
    for s in scholarships:
        row = table.add_row()
        for i, key in enumerate(col_keys):
            cell = row.cells[i]
            cell.text = s.get(key, '')
            cell.paragraphs[0].runs[0].font.size = Pt(9)

    doc.add_paragraph()


def _add_timeline_table(doc, timeline_rows: list[tuple]):
    """
    timeline_rows: list of (timeframe_label, action_items_string)
    """
    headers = ['Timeframe', 'Action Items']
    table = doc.add_table(rows=1, cols=2)
    table.style = 'Table Grid'

    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        _set_cell_bg(cell, '1F3864')
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run.font.size = Pt(10)

    for timeframe, actions in timeline_rows:
        row = table.add_row()
        row.cells[0].text = timeframe
        row.cells[0].paragraphs[0].runs[0].bold = True
        row.cells[0].paragraphs[0].runs[0].font.size = Pt(9)
        row.cells[1].text = actions
        row.cells[1].paragraphs[0].runs[0].font.size = Pt(9)

    doc.add_paragraph()


# ---------------------------------------------------------------------------
# Main public function
# ---------------------------------------------------------------------------

def generate_plan(
    student_name: str,
    grade: str,
    city: str,
    state: str,
    intended_major: str,
    career_paths: list[dict],
    course_recs: list[str],
    gpa_targets: list[str],
    summer_programs: list[str],
    reach_colleges: list[dict],
    match_colleges: list[dict],
    safety_colleges: list[dict],
    activities: list[str],
    leadership_recs: list[str],
    service_recs: list[str],
    federal_aid_notes: list[str],
    state_aid_notes: list[str],
    institutional_aid: list[str],
    scholarships: list[dict],
    timeline_rows: list[tuple],
    strategy_notes: list[str],
) -> str:
    """
    Build and save the student's college planning Word document.
    Returns the output file path.
    """
    os.makedirs('output', exist_ok=True)
    doc = Document()

    # Page margins
    for sec in doc.sections:
        sec.top_margin    = Inches(1)
        sec.bottom_margin = Inches(1)
        sec.left_margin   = Inches(1.25)
        sec.right_margin  = Inches(1.25)

    # Default body font
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(11)

    # ── Cover page ────────────────────────────────────────────────────────────
    _add_cover_page(doc, student_name, grade, city, state, intended_major)

    # ── Section 1: Career Paths ───────────────────────────────────────────────
    _add_section_heading(doc, 1, 'Career Path Recommendations')
    doc.add_paragraph(
        f'Based on your academic strengths, interests, and goals, here are the three '
        f'career paths that are the best fit for you, {student_name.split()[0]}.'
    )
    doc.add_paragraph()
    for i, cp in enumerate(career_paths, 1):
        _add_career_path(doc, i, **cp)

    # ── Section 2: Academic Roadmap ───────────────────────────────────────────
    _add_section_heading(doc, 2, 'Academic Roadmap')

    _add_sub_heading(doc, '2.1  Recommended Courses')
    for item in course_recs:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '2.2  GPA and Test Score Targets')
    for item in gpa_targets:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '2.3  Summer Program and Internship Recommendations')
    for item in summer_programs:
        _add_bullet(doc, item)
    doc.add_paragraph()

    # ── Section 3: College List ───────────────────────────────────────────────
    total = len(reach_colleges) + len(match_colleges) + len(safety_colleges)
    _add_section_heading(doc, 3, 'College List')
    doc.add_paragraph(
        f'The following {total} colleges have been selected based on your academic '
        f'profile, location preferences, intended major, and financial situation.'
    )
    doc.add_paragraph()
    _add_college_table(doc, '3.1  Reach Schools',  'C00000', reach_colleges)
    _add_college_table(doc, '3.2  Match Schools',  '375623', match_colleges)
    _add_college_table(doc, '3.3  Safety Schools', '1F3864', safety_colleges)

    # ── Section 4: Profile-Building Activities ────────────────────────────────
    _add_section_heading(doc, 4, 'Profile-Building Activities')

    _add_sub_heading(doc, '4.1  Recommended Activities and Competitions')
    for item in activities:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '4.2  Leadership Development')
    for item in leadership_recs:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '4.3  Community Service')
    for item in service_recs:
        _add_bullet(doc, item)
    doc.add_paragraph()

    # ── Section 5: Financial Aid and Scholarships ─────────────────────────────
    _add_section_heading(doc, 5, 'Financial Aid and Scholarships')

    _add_sub_heading(doc, '5.1  Federal Aid Overview')
    for item in federal_aid_notes:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '5.2  State Grant Programs')
    for item in state_aid_notes:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '5.3  Institutional Aid Highlights')
    for item in institutional_aid:
        _add_bullet(doc, item)
    doc.add_paragraph()

    _add_sub_heading(doc, '5.4  External Scholarships')
    _add_scholarship_table(doc, scholarships)

    # ── Section 6: Application Timeline and Checklist ─────────────────────────
    _add_section_heading(doc, 6, 'Application Timeline and Checklist')

    _add_sub_heading(doc, '6.1  Month-by-Month Action Plan')
    _add_timeline_table(doc, timeline_rows)

    _add_sub_heading(doc, '6.2  Application Strategy Recommendations')
    for item in strategy_notes:
        _add_bullet(doc, item)
    doc.add_paragraph()

    # ── Save ──────────────────────────────────────────────────────────────────
    out_path = f'output/{student_name.replace(" ", "_")}_plan.docx'
    doc.save(out_path)
    print(f'Plan saved to {out_path}')
    return out_path


# ---------------------------------------------------------------------------
# Entry point — replace placeholder values with real student data
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    generate_plan(
        student_name   = 'Jane Smith',
        grade          = '11th',
        city           = 'Austin',
        state          = 'TX',
        intended_major = 'Computer Science',

        career_paths = [
            dict(
                title        = 'Software Engineer',
                fit_label    = 'Best Fit',
                major        = 'Computer Science, Software Engineering',
                grad_school  = 'Optional — M.S. can accelerate career',
                salary_start = '$95,000 – $120,000',
                salary_mid   = '$140,000 – $180,000',
                outlook      = 'Growing — 25% over next decade (BLS)',
                why_fit      = 'Strong math scores and passion for coding align perfectly.',
                day_in_life  = 'Design, build, and maintain software systems; collaborate with teams.',
            ),
            # Add career path 2 and 3 here
        ],

        course_recs     = ['AP Computer Science A (11th)', 'AP Calculus BC (12th)'],
        gpa_targets     = ['Target unweighted GPA: 3.7+', 'SAT target: 1350–1450'],
        summer_programs = [
            'MIT PRIMES / PRIMES-USA — math/CS research (apply Dec, free)',
            'Google CSSI — CS immersion for rising college freshmen (apply Feb, free)',
            'Local: UT Austin pre-college summer programs for TX residents',
            'Local: Austin tech startup internship — search LinkedIn "[Austin] software intern high school"',
        ],

        reach_colleges = [
            dict(
                name            = 'Carnegie Mellon University',
                location        = 'Pittsburgh, PA',
                type            = 'Private Research',
                acceptance_rate = '11%',
                avg_gpa         = '3.9',
                sat_act_range   = '1510–1570 / 34–36',
                enrollment      = '14,700',
                program_notes   = '#1 CS program (US News)',
                annual_coa      = '$82,000',
                net_price       = '~$28,000 (est.)',
                aid_notes       = 'Meets 100% demonstrated need',
                fit_reason      = 'Top CS program; strong internship pipeline to Big Tech',
            ),
        ],
        match_colleges  = [],   # populate with same structure
        safety_colleges = [],   # populate with same structure

        activities      = ['Join FIRST Robotics team — builds CS + teamwork profile'],
        leadership_recs = ['Run for VP of Computer Club by 12th grade'],
        service_recs    = ['Teach coding at local library (CoderDojo volunteer)'],

        federal_aid_notes  = ['File FAFSA on October 1 — do not wait'],
        state_aid_notes    = ['Texas TEXAS Grant — up to $5,512/yr for TX public colleges'],
        institutional_aid  = ['UT Austin Longhorn Scholarship — merit-based, $5,000/yr'],

        scholarships = [
            dict(
                name        = 'National Merit Scholarship',
                amount      = 'Up to $2,500',
                eligibility = 'PSAT/NMSQT top scorers; GPA 3.5+',
                deadline    = 'October (PSAT)',
                website     = 'nationalmerit.org',
            ),
        ],

        timeline_rows = [
            ('Jun–Jul 2025', 'SAT prep; finalize college list; start Common App essay draft'),
            ('Aug 2025',     'Common App opens Aug 1 — fill out activities section'),
            ('Sep 2025',     'Request letters of recommendation from two teachers'),
            ('Oct 2025',     'File FAFSA on Oct 1; take SAT if retaking; PSAT on Oct 18'),
            ('Nov 2025',     'Submit Early Action applications by Nov 1/15 deadlines'),
            ('Dec 2025',     'EA decisions arrive; complete remaining RD applications'),
            ('Jan 2026',     'Submit all RD applications (most due Jan 1–15)'),
            ('Feb–Mar 2026', 'Compare financial aid award letters as they arrive'),
            ('Apr 2026',     'Evaluate offers; visit top choices; negotiate aid if needed'),
            ('May 1, 2026',  'National Decision Day — submit enrollment deposit'),
        ],

        strategy_notes = [
            'Apply Early Action (non-binding) to top match and safety schools — '
            'acceptance rates are 10–15% higher than Regular Decision.',
            'Do not apply Early Decision unless financial aid comparison is not a concern.',
            'Personalise each Why Us essay — 150–250 words citing specific programs, '
            'professors, or clubs you have researched.',
        ],
    )
