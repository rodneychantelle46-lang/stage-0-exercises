import json

person = {
    "name": "Chang Feng",
    "age": 24,
    "skills": ["Python", "Git"]
}

text = json.dumps(person, ensure_ascii=False, indent=2)
print(text)

with open("person2.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)

with open("person2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["city"] = "Shanghai"

with open("person2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("person2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(data["name"])
