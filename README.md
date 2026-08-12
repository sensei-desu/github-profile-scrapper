# GitHub Profile Scraper

A beginner-friendly college project built with Python, FastAPI, HTML, and CSS.

## Features

- Search a public GitHub username
- Fetch profile information using the GitHub REST API
- Display followers, following, repositories, bio, location, and avatar
- Display six recently updated repositories
- Provide a custom FastAPI JSON endpoint
- Provide automatic FastAPI Swagger documentation
- No JavaScript required

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## API endpoint

```text
GET /github/{username}
```

Example:

```text
/github/torvalds
```

## Render deployment

This repository includes `render.yaml`.

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
uvicorn main:app --host 0.0.0.0 --port $PORT
```
RENDER URL :https://github-profile-scrapper-cmtk.onrender.com
