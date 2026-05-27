# College Counselor

An AI-powered college counselor built with Claude Code. It guides high school students through personalized academic planning, career exploration, college selection, extracurricular strategy, and financial aid — and generates a complete college planning document (`.docx`) as output.

---

## Requirements

- [Claude Code](https://claude.ai/code) (CLI or desktop app)
- Python 3.8+ (for document generation)
- `python-docx` library

```bash
pip install python-docx
```

---

## Getting Started

1. **Clone the repo and open it in Claude Code:**

   ```bash
   git clone https://github.com/tamizhmani2000/college-counselor.git
   cd college-counselor
   claude .
   ```

2. **Start a counseling session** — either type `/college-counselor` or just describe what you need:

   ```
   /college-counselor
   ```

   You can also trigger the skill naturally by mentioning topics like:
   - "I need help with college planning"
   - "What career should I choose?"
   - "Help me find scholarships"
   - "How do I build a strong college application?"

---

## How It Works

The skill runs a four-step workflow:

### Step 1 — Profile Collection
Claude asks conversational questions to build a complete student profile covering:
- Personal information and location
- Academic record (GPA, AP courses, test scores)
- Career interests and hobbies
- College preferences (size, type, location)
- Financial profile (for aid eligibility)

The profile is saved to `inputs/<StudentName>_profile.md`.

### Step 2 — Plan Generation
Claude analyzes the profile and builds a personalized plan covering:
- **Career paths** — 3 ranked recommendations with day-in-life descriptions, salary data, and major alignment
- **Academic roadmap** — course recommendations, GPA targets, test prep guidance
- **College list** — 15-20 schools across Reach / Match / Safety tiers with acceptance rates, costs, and fit notes
- **Extracurriculars & summer programs** — national and local/nearby opportunities by grade level
- **Financial aid & scholarships** — federal, state, institutional, and external scholarships with deadlines
- **Application timeline** — month-by-month action checklist through enrollment

### Step 3 — Document Export
Claude populates `tools/generate_plan.py` with the student's data and runs it:

```bash
python skills/college-counselor/tools/generate_plan.py
```

This creates a formatted Word document at `output/<StudentName>_plan.docx`.

### Step 4 — Summary
Claude presents a concise planning summary and walks through the student's single most important next step.

---

## Project Structure

```
college-counselor/
├── .claude/
│   └── commands/
│       └── college-counselor.md   ← registers /college-counselor slash command
├── skills/
│   └── college-counselor/
│       ├── SKILL.md               ← full counseling workflow definition
│       └── tools/
│           └── generate_plan.py   ← generates the .docx output file
├── inputs/                        ← student profiles (gitignored)
├── output/                        ← generated plan documents (gitignored)
├── CLAUDE.md                      ← project instructions for Claude Code
└── README.md
```

> `inputs/` and `output/` are gitignored — student data stays local and is never committed.

---

## Slash Command

| Command | What it does |
|---|---|
| `/college-counselor` | Starts the full counseling workflow from Step 1 |

---

## Example Output

After completing the workflow, you will have:

- `inputs/Jane_profile.md` — complete student profile
- `output/Jane_plan.docx` — formatted college planning guide with career paths, college list, scholarships, and timeline

---

## Notes

- All recommendations are personalized — generic advice is explicitly avoided.
- Local and nearby opportunities (hospitals, universities, nonprofits) are surfaced alongside national programs based on the student's city and state.
- Scholarship amounts and college statistics are based on current data; always verify deadlines at the authoritative source before applying.
