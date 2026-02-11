# Elective Mini Projects

Choose **1–2** of the following projects in addition to the 3 required projects. Each follows the same milestone structure (Proposal → Prototype → Core → Polish) and grading criteria described in the [README](README.md).

---

## Option A: Simulation & Numbers

**Build a program that uses randomness to explore a question.** Roll dice, flip coins, simulate card games, or model a real-world process. Run it thousands of times and see if the results match the math.

**Example ideas:**
- Monte Carlo estimation of pi
- Monty Hall problem simulator (does switching really help?)
- Dice probability explorer (roll 2d6 ten thousand times, chart the distribution)
- Blackjack strategy tester
- Random walk visualizer
- Financial simulation (stock price random walk, savings projection with variable returns)

**Key skills:** `random` module, loops, functions, data collection, `matplotlib` for visualization

---

## Option B: Data Explorer

**Find a dataset that interests you and tell a story with it.** Use Python to load, clean, analyze, and visualize real data. The goal is to ask interesting questions and answer them with data.

**Example ideas:**
- Spotify listening habits (export your data, analyze patterns)
- College cost comparison (College Scorecard dataset)
- Movie/TV trends (IMDb or TMDb data)
- Boston open data (transit, crime, permits)
- Personal finance dashboard (export bank transactions, categorize spending)
- Weather comparison across cities

**Where to find data:** [Kaggle](https://www.kaggle.com/datasets), [data.gov](https://data.gov), [Google Dataset Search](https://datasetsearch.research.google.com/), [FiveThirtyEight](https://github.com/fivethirtyeight/data), or your own exports (Spotify, fitness apps, bank statements)

**Key skills:** `pandas`, `matplotlib`, file I/O, data cleaning, exploratory analysis

---

## Option C: Web Scraper

**Build a program that extracts useful information from a website** and does something with it - save it, analyze it, or display it. The web is full of data that isn't available as a nice API. Scraping is how you get it.

**Example ideas:**
- Price tracker (monitor a product, save price history to CSV)
- Job listing aggregator (scrape titles, companies, locations)
- News headline collector (track trending stories across sites)
- Restaurant menu scraper (compare prices across restaurants)
- Sports stats collector (scores, standings, player stats)
- Course catalog explorer (scrape your university's catalog)

**Important:** Be ethical - respect `robots.txt`, add delays between requests, don't scrape personal data, check Terms of Service.

**Key skills:** `requests`, `BeautifulSoup`, HTML parsing, file I/O, error handling

---

## Option D: AI-Powered Tool

**Build an application that uses an AI model through its API** to do something useful. You've been using AI tools all semester - now build something on top of one.

**Example ideas:**
- Study buddy (paste notes, get auto-generated quiz questions)
- Email/message drafter (give a scenario, get a professional message)
- Code reviewer (input a Python file, get feedback)
- Recipe generator (input ingredients, get recipes)
- Meeting summarizer (paste transcript, get structured summary)
- Language learning tool (AI conversation partner that corrects grammar)

**Getting started:** Use the OpenAI API (`pip install openai`). Never commit API keys to GitHub - use a `.env` file.

**Key skills:** REST APIs, JSON, prompt engineering, string processing, API key management

---

## Option E: Game

**Build a game you'd actually want to play.** It can be terminal-based or graphical. Focus on clean game logic, state management, and a good player experience.

**Example ideas:**
- Terminal Wordle (with color-coded hints)
- Text adventure / choose-your-own-adventure
- Hangman with word categories
- Typing speed test
- Card game (Blackjack, War, memory matching)
- Snake or Pong (using `pygame`)

**Key skills:** Game loops, state management, user input handling, conditional logic, optionally `pygame` or `curses`

---

## Option F: Custom Project

**Propose your own project.** It can be anything that uses Python to solve a real problem or explore something you're curious about. The only requirements:

- It must involve writing Python code
- It must follow the same milestone structure (Proposal → Prototype → Core → Polish)
- You must be able to explain what you built and why

**To propose:** Write your `PROPOSAL.md` with extra detail on what you plan to build, and discuss it with the instructor before starting.
