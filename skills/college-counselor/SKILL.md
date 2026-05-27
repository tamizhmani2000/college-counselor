---
name: college-counselor
description: >
  Guide students through academic planning, career exploration, financial aid, and college
  admissions. Use this skill whenever a student mentions college planning, college
  applications, career path, scholarships, financial aid, FAFSA, SAT/ACT prep, extracurricular
  activities, college list, common app, or needs help choosing a major. Also triggers on
  "what college should I go to", "best colleges for my major", "how to get into college",
  "college essay help", "how do I apply for financial aid", "what career should I choose",
  "build a strong college application", or "what activities should I do for college".
user_invocable: true
triggers:
  - college planning
  - college admissions
  - college application
  - career exploration
  - financial aid
  - scholarships
  - FAFSA
  - college list
  - major selection
  - extracurricular activities
  - SAT ACT prep
  - common app
  - what college should I attend
  - how to get into college
  - build college profile
  - student academic planning
---

# College Counselor Skill

Guide the student through a comprehensive, personalized academic and college planning process.
Collect student profile information, recommend career paths, build a curated college list,
suggest profile-strengthening activities, and identify financial aid opportunities.
Produce a complete college planning package saved to the project folder.

## Why This Matters

College admissions has become increasingly competitive. Students who start planning early —
understanding career interests, selecting the right courses, building a meaningful extracurricular
profile, and targeting the right colleges — have significantly better outcomes. Financial aid
deadlines and scholarship opportunities are frequently missed simply due to lack of awareness.
A personalized, data-driven plan gives every student a fair shot regardless of access to
expensive private counselors.

## Folder Structure

```
working_dir/
  inputs/
    <StudentName>_profile.md     ← student profile collected in Step 1
  output/
    <StudentName>_plan.md        ← complete college planning document
```

Create `inputs/` and `output/` at the start if they do not exist.

## Dependencies

Install before generating output documents:
```bash
pip install python-docx
```

## Workflow

### Step 1: Collect Student Profile

Introduce yourself warmly and explain that you are going to ask a series of questions to
build a personalized college plan. Collect ALL of the following before proceeding.
Ask questions conversationally — do not dump a form on the student. Group related questions
together naturally.

**Personal Information**
1. **Full Name** — first and last name
2. **Age**
3. **Current Grade** (e.g., 9th, 10th, 11th, 12th, or middle school)
4. **Gender** (optional — used only for scholarship eligibility filtering)
5. **City and State** — where they currently live

**Academic Profile**
6. **Current GPA** — unweighted (on a 4.0 scale) and weighted if they know it
7. **Class Rank** — if their school provides it (e.g., top 10%, top 25%)
8. **Strongest Academic Subjects** — subjects they enjoy and perform best in
9. **Weakest Subjects** — areas where they struggle
10. **AP / IB / Dual Enrollment Courses** — list what they are currently taking or have taken
11. **Standardized Test Scores** — SAT, ACT, PSAT (or "not yet taken")
12. **Type of School** — public, private, charter, homeschool

**Career and Interest Profile**
13. **Interested Career Paths** — list 1-3 career areas that interest them (be specific:
    "I want to be a pediatric surgeon" is better than "I like science")
14. **Hobbies and Passions** — activities outside of school they genuinely enjoy
15. **Work or Volunteer Experience** — any jobs, internships, or community service
16. **Current Extracurricular Activities** — clubs, sports, arts, competitions, leadership roles

**College Preferences**
17. **Preferred College Location** — in-state only, specific region, open to anywhere, urban/rural preference
18. **Preferred College Size** — small (<5,000), medium (5,000-15,000), large (>15,000), no preference
19. **College Type Preference** — public, private, liberal arts, HBCUs, women's colleges, faith-based, no preference
20. **Distance from Home** — willing to be far from home, prefer close, or no preference
21. **Intended Major or Field of Study** — even if undecided, list the broad area

**Financial Profile**
22. **Household Income Range** — rough estimate: under $50K, $50K-$100K, $100K-$150K, over $150K
    (explain this is used solely to identify financial aid eligibility)
23. **Financial Aid Need** — are they expecting to need significant financial aid?
24. **State Residency** — confirm state for in-state tuition and state-specific scholarships
25. **Citizenship Status** — US citizen, permanent resident, DACA, international student
    (affects federal aid eligibility)

**Additional Context**
26. **First-Generation College Student?** — neither parent attended a 4-year college
27. **Any Special Circumstances** — learning differences, physical/medical needs, military family,
    recent hardships (optional — helps identify targeted support programs)
28. **Dream College** — if they have one, even if it seems out of reach
29. **Anything Else** — open field for anything important they want to share

After collecting all responses, save the complete profile to `inputs/<FirstName>_profile.md`
using the template in the **Profile Template** section below.

Confirm with the student: "I have saved your profile. Now let me build your personalized
college plan — this will take a moment."

---

### Step 2: Analyze the Profile and Build the Plan

Use the collected profile to generate a comprehensive, personalized plan. Work through
each section below methodically.

