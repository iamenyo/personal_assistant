import webbrowser

WEBSITES = [
    {
        "name": "youtube",
        "url": "https://www.youtube.com"
    },

    {
        "name": "google",
        "url": "https://www.google.com"
    },

    {

        "name": "github",
        "url": "https://www.github.com"
    },
]


def open_website(site_name):
    site_name = site_name.lower()
    for site in WEBSITES:
        if site_name in site["name"]:
            webbrowser.open(site["url"])
            return True
    return False
