import string
import argparse

MAPPING = {
    "Ä…": "ą",
    "Ä‡": "ć",
    "Ä™": "ę",
    "Ăł": "ó",
    "Ĺ‚": "ł",
    "Ĺ„": "ń",
    "Ĺ›": "ś",
    "Ĺź": "ż",
    "Ĺş": "ź",
    "Ĺ": "Ł",
    "Ă“": "Ó",
    "Ăź": "ü",
    "Ă¤": "ä",
    "Ĺ‘": "ö",
    "Ĺ": "Ö",
    "ĹĽ": "ż",
    "Ĺ›": "Ś",
}

ALLOWED_LIST = set(
    string.ascii_lowercase + 
    string.ascii_uppercase + 
    "W niżach mógł zjeść truflę koń bądź psy" + 
    "W niżach mógł zjeść truflę koń bądź psy".upper() + 
    "{y:i}" + 
    "ď»ż"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    with open(args.path, "r") as f:
        for line in f:
            for actual, expected in MAPPING.items():
                if actual in line:
                    line = line.replace(actual, expected)

                    for char in line:
                        if char not in ALLOWED_LIST:
                            print(line)

            print(line, end="")

if __name__ == "__main__":
    main()
