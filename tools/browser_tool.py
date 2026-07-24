import webbrowser
from urllib.parse import quote


def open_google():

    webbrowser.open("https://www.google.com")

    return "Opening Google."


# --------------------------------------------------


def search_google(query):

    url = f"https://www.google.com/search?q={quote(query)}"

    webbrowser.open(url)

    return f"Searching Google for {query}."


# --------------------------------------------------


def open_youtube():

    webbrowser.open("https://youtube.com")

    return "Opening YouTube."


# --------------------------------------------------


def search_youtube(query):

    url = (
        "https://www.youtube.com/results?"
        f"search_query={quote(query)}"
    )

    webbrowser.open(url)

    return f"Searching YouTube for {query}."


# --------------------------------------------------


def open_github():

    webbrowser.open("https://github.com")

    return "Opening GitHub."


# --------------------------------------------------


def search_github(query):

    url = (
        "https://github.com/search?"
        f"q={quote(query)}"
    )

    webbrowser.open(url)

    return f"Searching GitHub for {query}."


# --------------------------------------------------


def open_chatgpt():

    webbrowser.open("https://chat.openai.com")

    return "Opening ChatGPT."


# --------------------------------------------------


def open_gmail():

    webbrowser.open("https://mail.google.com")

    return "Opening Gmail."


# --------------------------------------------------


def open_linkedin():

    webbrowser.open("https://linkedin.com")

    return "Opening LinkedIn."


# --------------------------------------------------


def open_stackoverflow():

    webbrowser.open("https://stackoverflow.com")

    return "Opening Stack Overflow."