from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from github_api import get_github_profile, get_repositories


app = FastAPI(
    title="GitHub Profile Scraper",
    description="A simple GitHub profile scraper using the GitHub REST API.",
    version="1.0"
)

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/search", response_class=HTMLResponse)
def search_profile(
    request: Request,
    username: str = Form(...)
):
    username = username.strip()

    if not username:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Please enter a GitHub username."
            }
        )

    try:
        profile = get_github_profile(username)
        repositories = get_repositories(username) if profile else []
    except Exception:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Could not connect to GitHub. Please try again."
            }
        )

    if profile is None:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"GitHub user '{username}' was not found."
            }
        )

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "profile": profile,
            "repositories": repositories
        }
    )


@app.get("/github/{username}")
def github_profile_api(username: str):
    try:
        profile = get_github_profile(username)

        if profile is None:
            return {"error": "GitHub user not found"}

        repositories = get_repositories(username)

        return {
            "profile": profile,
            "repositories": repositories
        }

    except Exception:
        return {"error": "Could not connect to GitHub"}


@app.get("/health")
def health():
    return {"status": "ok"}