#### 2A. Career Path Recommendations

Based on stated career interests, academic strengths, hobbies, and personality signals:

- Recommend **3 career paths** ranked from best fit to alternative fit
- For each career path provide:
  - Career title and brief description (what does the job actually look like day-to-day)
  - Recommended undergraduate major(s) that lead to this career
  - Typical graduate school requirements (if applicable)
  - Average starting salary and mid-career salary (use current data)
  - Job market outlook (growing, stable, or declining)
  - Why this fits the student's specific profile (reference their stated interests and strengths)

If a student's stated career is highly competitive (medicine, law, top finance), flag this
clearly and explain the realistic pathway including GPA expectations, test score requirements,
and typical timelines.

#### 2B. Academic Roadmap

Based on current grade and GPA:

- **Course Recommendations**: Suggest specific AP/IB/dual enrollment courses to take in
  remaining high school years, aligned to the recommended major
- **GPA Improvement Plan**: If GPA is below target for desired colleges, identify specific
  steps (tutoring, course selection, test retakes)
- **Test Prep Guidance**:
  - Target SAT/ACT score ranges for recommended colleges
  - Recommend when to test (timeline based on current grade)
  - Suggest free resources: Khan Academy SAT prep, ACT Academy
- **Summer Programs and Internships**: Recommend grade-appropriate summer opportunities
  (see full grade-by-grade guidance in Section 2D and the Summer Opportunities Reference).
  Always include a mix of: (1) nationally known programs, (2) local/regional opportunities
  within or near the student's city and state, and (3) self-directed options the student
  can pursue independently if cost or travel is a barrier.

#### 2C. College List

Build a tierated college list of **15-20 colleges** across three tiers:

**Reach Schools (4-6 schools)**: GPA and test scores are below the school's 25th percentile,
or acceptance rate is under 20%. Dream school goes here if applicable.

**Match Schools (6-8 schools)**: GPA and test scores are within the school's middle 50% range.
These are the most likely acceptances.

**Safety Schools (4-6 schools)**: GPA and test scores are above the school's 75th percentile,
and acceptance rate is above 40%. Student should feel confident about admission.

For each college include:
- College name and location (city, state)
- Type (public/private/liberal arts/HBCU/etc.)
- Acceptance rate
- Average GPA of admitted students
- Average SAT/ACT range of admitted students
- Enrollment size
- Relevant programs for the student's intended major (with any notable rankings)
- Approximate annual cost of attendance (COA)
- Average net price for students at the household income level provided
- Notable financial aid policies (e.g., meets 100% of demonstrated need, no-loan policy,
  generous merit scholarships)
- Why this college is a good fit for THIS student specifically

Apply the student's location, size, and type preferences. For students in financial need,
weight toward schools with strong financial aid. For first-generation students, note schools
with strong first-gen support programs.

#### 2D. Extracurricular, Summer Internship, and Profile-Building Recommendations

Based on current grade and existing activities, recommend what the student should do to
strengthen their college application profile. Be specific and realistic — not every student
can become class president.

For every grade level, provide **three tiers of summer opportunities**:
1. **National programs** — competitive, resume-building, well-known to admissions officers
2. **Local / nearby opportunities** — search specifically within or near the student's city
   and state; use the student's location to surface hospitals, universities, nonprofits,
   government offices, museums, labs, or companies within reasonable commuting distance
3. **Self-directed options** — free or low-cost alternatives the student can build
   independently (online courses, personal projects, volunteering, freelance work)

---

**If currently in 8th grade or entering 9th grade (rising 9th):**

*Goal: exploration and early exposure — build curiosity, not a resume.*

Summer Activities:
- Attend a free or low-cost summer enrichment program at a local college or library
- Volunteer at a nonprofit, animal shelter, food bank, or community organization in the
  student's city — any cause they genuinely care about
- Take a free online course on Coursera, edX, or Khan Academy in a subject of interest
- Visit local businesses, hospitals, or labs through job-shadow or career day programs
  (call and ask — many organizations welcome curious middle-schoolers)
- Read 2-3 books in an area of career interest; write short reflections

Nearby Opportunity Search:
- Search "[student's city] summer camp high school [career interest]"
- Search "[student's state] youth volunteer programs"
- Contact local library: many run free STEM, arts, or writing programs for teens
- Check local community college for free dual-enrollment or audit options

---

**If currently in 9th grade (rising 10th):**

*Goal: first meaningful exposure — start connecting interests to real-world experience.*

Summer Activities:
- **Volunteer or intern** at a local organization aligned to career interest:
  - Pre-med → volunteer at a local hospital, clinic, or nursing home (many accept 14+)
  - STEM → volunteer at a science museum or apply to a university lab assistant program
  - Business → shadow a local small business owner or help with social media/marketing
  - Arts → apprentice with a local artist, theatre company, or design studio
  - Law/Policy → volunteer at a local courthouse, legal aid office, or city government office
- Enroll in one **online course** to build a tangible skill: Python (CS50x), biology
  (MIT OpenCourseWare), creative writing, graphic design (Canva Design School), etc.
