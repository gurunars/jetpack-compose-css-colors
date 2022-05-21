import requests
from bs4 import BeautifulSoup


EXISTING_COLORS = { 
    "White",
    "Yellow", 
    "Red",
    "Magenta",
    "LightGray",
    "Green",
    "Gray",
    "DarkGray",
    "Cyan",
    "Blue",
    "Black"
}


SUFFIXES_TO_SKIP = {
    "Grey"
}


def to_rgb(hex):
    return [int(it, 16) for it in [hex[1:3], hex[3:5], hex[5:7]]]


def should_be_skipped(name: str) -> bool:
    if name in EXISTING_COLORS:
        return True
    for suffix in SUFFIXES_TO_SKIP:
        if name.endswith(suffix):
            return True
    return False


def get_colors():
    resp = requests.get("https://www.w3schools.com/cssref/css_colors.asp")

    soup = BeautifulSoup(resp.text, 'html.parser')

    boxes = soup.findAll("div", {"class": "colorbox"})

    # val Color.AliceBlue get() = Color(240, 248, 255)
    print("import androidx.compose.ui.graphics.Color")
    print("")
    for box in boxes:
        name = box.find("span", {"class": "colornamespan"}).find("a").getText()
        if should_be_skipped(name):
            continue
        color_hex = box.find("span", {"class": "colorhexspan"}).find("a").getText()
        r, g, b = to_rgb(color_hex)
        print("val Color.Companion.{} get() = Color({}, {}, {})".format(name, r, g, b))


if __name__ == "__main__":
    get_colors()
