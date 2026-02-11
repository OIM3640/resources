# Mini Project 2: Text Analysis

## Direction

Take a body of text and **find something interesting in it**. Count words, discover patterns, compare authors, generate new text, or extract meaning from raw language.

Text is everywhere - books, lyrics, tweets, emails, news articles. Python is excellent at taking messy text and turning it into structured insight. Pick a text source you're genuinely curious about.

**The question matters more than the technique.** "Which artist has the biggest vocabulary?" is more interesting than "I counted words."

## Example Ideas

Pick one of these, or come up with your own:

### Simpler Starting Points

- **Word Frequency Analyzer** - Load a text file (book, speech, article), count word frequencies, find the most/least common words, compute basic stats (average word length, unique word ratio, reading level).
- **Song Lyrics Analyzer** - Pick your favorite artist. Analyze their lyrics across albums: vocabulary size, most-used words, sentiment shifts, recurring themes.
- **Markov Text Generator** - Build a Markov chain from a text source and generate new text in the same style. Feed it Shakespeare, then feed it your own text messages.

### More Ambitious Ideas

- **Book Comparison Tool** - Compare two books or authors: vocabulary richness, sentence complexity, word frequency distributions. Who uses more adjectives? Who writes longer sentences?
- **Personal Writing Analyzer** - Feed in your own essays, emails, or text messages. How does your writing style change across contexts? What are your verbal tics?
- **Fake Review Detector** - Analyze product reviews for patterns that suggest they're fake (repetitive phrases, unusual word choices, suspiciously similar reviews).
- **News Headline Tracker** - Collect headlines over time and analyze trends: what words appear more during certain events? How does framing differ across sources?

## Where to Get Text

- [Project Gutenberg](http://www.gutenberg.org/) - 55,000+ free public domain books in plain text (download directly via URL in Python)
- [Wikipedia](https://www.mediawiki.org/wiki/API:Main_page) - Articles via the MediaWiki API (`pymediawiki` library)
- [Kaggle Datasets](https://www.kaggle.com/datasets) - Movie reviews, tweets, news articles, spam messages
- Song lyrics - via web search or lyrics APIs
- Your own data - text messages, essays, Spotify history, email exports

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

Example: "I'm building a tool to compare Taylor Swift's vocabulary across albums because I want to know if her writing got more complex over time. I don't know yet how to get lyrics data or measure vocabulary richness."

### Milestone 1 - Prototype (Commit by end of Week 1)

Before jumping into code, try sketching your logic in a document or on paper. What steps does your program need to take? What data structures make sense? A few minutes of planning saves hours of debugging.

Get text loaded and produce basic output:
- Load text from a file (`.txt`, `.csv`, or copy-pasted into a string)
- Count word frequencies using a dictionary
- Print the top 10 most common words and basic stats (word count, unique words)

Example: Load a book from Project Gutenberg, print the 20 most frequent words and total word count.

### Milestone 2 - Core Features (Commit by end of Week 1.5)

Go beyond simple counting:
- Clean the text (lowercase, remove punctuation, remove stop words)
- Answer at least 2 interesting questions using your analysis
- Create at least 1 visualization (bar chart, word cloud, etc.)
- Organize your code into well-named functions

Example: Compare vocabulary richness across 3 books. Create a bar chart of top words for each.

### Milestone 3 - Polish (Commit by end of Week 2)

Tell a story with your findings:
- Present results clearly (formatted output, tables, or visualizations)
- Write a README that explains: what text you analyzed, what questions you asked, what you found, and what surprised you
- Clean up the code

Example: A README with embedded charts showing vocabulary trends across albums, with a "Conclusions" section discussing what you found.

## What You'll Practice

- String methods (`split`, `strip`, `lower`, `replace`)
- Dictionaries (word counting, frequency tables)
- File I/O (reading text files, writing results)
- Data cleaning and normalization
- Functions and code organization

## Expanding Your Project

Already finished the basics? Here are ways to push further:

- **Visualize** - Use `matplotlib` to create bar charts, word clouds, or trend lines
- **Add Markov generation** - Build a Markov chain and generate new text in the style of your source
- **Use pandas** - Load results into DataFrames for more sophisticated analysis (groupby, pivot tables)
- **Sentiment analysis** - Use the OpenAI API or a library like `TextBlob` to analyze sentiment across sections
- **Compare multiple sources** - Analyze differences between authors, time periods, or genres
- **Build a web interface** - Wrap your analyzer in a Flask app where users can paste text and see results
