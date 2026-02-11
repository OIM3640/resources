# Mini Projects

## Overview

Throughout this semester, you will complete a series of **mini projects** to practice building real things with Python. These are designed around problems you actually care about - tools you want to use, questions you want to answer, things you want to build.

### Structure: 3 Required + 1–2 Elective

You must complete the **3 required projects**. Additionally, choose **1–2 elective projects** to explore areas that interest you.

### Required Projects

| # | Project | Core Skills | Released (tentative) |
|---|---------|-------------|----------|
| 1 | [Your First Python App](01-your-first-python-app.md) | Functions, logic, user interaction | After Session 8 |
| 2 | [Text Analysis](02-text-analysis.md) | Strings, files, dictionaries, text processing | After Session 13 |
| 3 | [Web App (MBTA + Mapbox)](03-web-app.md) | Flask, HTML templates, external APIs | After Session 18 |

### Elective Projects (Choose 1–2)

| Project | Core Skills |
|---------|-------------|
| [Simulation & Numbers](elective-projects.md#option-a-simulation--numbers) | Random, probability, matplotlib |
| [Data Explorer](elective-projects.md#option-b-data-explorer) | pandas, matplotlib, data storytelling |
| [Web Scraper](elective-projects.md#option-c-web-scraper) | requests, BeautifulSoup, data cleaning |
| [AI-Powered Tool](elective-projects.md#option-d-ai-powered-tool) | API calls, prompt engineering |
| [Game](elective-projects.md#option-e-game) | Game logic, state management, user interaction |
| [Custom Project](elective-projects.md#option-f-custom-project) | Propose your own - anything that uses Python to solve a real problem |

Each project gives you a **direction**, not a specific problem to solve. You choose what to build within that direction.

Every project has a **base** (accessible starting point) and **extensions** (room to push further with AI, libraries, and creativity). Start with the base. Build from there.

---

## Guiding Principles

### 1. Build Something You Actually Want to Use

The best projects come from personal motivation. Don't just build what you think the professor wants - build something that solves a problem *you* have, or something you'd actually show to a friend.

### 2. Start with a Proposal

Before writing any code, submit a short **proposal** (Milestone 0). This forces you to think about *what* you're building and *why* before jumping into *how*:

```markdown
## My Project Proposal

**What I'm building:** (one sentence)
**Why I chose this:** (personal motivation - what problem does this solve for you?)
**Core features:** (3-5 bullet points of what it will do)
**What I don't know yet:** (honest list of things you'll need to figure out)
```

Commit this as `PROPOSAL.md` in your project folder before starting Milestone 1.

### 3. Iteration Over Perfection

**No one-shot submissions.** Your project must show a clear evolution through multiple commits:

- **Milestone 0 - Proposal**: Define what you're building and why.
- **Milestone 1 - Prototype**: Get the basic idea working. It can be ugly. It just needs to run.
- **Milestone 2 - Core Features**: Add the main functionality. Handle edge cases. Clean up the code.
- **Milestone 3 - Polish**: Improve the user experience. Write a proper README. Refactor where needed.

Each milestone should have its own commit(s). A project with 1 commit will not receive full credit, regardless of code quality.

### 4. AI is a Tool, Not a Shortcut

You are **encouraged** to use AI (ChatGPT, Claude, Copilot, etc.) throughout your projects. However:

- You must maintain a **Learning Log** (see below)
- You must understand the logic and key parts of all code you submit
- You must be able to answer any questions about your code in person

Using AI to generate code you don't understand is not learning - it's copy-pasting with extra steps.

### 5. Show Your Process

Your GitHub commit history is part of your submission. It should tell the story of how your project evolved. This means:

- **Commit early, commit often** (minimum 5 meaningful commits per project)
- **Write descriptive commit messages** - "Add input validation for calculator" not "update" or "fix stuff"
- **Don't be afraid to commit broken code** - that's what iteration looks like

### 6. Document for Others

Every project must include a `README.md` that answers:

- What does this project do?
- How do I run it?

Write it for a classmate who has never seen your code.

---

## Learning Log

For **every project**, include a file called `LEARNING_LOG.md` in your project repository. After each session where you use AI, add an entry:

```markdown
## Date: YYYY-MM-DD

**What I asked AI to do:**
- e.g., "Generate a function to parse CSV files"

**What I didn't understand in the generated code:**
- e.g., "The `with` statement for file handling was new to me"

**What I learned:**
- e.g., "Context managers automatically close files even if an error occurs"
```

The learning log is **not graded on length** - it's graded on whether it shows genuine engagement with the code AI helped you write.

---

## Grading

Each project is checked for **completeness and process**. The following are checked (many automatically):

| Criteria | What We Check |
|----------|---------------|
| Proposal | `PROPOSAL.md` exists with all 4 sections filled in |
| Commit history | 5+ commits spanning multiple days, showing prototype → core → polish evolution |
| README | `README.md` exists and answers: what it does, how to run it |
| Learning Log | `LEARNING_LOG.md` exists with substantive entries |
| Working code | The project runs and does what the README says it does |
| Link in portfolio | Project is linked from your main `oim3640` repository README |

**Oral interview**: The instructor may ask you to walk through your code and explain your decisions. You should be able to answer any questions about your code.

---

## Submission

For each project:

1. **Where to put your code**: Either in your main repo (`oim3640/projects/mp1-your-app-name/`) or in a separate GitHub repository. Your choice.
2. **Link it from your portfolio**: Add a link to each project in the **Mini Projects** section of your main `oim3640/README.md`. This is how we find and check your work.
3. **Include**: Your code, `PROPOSAL.md`, `README.md`, and `LEARNING_LOG.md`.
4. **Deadline**: **2 weeks** after the project is released (but you can always submit early or keep iterating after).

Example `oim3640/README.md` section:

```markdown
## Mini Projects

- [MP1: Unit Converter](projects/mp1-unit-converter/) - converts between temperature, distance, and weight
- [MP2: Song Lyrics Analyzer](https://github.com/username/mp2-lyrics-analyzer) - analyzes word frequency in song lyrics
```

---

## Getting Started

Pick a project that interests you, read its description, and start with the simplest possible version. Don't plan for 3 days and code for 1 day - code for 10 minutes on day 1 and build from there.

The best way to learn to code is to write code. Let's build things.