- Participate in a **local competition**: science fair, debate tournament, robotics
  regional, writing contest, math olympiad
- Begin a **personal project** that can grow over multiple summers: a blog, a YouTube
  channel explaining a topic, a small app, a research paper, an art portfolio

Nearby Opportunity Search:
- Search "[student's city] hospital volunteer teens" or "[student's city] teen volunteer"
- Search "[student's state] governor's school" or "[student's state] summer academy"
- Look up university summer programs within 100 miles — many are free or low-cost for
  local students (e.g., university research exposure programs for underrepresented youth)
- Ask school counselor about local employer partnerships or job-shadow programs

National Programs (selective — good to know early):
- Girls Who Code Summer Immersion (free, tech-focused, for girls)
- NASA Internships (high school track, competitive)
- National Student Leadership Conference (NSLC) — various fields

---

**If currently in 10th grade (rising 11th):**

*Goal: depth and early credibility — first real internship or research experience.*

Summer Activities:
- **Pursue a formal internship or research position**:
  - Cold-email professors at nearby colleges asking to assist in their lab over the summer
    (email 10-15 professors; expect 1-2 responses — this works more often than students think)
  - Apply to local hospitals for clinical volunteering or patient care assistant programs
  - Apply to small local companies in the career field of interest — many hire unpaid interns
    who are self-motivated high schoolers; emphasize eagerness to learn over experience
  - Contact local government offices (city council, parks dept, planning dept) for summer
    intern or aide positions — often unpaid but highly regarded on applications
- **Attend a summer academic program** if budget allows:
  - Look for programs at in-state public universities — significantly cheaper than
    nationally advertised private programs and equally impressive to admissions readers
  - Apply for financial aid at any program before assuming it is unaffordable
- **Build a significant personal project**: by the end of this summer the student should
  have something concrete to show — code on GitHub, published writing, an art portfolio,
  a community initiative with measurable impact, a research abstract, etc.
- Prepare for **PSAT** in October — this is the qualifying test for National Merit

Nearby Opportunity Search:
- Search "[city or state] university summer research high school"
- Search "[career field] internship high school [city]" on LinkedIn, Indeed, Handshake
- Look up [state] Department of Health, [state] Dept of Education, or city government
  websites — many post summer youth employment opportunities in April/May
- Search "[state] Junior Science and Humanities Symposium (JSHS)" — free research
  competition for 10th-12th graders

National Programs (apply in winter for following summer):
- Research Science Institute (RSI) at MIT — extremely competitive, fully funded
- Garcia Research Program (Stony Brook) — materials science
- Simons Summer Research Program — STEM research at Stony Brook
- Bank of America Student Leaders — paid summer internship + leadership summit
- Congressional App Challenge — app development competition

---

**If currently in 11th grade (rising 12th):**

*Goal: peak profile-building summer — this is the most important summer for applications.*

Summer Activities:
- **Secure the strongest possible internship or research role available**:
  - This summer carries the most weight on applications — the activity will appear on the
    Common App and can anchor the personal statement
  - Target paid internships if possible — demonstrates real-world value and work ethic
  - Re-approach professors, companies, or organizations the student contacted last year
  - If a formal internship is unavailable, **create your own**: design an independent
    research project, start a community initiative, launch a small business or service,
    or complete a substantial creative work
- **Nearby opportunities to search aggressively**:
  - Local hospitals and health systems often have summer volunteer or shadow programs —
    apply by February/March as spots fill quickly
  - Local tech companies and startups — LinkedIn search "[city] software intern high school"
  - Local law firms — many accept unpaid high school clerks who file, research, and observe
  - Local newspapers, TV stations, or media companies for journalism/communications interest
  - Local nonprofits — many have youth program coordinator assistant roles
  - University libraries, archives, or special collections — often take summer research
    assistants for cataloguing or digitization projects (good for humanities-oriented students)
- **If cost and travel allow**, apply to a nationally recognized residential summer program
  (see national programs list below) — these are not required but are impressive
- **Begin the Common App essay** — draft 1 should be complete by end of August
- **Finalize the college list** — visit 2-3 campuses in person or take virtual tours
- **Request letters of recommendation** from two teachers before school ends in June
  so teachers have the full summer to write; provide each teacher a brag sheet

Nearby Opportunity Search:
- Search "[city] summer internship high school 2025" on LinkedIn and Indeed
- Search "[state] paid summer internship high school"
- Email the student services or outreach office at the nearest college or university —
  ask if they accept high school research assistants or lab volunteers
- Check local Chamber of Commerce website for member companies that may accept interns
- Search "[city] teen employment program" — many cities run subsidized summer youth jobs

National Programs (apply Nov–Feb for the following summer):
- Google CSSI (Computer Science Summer Institute) — fully funded, for rising college freshmen
  but some tracks accept rising 12th graders
