# OIM3640 Problem Solving & Software Design - Final Project - 2026 Spring

---

## 1. Overview

This is your capstone project and the main deliverable of the course (25% of your grade). Build something meaningful with Python - something you can proudly add to your portfolio.

You've already completed three mini projects. This time, you choose the problem, the approach, and the scope. AI tools are encouraged, but **you** make the decisions.

---

## 2. Timeline

| Milestone | Date | Details |
| --- | --- | --- |
| **Proposal** | 4/17 (Fri) | Submit `proposal.md` to your project repo |
| **Gallery Walk** | 4/28 (Mon) | In-class demo, everyone presents |
| **Peer Review** | 4/30 (Wed) | GitHub issues on 2 classmates' repos |
| **Final Submission** | 5/1 (Thu) | Code, README, AI_USAGE.md all finalized |

---

## 3. Forming a Team

- Work **individually** or in a **team of two**.
- Create a new **public** GitHub repository for this project.
  - If working in a team: one person owns the repo, the other is a contributor.
  - List all team member names at the top of `README.md`.
- **Each team member** must submit the repo URL on Canvas.

### Tips for Teams

- Choose partners based on **shared interests**, not just friendship.
- Make sure you both want to invest a **similar level of effort**.
- Agree on how you'll work together (pair programming, dividing tasks, etc.) before you start.

---

## 4. Proposal

- Due: **4/17**
- Create a file named `proposal.md` in your project repo.

Your proposal should include:

1. **What are you building?** One or two sentences describing your project.
2. **Why?** What motivates you to build this? What problem does it solve?
3. **MVP vs. Stretch Goals**: What is the minimum working version? What would you add if you have time?
4. **What don't you know yet?** Be honest about uncertainties - new libraries, APIs, concepts you need to learn.

Keep it short and focused. You've done this three times already.

---

## 5. Project Requirements

### Your project must include:

- A **functional application** (not just code snippets or notebooks)
- Meaningful functionality that solves a real problem or serves a real purpose
- A clear `README.md` with:
  - What your project does
  - How to install and run it
  - Any required API keys or setup steps
- An `AI_USAGE.md` file (see Section 7)

### Your project should:

- Be written primarily in **Python**
- Demonstrate what you've learned in this course
- Have a clear **minimum viable product (MVP)** with room for extension
- Show consistent progress through **regular commits** (not one big commit at the end)

---

## 6. Project Ideas

The theme of this course is "Problem Solving." Use this project to explore how computation applies to something you care about.

**Directions to consider:**

- **Web app** (Flask) - build on what you learned in MP3
- **Data analysis/visualization** - build on what you learned in MP2
- **Automation** - automate a repetitive workflow using APIs and scripts
- **AI-powered tool** - use AI APIs (OpenAI, Claude, etc.) to build something useful
- **Interdisciplinary** - apply Python to another course or personal interest

**A few guidelines:**

- Avoid pure games (they tend to focus on graphics, not software design)
- A project built **for** someone (a club, a friend, a small business) often turns out better than one built in the abstract
- If your project overlaps with another course, check with both instructors first

**Need inspiration?**

- [Project Based Learning (Python)](https://github.com/practical-tutorials/project-based-learning#python)
- [App Ideas Collection](https://github.com/florinpop17/app-ideas)
- [55 Python Project Ideas for Beginners](https://www.dataquest.io/blog/python-projects-for-beginners/)
- [Programming Projects for Advanced Beginners](https://robertheaton.com/2018/12/08/programming-projects-for-advanced-beginners/)

---

## 7. AI Usage

AI tools (ChatGPT, Claude, Copilot, etc.) are **encouraged**. Use them to brainstorm ideas, debug code, generate boilerplate, or learn new libraries.

**You must document your AI usage** in a file named `AI_USAGE.md` in your project repo. For each significant use of AI, record:

- **What you asked** - the prompt or question
- **What AI generated** - the output you received
- **What you did with it** - how you verified, modified, or integrated the output
- **What you learned** - what you understood better as a result

This is not about catching you - it's about developing the skill of working with AI thoughtfully. The quality of your AI documentation is part of your grade.

---

## 8. Peer Review

- Due: **4/30**
- Worth **10%** of your project grade.

After Gallery Walk, you will be **assigned 2 classmates' projects** to review on GitHub. Assignments will be posted on Canvas after Demo Day.

### How it works:

1. Go to your assigned classmate's GitHub repo.
2. Read their README, look through their code, and try running the app if possible.
3. Open a **GitHub Issue** titled "Peer Review - [Your Name]" with feedback using this checklist:

**Checklist:**

- [ ] Does the README clearly explain what the project does?
- [ ] Can you follow the setup instructions to run the project?
- [ ] Is the code organized and readable?
- [ ] Does the project work as described?
- [ ] Is there an AI_USAGE.md with meaningful entries?
- [ ] One thing that impressed you
- [ ] One suggestion for improvement

### Good vs. bad feedback examples

**"One thing that impressed you":**

- Bad: "Nice project!"
- Good: "The way you used the Mapbox API to show a live map of MBTA stops was really cool. I didn't know you could embed interactive maps that easily."

**"One suggestion for improvement":**

- Bad: "Maybe add more features."
- Good: "When I type an invalid address in the search form, the app crashes with a KeyError. Adding a try/except around the API call in `app.py` would fix this."

The goal is to be **specific** - point to actual code, actual behavior, actual experience.

---

## 9. Gallery Walk (Demo Day)

- Date: **4/28** (Session 26)

On Demo Day, you'll set up your project on your laptop. The class will walk around, try each other's projects, and ask questions.

**Prepare:**

- Have your app running and ready to demo
- Be ready to explain: what it does, how it works, what you learned
- Try at least 5 classmates' projects and ask them questions

This is informal and fun - a celebration of what you've built.

---

## 10. Evaluation Criteria

| Criteria | What we're looking for |
| --- | --- |
| **Functionality** | Does it work? Does it solve the problem it set out to solve? |
| **Documentation** | README, AI_USAGE.md, code comments where needed |
| **Technical Depth** | Complexity appropriate to your skill level, evidence of learning |
| **Code Quality** | Organized, readable, good naming, no hardcoded secrets |
| **Peer Review** | Thoughtful feedback on 2 classmates' projects |

**What matters most:** We're looking for evidence that you **understood** what you built and **grew** as a programmer. A simple project that you deeply understand is worth more than a complex one you can't explain.

---

## 11. Final Submission Checklist

Before 5/1, make sure your repo includes:

- [ ] Working code that runs without errors
- [ ] `README.md` with project description, setup instructions, and usage
- [ ] `proposal.md` (from 4/17)
- [ ] `AI_USAGE.md` documenting your AI tool usage
- [ ] Peer review issues posted on 2 classmates' repos
- [ ] Consistent commit history showing iterative progress
- [ ] No secrets (API keys, passwords) committed to the repo - use `.env` + `.gitignore`

---

*Updated: 2026/04/15*
