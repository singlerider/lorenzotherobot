import json

import globals
import requests


def report(args, **kwargs):  # pragma: no cover
    username = globals.GITHUB_AUTH[0]
    bot_repo = globals.GITHUB_AUTH[1]
    github_token = globals.GITHUB_AUTH[2]
    reporter = kwargs.get("username", "testuser")
    channel = kwargs.get("channel", "testchannel")
    description = unicode(args[0])
    with requests.Session() as session:
        session.auth = (username, github_token)
        url = (
            "https://api.github.com/repos/" + username + "/" + bot_repo +
            "/issues")
        headers = {
            "Content-Type": "application/json",
            "Authorization": "token " + github_token,
        }
        params = {
            "title": channel + ": " + reporter,
            "body": reporter + " reports \"" + description + "\" in " + channel
        }
        resp = session.post(url=url, json=params, headers=headers)
        data = json.loads(resp.content)
        if "number" in data:
            issue_number = data["number"]
            issue_url = data["html_url"]
            message = (
                "Issue #" + str(issue_number) + " created and is visible at " +
                issue_url)
            return message
        else:
            return (
                "Well, that didn't work. Contact " + username + " on Twitter")
