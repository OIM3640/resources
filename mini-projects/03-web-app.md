# Mini Project 3: Web App (MBTA + Mapbox)

## Direction

Build a **web application** using Flask that helps people find the nearest MBTA station. The user enters a place name or address, your app geocodes it using the Mapbox API, finds the closest MBTA stop using the MBTA API, and displays the result - ideally on a map.

This project brings together everything you've learned: functions, APIs, data processing, and web development. You'll go from writing Python scripts to building something people can actually use in a browser.

**tl;dr:** Build a Flask web app that takes a place name and shows the nearest MBTA stop.

## How It Works

Your app connects two APIs:

1. **Mapbox Geocoding API** - Convert a place name (e.g., "Boston Common") into latitude/longitude coordinates
2. **MBTA V3 API** - Find the nearest transit stop to those coordinates

Then Flask serves a web page that ties it all together with a form, results display, and (optionally) a map.

### API Keys You'll Need

- **Mapbox**: Sign up at [mapbox.com](https://account.mapbox.com/auth/signup/) for a free access token
- **MBTA**: Request a free API key at [api-v3.mbta.com](https://api-v3.mbta.com)

**Important**: Never commit API keys to GitHub. Store them in a `.env` file and add `.env` to `.gitignore`.

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

Example: "I'm building a web app to find the nearest T stop from any Boston address. I want to add a map and real-time arrival times. I don't know yet how to display a Mapbox map in HTML or how the MBTA API structures its response."

### Milestone 1 - Prototype (Commit by end of Week 1)

Before jumping into code, try sketching the data flow on paper: place name → Mapbox → lat/lng → MBTA → stop name. Understanding the pipeline first makes the code much easier to write.

Get the API pipeline working (no Flask yet):
- Write a function that takes a place name and returns latitude/longitude using the Mapbox API
- Write a function that takes lat/lng and returns the nearest MBTA stop name and wheelchair accessibility
- Combine them: `find_stop_near("Boston Common")` → `("Park Street", True)`
- Test with `print()` statements in `main()`

Example: A working `mbta_helper.py` that you can run from the terminal.

### Milestone 2 - Core Features (Commit by end of Week 1.5)

Build the Flask web app:
- Create a home page with a form where the user enters a place name
- Handle the form submission (POST request), call your helper functions, display the result
- Show the nearest stop name and wheelchair accessibility on a results page
- Handle errors gracefully (place not found, no nearby stops, API errors)

Example: User types "Fenway Park", clicks Submit, sees "Nearest stop: Kenmore - Wheelchair accessible: Yes".

### Milestone 3 - Polish (Commit by end of Week 2)

Make it feel like a real app:
- Add basic CSS styling (Bootstrap is fine, or write your own)
- Add a Mapbox map showing the location and nearest stop
- Write a complete README with setup instructions and screenshots
- Clean up the code (separate helper module from Flask routes)

Example: A styled page with an interactive map, the stop marked with a pin, and a link back to search again.

## What You'll Practice

- Web APIs (HTTP requests, JSON parsing, API keys)
- Flask (routing, templates, forms, POST requests)
- HTML basics (forms, structure, displaying dynamic data)
- Modular code design (helper module separate from web app)
- Error handling for real-world API calls

## Expanding Your Project

Already finished the basics? Here are ways to push further:

- **Real-time arrivals** - Use the MBTA API to show when the next train/bus is arriving at the nearest stop
- **Filter by transit type** - Let users choose: T only, bus only, commuter rail, etc.
- **Multiple results** - Show the 3 nearest stops instead of just one
- **Weather integration** - Add current weather for the location using OpenWeatherMap API
- **Save favorites** - Let users bookmark stations (using cookies or a SQLite database)
- **Nearby events** - Use the Ticketmaster API to show events near the selected location
- **Deploy it** - Put your app online using PythonAnywhere, Render, or Railway
- **Add more APIs** - Explore [public-apis](https://github.com/public-apis/public-apis) for ideas