- MIT Beaver Works Summer Institute — STEM, highly selective, free
- Yale Young Global Scholars — various tracks, competitive, residential
- Stanford Pre-Collegiate Summer Institutes — residential, various fields
- Johns Hopkins Center for Talented Youth (CTY) — various fields
- Telluride Association Summer Seminars (TASS) — humanities and social sciences, fully funded
- PRIMES (MIT) / PRIMES-USA — math research, highly competitive
- American Legion Auxiliary Girls State / Boys State — civics and leadership, state-based

---

**If currently in 12th grade:**

*Goal: maintain profile strength, do not start new activities that cannot be completed.*

Summer (after graduation / before college):
- Accept any **orientation or pre-college program** offered by the enrolled college
  (Bridge programs, summer research fellowships for incoming freshmen, etc.)
- If a gap year is being considered, research structured gap year programs
  (AmeriCorps, City Year, Global Citizen Year) rather than unstructured time
- Continue or wrap up any ongoing community service commitments — do not abandon them
- A part-time or full-time summer job is entirely acceptable and relatable; do not
  stress about adding more resume items at this stage
- Revisit financial aid award letters — this is the time to negotiate or appeal

---

For all grade levels, after identifying summer opportunities:

1. **Search for nearby-specific openings** using the student's city and state. Web-search:
   `"[city] [career field] internship high school summer [year]"` and
   `"[state] summer program high school [career interest]"`.
   Surface real named programs, hospitals, universities, companies, or nonprofits that
   are plausibly within commuting or reasonable travel distance from the student.

2. **Flag cost and access barriers** honestly. If a program costs $5,000+, note that
   financial aid is usually available and provide the aid application link. Always list
   at least two free or low-cost alternatives alongside expensive options.

3. **Provide application timelines** for every program recommended — most competitive
   programs open applications in October–February for the following summer.

Provide a specific list of **5-8 recommended activities** (a mix of national and local/nearby)
with explanation of why each is valuable for this student's profile and intended career path.

#### 2E. Financial Aid and Scholarships

Based on household income, state, intended major, grade, and demographics:

**Federal Aid**
- Explain FAFSA (Free Application for Federal Student Aid) — what it is, when to file
  (open October 1 each year for the following academic year), and why filing early matters
- Estimate likely Pell Grant eligibility based on income range
- Explain subsidized vs. unsubsidized loans and work-study

**State Aid**
- Identify state-specific grant programs for the student's home state
  (e.g., Texas: TEXAS Grant, B-On-Time, Texas Public Education Grant;
   California: Cal Grant; New York: TAP; Florida: Bright Futures)
- Note GPA and enrollment requirements for state grants

**Institutional Aid**
- Highlight colleges on the recommended list with the most generous aid for the
  student's income level
- Note any colleges that meet 100% of demonstrated financial need (e.g., MIT, Harvard,
  Amherst, UVA for in-state)
- Identify merit scholarship opportunities at match and safety schools

**External Scholarships (list at least 8-10 scholarships)**
For each scholarship include:
- Scholarship name
- Amount
- Eligibility criteria (GPA, demographics, major, state, etc.)
- Application deadline
- Website or search source (collegeboard.org/scholarship-search, fastweb.com,
  scholarships.com, bold.org)

Prioritize scholarships that match the student's specific profile: state, career interest,
first-gen status, gender, ethnicity, community involvement.

**Financial Aid Timeline**
Provide a semester-by-semester financial aid action checklist from current grade through
first year of college.

#### 2F. Application Timeline and Checklist

Create a month-by-month action plan from now through college enrollment:

**For 9th-10th graders**: Multi-year planning roadmap
**For 11th graders**: 18-month countdown plan
**For 12th graders**: Immediate application season checklist

Include deadlines for:
- PSAT (October of 10th and 11th grade)
- SAT/ACT test dates and registration deadlines
- College visit planning
- Early Decision / Early Action vs. Regular Decision tradeoffs
- Common App opening (August 1) and submission windows
- FAFSA filing (October 1)
- CSS Profile schools (if applicable)
- Scholarship application deadlines (specific to list)
- Financial aid award comparison (February-April)
- Deposit deadline (May 1 national deadline)

---

### Step 3: Generate Output Files

#### `inputs/<StudentName>_profile.md`

Save the complete student profile using this structure:

```markdown
# Student Profile: [Full Name]
**Date Created**: [date]

## Personal Information
- **Name**: 
- **Age**: 
- **Grade**: 
- **Gender**: 
- **Location**: [City, State]

## Academic Profile
- **GPA (Unweighted)**: 
- **GPA (Weighted)**: 
- **Class Rank**: 
- **School Type**: 
- **Strongest Subjects**: 
- **Weakest Subjects**: 
- **AP/IB/Dual Enrollment**: 
- **Standardized Test Scores**: 

## Career and Interests
- **Career Interests**: 
- **Hobbies and Passions**: 
- **Work/Volunteer Experience**: 
- **Current Extracurriculars**: 

## College Preferences
- **Preferred Location**: 
- **Preferred Size**: 
- **College Type Preference**: 
- **Distance from Home**: 
- **Intended Major/Field**: 

## Financial Profile
- **Household Income Range**: 
- **Financial Aid Need**: 
- **State Residency**: 
- **Citizenship Status**: 

## Additional Context
- **First-Generation Student**: 
- **Special Circumstances**: 
- **Dream College**: 
- **Additional Notes**: 
```

