import requests

res = requests.get(
    "https://codewithmosh.com/_next/static/media/bg-grid-lighter.4c1e8196.svg"
)

with open("test.html", "w") as f:

    f.write(res.text)
