import markdown


def render_md(data):
    md = markdown.Markdown(extensions=["fenced_code"])
    return md.convert(data)
