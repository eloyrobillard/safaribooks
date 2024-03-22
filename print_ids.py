import json

with open('oreilly-ja-zh.json', 'r') as oreilly:
    content = oreilly.read()
    results = json.loads(content)

    for e in results:
        if e.get('isbn'):
            print(e['isbn'])
