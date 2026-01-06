import requests
from utils.version import VERSION

GITHUB_REPO = "loudshield/Ghoost-Crypter"


def check_for_updates():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return {
                "status": "error",
                "message": "Unable to check updates"
            }

        data = response.json()
        latest_version = data.get("tag_name")
        release_url = data.get("html_url")

        if latest_version and latest_version != VERSION:
            return {
                "status": "update",
                "current": VERSION,
                "latest": latest_version,
                "url": release_url
            }

        return {
            "status": "ok",
            "version": VERSION
        }

    except Exception:
        return {
            "status": "error",
            "message": "Network error"
        }
