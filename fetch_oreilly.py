import json
import requests

results = []

with open('oreilly-ja-zh.json', 'w') as oreilly:
    url = 'https://learning.oreilly.com/api/v2/search/'

    for i in range(100):
        params = {
            "topics": ["Domain Specific Languages", "Software Architecture", "Design Patterns", "Graphics Programming", "Algorithms", "Math", "Parallel Computing", "Engineering", "Game Development", "Linear Algebra", "Calculus", "Physics", "Programming Languages", "Software Development", "Chips & Processors", "Assembly", "Embedded Systems", "Coding Practices", "GNU Build System", "Shell Scripting", "Vim", "Lisp", "Clojure", "Emacs"],
            "languages": ["en"],
            "fields": ["isbn","title"],
            "limit": 200,
            "page": i
        }

        resp = requests.post(url = url, data = params)

        j = json.loads(resp.text)
        if len(j['results']) == 0:
            break

        results += j["results"]

    json.dump(results, oreilly)