#### `output/<StudentName>_plan.docx`

Generate a complete college planning Word document using a Python script with the
`python-docx` library. The document must be professional, well-formatted, and
personalized — every section should reference the student by name and tie back to
their specific profile.

**Document structure:**

```
Cover Page
  College Planning Guide — [Student Name]
  Grade [X] | [City, State] | Prepared [Date]

Section 1: Career Path Recommendations
  1.1  Career Path 1 — Best Fit
  1.2  Career Path 2 — Strong Alternative
  1.3  Career Path 3 — Alternative

Section 2: Academic Roadmap
  2.1  Recommended Courses (remaining high school years)
  2.2  GPA and Test Score Targets
  2.3  Summer Program Recommendations

Section 3: College List
  3.1  Reach Schools
  3.2  Match Schools
  3.3  Safety Schools

Section 4: Profile-Building Activities
  4.1  Recommended Activities and Competitions
  4.2  Leadership Development
  4.3  Community Service

Section 5: Financial Aid and Scholarships
  5.1  Federal Aid Overview
  5.2  State Grant Programs
  5.3  Institutional Aid Highlights
  5.4  External Scholarships

Section 6: Application Timeline and Checklist
  6.1  Month-by-Month Action Plan
  6.2  Key Deadlines
  6.3  Application Strategy Recommendations
```

**Install the dependency, then run the tool:**

```bash
pip install python-docx
python tools/generate_plan.py
```

The document generator lives in **`tools/generate_plan.py`**. Before running it:

1. Open `tools/generate_plan.py` and populate the `generate_plan(...)` call inside
   the `if __name__ == '__main__':` block at the bottom of the file with the student's
   real data from Step 2.
2. Run the script — it creates `output/<StudentName>_plan.docx` automatically.

See `tools/generate_plan.py` for the full data contracts:
- `career_paths` — list of dicts with keys: `title`, `fit_label`, `major`,
  `grad_school`, `salary_start`, `salary_mid`, `outlook`, `why_fit`, `day_in_life`
- `reach/match/safety_colleges` — list of dicts with keys: `name`, `location`,
  `type`, `acceptance_rate`, `avg_gpa`, `sat_act_range`, `enrollment`,
  `program_notes`, `annual_coa`, `net_price`, `aid_notes`, `fit_reason`
- `scholarships` — list of dicts with keys: `name`, `amount`, `eligibility`,
  `deadline`, `website`
- `timeline_rows` — list of `(timeframe_label, action_items_string)` tuples
- All other arguments — `list[str]`

After running the script, confirm the file exists at `output/<StudentName>_plan.docx`
and report its file size to the student.

---

### Step 4: Present the Summary

After generating all files, present a clean summary to the student:

```
COLLEGE PLANNING SUMMARY
=========================
Student:          [Name]
Grade:            [X]
Location:         [City, State]
Intended Major:   [Field]

Career Paths Recommended:
  1. [Career Path 1]
  2. [Career Path 2]
  3. [Career Path 3]

College List: [N] schools
  Reach:   [N] schools
  Match:   [N] schools
  Safety:  [N] schools

Top Financial Aid Opportunities:
  [Scholarship 1] — $[Amount]
  [Scholarship 2] — $[Amount]
  [Scholarship 3] — $[Amount]

Immediate Next Steps:
  1. [Most important action based on current grade]
  2. [Second action]
  3. [Third action]

Files Saved:
  inputs/[Name]_profile.md
  output/[Name]_plan.docx
```

Then walk the student through their single most important next step based on their grade
and timeline urgency.

---

## Profile Template

See the `inputs/<StudentName>_profile.md` format in Step 3 above.

---

## Career Path Quick Reference

Use this as a starting guide. Always customize based on the student's full profile.

### STEM Careers

| Career Interest | Recommended Majors | Target GPA | Grad School? |
|---|---|---|---|
| Medicine / Pre-Med | Biology, Biochemistry, Chemistry | 3.7+ | Yes (MD/DO) |
| Engineering | Mechanical, Electrical, Civil, CS | 3.5+ | Optional |
| Computer Science / Tech | CS, Software Engineering, Data Science | 3.3+ | Optional |
| Data Science / AI | CS, Statistics, Math | 3.5+ | Recommended |
| Environmental Science | Environmental Science, Biology, Chem | 3.3+ | Optional |
| Nursing | Nursing (BSN) | 3.2+ | Optional |
| Pharmacy | Biochemistry, Biology | 3.5+ | Yes (PharmD) |
| Dentistry | Biology, Chemistry | 3.6+ | Yes (DDS) |
| Veterinary Medicine | Animal Science, Biology | 3.5+ | Yes (DVM) |

### Business and Economics Careers

