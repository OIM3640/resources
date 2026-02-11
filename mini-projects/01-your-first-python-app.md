# Mini Project 1: Your First Python App

## Direction

Build a Python program that **does something useful**. It should take user input, process it, and produce meaningful output. That's it.

This is your first project, so keep it simple. The goal is to practice writing functions, handling input, and thinking about how someone interacts with your program. Pick something you'd actually want to use - a tool, a calculator, a game, a simulator.

**Start small. Get it working. Then make it better.**

## Example Ideas

Pick one of these, or come up with your own. These are starting points - you can mix, combine, or go in a completely different direction.

### Simpler Starting Points

- **Unit Converter** - Convert between temperature, distance, weight, or currency. Support multiple conversion types with a menu.
- **Grade Calculator** - Input your grades and weights, compute your average, predict what you need on the final to hit your target GPA.
- **Tip & Bill Splitter** - Calculate tips, split bills unevenly, handle tax, compare tipping percentages.
- **Quiz Game** - A trivia game that asks questions, tracks your score, and gives feedback. Bonus: load questions from a file.

### More Ambitious Ideas

- **Personal Finance Calculator** - Compound interest, loan payments, mortgage comparison, savings goals. A mini financial toolkit.
- **Password Generator & Checker** - Generate passwords with customizable rules. Rate password strength. Check if a password meets requirements.
- **Simulation Lab** - Roll dice thousands of times and visualize the distribution. Simulate coin flips, card draws, or the Monty Hall problem. Does the math match the theory?
- **Number Guessing Game with AI** - The computer guesses *your* number using binary search. Or you guess the computer's number with hints. Track statistics across rounds.

## Milestones

### Milestone 0 - Proposal (Before you write any code)

Define what you're building. Commit a `PROPOSAL.md` file:

```markdown
## My Project Proposal

**What I'm building:** (one sentence)
**Why I chose this:** (personal motivation - what problem does this solve for you?)
**Core features:** (3-5 bullet points of what it will do)
**What I don't know yet:** (honest list of things you'll need to figure out)
```

Example: "I'm building a tip calculator because I always argue with my friends about how to split the bill. I don't know yet how to handle uneven splits or tax."

### Milestone 1 - Prototype (Commit by end of Week 1)

Before jumping into code, try sketching your logic in a document or on paper. Write out the steps your program needs to take, or try writing a few lines of code by hand. This helps you think through the problem before worrying about syntax.

Get the most basic version working:
- The program runs without crashing
- It takes at least one user input
- It produces correct output for the simplest case
- Use at least one function you wrote yourself

Example: A converter that converts Fahrenheit to Celsius. That's it. One direction, one conversion.

### Milestone 2 - Core Features (Commit by end of Week 1.5)

Expand to cover the main functionality:
- Handle multiple operations or options (a menu, multiple conversions, etc.)
- Validate user input (what happens if they type "abc" instead of a number?)
- Organize code into well-named functions
- Add a loop so the user can keep using the program without restarting

Example: A converter that supports temperature, distance, and weight conversions, with a menu and input validation.

### Milestone 3 - Polish (Commit by end of Week 2)

Make it pleasant to use:
- Clear menu or help text
- Graceful exit (a "quit" command or clean Ctrl+C handling)
- Clean, well-organized code
- Complete README explaining what your app does and how to run it

Example: A full financial toolkit with a main menu, help text, calculation history, and formatted output.

## What You'll Practice

- Writing and calling functions
- Control flow (`if`/`elif`/`else`, `while` loops)
- String formatting and user interaction
- Input validation and error handling
- Code organization and readability

## Expanding Your Project

Already finished the basics? Here are ways to push further:

- **Add simulation** - Use `random` to run experiments (dice, cards, Monte Hall) and compare results to theoretical probabilities
- **Load data from a file** - Read questions from a CSV, conversion rates from JSON, or quiz banks from a text file
- **Add calculation depth** - Compound interest with monthly contributions, loan amortization tables, break-even analysis
- **Track history** - Save past calculations or game results to a file so the user can review them later
- **Make it look good** - Use [`rich`](https://rich.readthedocs.io/) to add colors, tables, and progress bars to your terminal output
- **Connect to an API** - Pull live currency exchange rates, stock prices, or weather data instead of using hardcoded values
