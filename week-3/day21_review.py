repos = [
    {"name": "daily-briefing", "stars": 2},
    {"name": "my-ai-tool", "stars": 12},
    {"name": "stage-0-exercises", "stars": 5},
]


def build_summary(items):
    popular_names = []
    for item in items:
        if item["stars"] >= 5:
            popular_names.append(item["name"])
    return {"count": len(items), "popular": popular_names}

result = build_summary(repos)
print(result)