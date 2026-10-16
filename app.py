PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}

todos = [
    {"title": "주간 보고선 초안 작성", "priority": "HIGH", "done": False},
    {"title": "회의 자료 작성", "priority": "MID", "done": False},
    {"title": "책상 정리", "priority": "LOW", "done": False},
    {"title": "이메일 답장", "priority": "HIGH", "done": False},
]

pending = [t for t in todos if not t["done"]]
for t in sorted(pending, key=lambda t: PRIORITY_ORDER[t["priority"]]):
    print(f"{t['title']}({t['priority']})")
