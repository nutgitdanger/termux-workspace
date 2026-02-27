from fastapi import FastAPI, BackgroundTasks
import subprocess
import requests

app = FastAPI()

GITHUB_USER = "nutgitdanger"

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

@app.post("/webhook/git/{repo}")
def git_flow(repo: str, data: dict, bg: BackgroundTasks):
    bg.add_task(process_repo, repo, data)
    return {"status": "queued", "repo": repo}

def process_repo(repo, data):
    repo_url = f"https://github.com/{GITHUB_USER}/{repo}.git"

    if subprocess.call(f"[ -d {repo} ]", shell=True) != 0:
        run(f"git clone {repo_url}")

    run(f"cd {repo} && git pull")

    with open(f"{repo}/data.json", "w") as f:
        f.write(str(data))

    run(f"cd {repo} && git add .")
    run(f"cd {repo} && git commit -m 'auto update from webhook'")
    run(f"cd {repo} && git push")

@app.get("/github/profile")
def github_profile():
    return requests.get(
        f"https://api.github.com/users/{GITHUB_USER}"
    ).json()

@app.get("/")
def status():
    return {"ok": True}
