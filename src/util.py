import markdown as md


def loadMarkdownAsHTML(filepath): # Loads in md files as HTML to be passed through flask
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    html = md.markdown(content)

    return html