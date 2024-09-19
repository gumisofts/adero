import requests

res = requests.get("https://codewithmosh.com/courses")

with open("test.html", "w") as f:

    f.write(res.text)