| Career Interest | Recommended Majors | Target GPA | Grad School? |
|---|---|---|---|
| Finance / Investment Banking | Finance, Economics, Math | 3.5+ | Optional (MBA) |
| Accounting / CPA | Accounting, Finance | 3.3+ | No (CPA exam) |
| Marketing | Marketing, Communications, Business | 3.0+ | Optional |
| Entrepreneurship | Business, CS, any major | Varies | Optional (MBA) |
| Management Consulting | Business, Economics, any top major | 3.5+ | Optional (MBA) |
| Real Estate | Finance, Business, Economics | 3.0+ | No |

### Law, Policy, and Social Sciences

| Career Interest | Recommended Majors | Target GPA | Grad School? |
|---|---|---|---|
| Law | Political Science, History, Philosophy, English | 3.7+ | Yes (JD) |
| Social Work | Social Work, Psychology, Sociology | 3.0+ | Optional (MSW) |
| Public Policy | Political Science, Economics, Sociology | 3.3+ | Yes (MPP/MPA) |
| Psychology / Counseling | Psychology | 3.3+ | Yes (MA/PhD) |
| Education / Teaching | Education, subject-area major | 3.0+ | Optional |

### Arts, Media, and Humanities

| Career Interest | Recommended Majors | Target GPA | Grad School? |
|---|---|---|---|
| Journalism / Media | Journalism, Communications, English | 3.0+ | Optional |
| Film / TV | Film Production, Communications | Portfolio | Optional (MFA) |
| Graphic Design / UX | Design, Fine Arts, HCI | Portfolio | Optional |
| Architecture | Architecture (B.Arch) | 3.3+ | Optional (M.Arch) |
| Music / Performing Arts | Music, Theatre, Dance | Audition | Optional (MFA) |
| Writing / Publishing | English, Creative Writing | 3.2+ | Optional (MFA) |

---

## College Fit Criteria

When building the college list, evaluate each school against these factors:

**Academic Fit**
- GPA within 0.3 points of the school's average admitted GPA
- SAT/ACT within the middle 50% range
- Strong program in the intended major (look for rankings, faculty, research)

**Financial Fit**
- Net price (after aid) is manageable for the family
- School meets demonstrated financial need (check Common Data Set)
- Available merit scholarships for the student's profile

**Personal Fit**
- Location and distance match stated preferences
- Campus culture and size match personality
- Available extracurricular opportunities in areas of student interest
- Diversity and inclusion considerations if relevant to student

**For First-Generation Students**
Prioritize schools with:
- Dedicated first-gen orientation and support offices
- High 4-year graduation rates for first-gen students
- Mentorship programs (e.g., QuestBridge partner schools, Posse scholars)
- Strong alumni networks in target career fields

---

## Scholarship Search Strategy

When recommending scholarships, search across these categories:

1. **Need-based**: FAFSA-linked federal and state grants
2. **Merit-based**: Academic achievement, GPA, test scores
3. **Field-specific**: Scholarships for STEM, arts, education, health, etc.
4. **Demographic**: Based on gender, ethnicity, first-gen status, disability status
5. **Geographic**: State, city, or regional scholarships
6. **Community/Religious**: Local foundations, civic organizations, faith communities
7. **Employer-linked**: If a parent works for a large employer, check tuition assistance
8. **Military/Veteran**: If student or parent has military connection (ROTC, VA benefits)

Key scholarship databases to reference:
- College Board Scholarship Search (bigfuture.collegeboard.org)
- Fastweb (fastweb.com)
- Scholarships.com
- Bold.org
- Cappex
- QuestBridge (for high-achieving, low-income students)
- Gates Scholarship (for minority students with high need)
- Coca-Cola Scholars Program
- Jack Kent Cooke Foundation (for high-achieving, lower-income students)
- National Merit Scholarship (triggered by PSAT)

---

## State-by-State Financial Aid Quick Reference

| State | Major Grant Program | Key Requirements |
|---|---|---|
| Texas | TEXAS Grant | Enrolled in TX public college, financial need, high school completion plan |
| Texas | B-On-Time Loan (forgiveness) | TX resident, full-time, TX public college |
| California | Cal Grant A/B | CA resident, GPA 3.0+ (A) or 2.0+ (B), FAFSA by March 2 |
| Florida | Bright Futures | FL resident, GPA 3.5+, 100+ community service hours, SAT 1290+/ACT 29+ |
| New York | TAP (Tuition Assistance Program) | NY resident, family income under $80K, full-time enrollment |
| Georgia | HOPE Scholarship | GA resident, GPA 3.0+, enrolled in GA college |
| Michigan | Michigan Reconnect / Michigan Achievement | Income-based, various programs |
| Illinois | MAP Grant | IL resident, financial need, FAFSA filed |

Always look up the current program requirements as amounts and eligibility change annually.

---

## College Application Strategy Notes

### Early Decision vs. Early Action

- **Early Decision (ED)**: Binding. Apply by November 1 or 15, hear back by December.
  Acceptance rates are often 10-15% higher than Regular Decision. Use only for true
  first-choice school. Not advisable if the student needs to compare financial aid offers.

