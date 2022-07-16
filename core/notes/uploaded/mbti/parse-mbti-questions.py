import json

questions = json.load(open("./mbti-post-cn.json"))["questions"]

i = 0
for item in questions:
    i += 1
    print(f'{i}. {item["text"]}')