- **Early Action (EA)**: Non-binding. Apply early, get an early decision, but can still
  wait for other offers. Generally the best strategy for strong students.

- **Regular Decision (RD)**: Deadlines January 1-15. More time to strengthen the application.
  Required for comparing aid offers from multiple schools.

- **Rolling Admissions**: Schools review as applications arrive — apply as early as possible.

### Common App vs. Coalition App

Most students use the **Common App** (commonapp.org). A few schools (e.g., MIT, University
of California) have their own portals. The Common App opens August 1 each year.

### The College Essay

The personal statement (650 words) is one of the most important differentiators for
competitive schools. Coach the student to:
- Write about a specific, concrete experience — not a general topic
- Show growth, self-awareness, or a unique perspective
- Avoid topics that are overused: sports injury comebacks, mission trips, immigration stories
  told without a unique angle
- Write in their own voice — admissions readers can spot over-polished essays
- Start early (summer before 12th grade) and revise multiple times

### Letters of Recommendation

- Request from teachers who know the student well (not just the teachers who gave A's)
- At least one STEM teacher and one humanities teacher is typical
- Provide teachers with a "brag sheet" — a one-page summary of achievements, activities,
  and what the student hopes to convey
- Request by end of 11th grade or very early in 12th grade

---

## Summer Opportunities Reference

Use this section when surfacing summer internship, research, and enrichment recommendations
for the student. Always layer national programs with a local search for the student's city
and state. Never list only national programs — nearby opportunities are often more accessible,
equally impressive, and build genuine community ties.

### How to Find Nearby Opportunities

For every student, actively search for local options using these strategies:

**Universities and Colleges (within 50-100 miles)**
- Search the university's website for "high school summer program", "pre-college", or
  "research experience for high school students"
- Email faculty directly in the relevant department — a short, polite cold email asking
  to volunteer in a lab over the summer has a surprising success rate
- Many public universities run free or subsidized programs for in-state students that are
  far less known than national programs but equally valuable

**Hospitals and Healthcare (for pre-med, nursing, public health)**
- Most major hospital systems have a formal teen volunteer or junior volunteer program
- Children's hospitals frequently run summer shadow programs for high schoolers
- Local clinics, Planned Parenthood, community health centers, and free clinics take
  teen volunteers and rarely advertise widely — call directly
- Search: "[city] hospital volunteer teens" or "[hospital system name] junior volunteer"

**Government and Public Sector**
- City and county government offices (planning, parks, public works, city council aide)
  often have unpaid summer intern positions not widely advertised — email the office directly
- State legislature intern programs (most states offer high school tracks)
- Local courts and legal aid societies for pre-law students
- Public library systems often hire teen assistants or run summer reading program support roles
- Search: "[city] government summer internship high school" or "[state] legislative intern"

**Nonprofits and Community Organizations**
- Local branches of national nonprofits (Red Cross, Habitat for Humanity, YMCA, Boys & Girls
  Club) routinely place teen volunteers and sometimes junior program assistants
- Environmental nonprofits, food banks, animal shelters, literacy programs, and arts
  organizations all welcome motivated high school volunteers
- Local chapters of professional associations (medical society, bar association, engineering
  society) sometimes run youth mentorship or shadow programs
- Search: "[city] nonprofit summer volunteer high school" or "[career field] volunteer [city]"

**Private Companies and Startups**
- Small local businesses and startups are far more likely to take a high school intern
  than large corporations — find them through local Chamber of Commerce member directories
- Tech startup hubs in the student's city often list intern openings on their community
  Slack groups or job boards
- Family-owned businesses in the career area of interest are worth a direct in-person ask
- Search LinkedIn: "intern high school [city]" filtered to posted in the last 30 days

**Museums, Libraries, Zoos, Science Centers**
- Science and natural history museums frequently run high school docent, research, or
  collections volunteer programs
- Zoos and aquariums run junior keeper or education assistant programs (popular — apply early)
- Art museums offer teen curatorial assistant or gallery guide programs
- Public libraries have summer reading program aide and technology helper roles

**Search Templates to Use (populate with student's actual city and state):**
```
"[city] summer internship high school [year]"
"[city] teen volunteer [career field]"
"[state] summer research program high school"
"[city] hospital volunteer teens"
"[state] governor's school [subject]"
"[city] nonprofit internship high school"
"[city] [career field] shadow program"
"[state] youth employment summer"
"[university near city] pre-college summer"
"[state] junior science symposium"
```

---

### National Summer Programs by Career Interest

#### STEM / Computer Science / Engineering
| Program | Focus | Grade | Cost | Deadline |
|---|---|---|---|---|
| MIT Beaver Works Summer Institute | STEM/Engineering | 11th | Free | Feb |
| Research Science Institute (RSI) | STEM Research | 11th | Free | Dec |
| PRIMES / PRIMES-USA (MIT) | Mathematics | 10th–11th | Free | Dec |
| Simons Summer Research Program | STEM Research | 11th | Free | Jan |
| NASA High School Internship | Aerospace/STEM | 9th–12th | Paid | Mar |
| Google CSSI | Computer Science | Rising college fresh. | Free | Feb |
| Girls Who Code Summer Immersion | Computer Science | 10th–11th | Free | Feb |
| iD Tech Camps | Tech/Gaming/AI | 9th–12th | Paid (~$1,000+) | Rolling |
| FIRST Robotics (year-round) | Robotics/Engineering | 9th–12th | Varies | Jan (season) |

#### Medicine / Health / Biomedical
| Program | Focus | Grade | Cost | Deadline |
|---|---|---|---|---|
| NIH Summer Internship Program | Biomedical Research | 11th–12th | Paid | Mar |
| Clinical Research Internship (local hospitals) | Clinical exposure | 10th–12th | Free/volunteer | Mar–Apr |
| Envision Healthcare — NSLC Medicine | Medical exploration | 9th–12th | Paid | Rolling |
| Junior Volunteer Programs (hospital systems) | Patient care | 14+ | Free | Feb–Apr |
| Physician Shadow Programs | Medical | 10th–12th | Free | Year-round |
| Pre-Health Scholars programs (state univ.) | Health sciences | 10th–11th | Varies | Mar |

#### Business / Finance / Entrepreneurship
| Program | Focus | Grade | Cost | Deadline |
|---|---|---|---|---|
| Bank of America Student Leaders | Leadership/Community | 11th–12th | Paid | Feb |
| NFTE (Network for Teaching Entrepreneurship) | Entrepreneurship | 9th–12th | Free | Rolling |
| Wharton Leadership in the Business World | Business | 11th | ~$5,000 (aid avail.) | Feb |
| DECA / FBLA (school year + summer) | Business/Marketing | 9th–12th | Low | Jan |
| Junior Achievement programs | Finance literacy | 9th–12th | Free | Rolling |

#### Law / Policy / Social Sciences
| Program | Focus | Grade | Cost | Deadline |
|---|---|---|---|---|
| Telluride Association Summer Seminars (TASS) | Humanities/Social sci. | 10th–11th | Free | Jan |
| Boys/Girls State | Civics/Government | 11th | Free (nominated) | Mar |
| Close Up Washington DC | Government/Policy | 9th–12th | ~$3,000 (aid avail.) | Rolling |
| Supreme Court/Federal Court public tours | Law | Any | Free | Year-round |
| Local Legal Aid Society volunteer | Law/Justice | 14+ | Free | Year-round |

#### Arts / Media / Writing / Film
| Program | Focus | Grade | Cost | Deadline |
|---|---|---|---|---|
| Interlochen Arts Camp | Music/Theatre/Visual Art | 9th–12th | Paid (aid avail.) | Mar |
| Oxbow School (semester) | Visual Arts | 11th | Paid (aid avail.) | Jan |
| Kenyon Review Young Writers | Creative Writing | 10th–12th | ~$2,500 (aid avail.) | Mar |
| NYT Student Journalism Institute | Journalism | 11th–12th | Free (competitive) | Feb |
| School of the New York Times | Various | 9th–12th | Paid | Rolling |
| Local community theatre internships | Theatre/Production | 9th–12th | Free | Year-round |

#### General / Leadership / Community Impact
| Program | Focus | Grade | Cost | Deadline |
|---|---|---|---|---|
| QuestBridge College Prep Scholars | Academic/College prep | 11th | Free | Mar |
| Jack Kent Cooke Young Scholars | Academic | 7th–8th (entry) | Free | Feb |
| Rotary Youth Leadership Awards (RYLA) | Leadership | 10th–12th | Low/Free | Mar |
| AmeriCorps VISTA Summer (18+) | Community service | Post-grad | Stipend | Rolling |
| Congressional Award (year-round) | Public service/fitness | 13–23 | Free | Rolling |

---

### Grade-Level Summer Opportunity Priority Matrix

| Grade | Top Summer Priority | Best Local Opportunity Type | Best National Program Type |
|---|---|---|---|
| 8th / Rising 9th | Exploration — find a passion | Library program, community volunteer | Enrichment day camp in career area |
| Rising 10th | First real-world exposure | Hospital volunteer, lab visit, nonprofit | STEM camp, arts program, NSLC |
| Rising 11th | Research or formal internship | University lab, government office, startup | RSI, TASS, Simons, Boys/Girls State |
| Rising 12th | Strongest possible credential | Hospital, paid job, university research | MIT BWSI, Yale YYGS, Telluride |
| 12th (post-graduation) | College-specific bridge program | Local job or AmeriCorps | College's own pre-freshman program |

---

## Grade-Level Priorities Quick Reference

| Grade | Top Priority | Secondary | Avoid |
|---|---|---|---|
| 9th | Explore widely, strong GPA foundation | Try new activities | Over-specializing too early |
| 10th | Identify 2-3 deep interests, take PSAT | Research summer programs | Burnout |
| 11th | SAT/ACT prep, college research, deepen leadership | Visit campuses | Waiting until 12th |
| 12th | Execute applications, FAFSA, scholarship apps | Maintain GPA (senioritis kills acceptances) | Procrastination |
