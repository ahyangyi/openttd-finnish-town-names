#!/usr/bin/env python3
import glob
from bs4 import BeautifulSoup

# From there:
# https://github.com/OpenTTD/OpenTTD/blob/master/src/lang/finnish.txt
system_prefixes = [
    "Pohjois-",
    "Etelä-",
    "Itä-",
    "Länsi-",
    "Keski-",
    "Ylä-",
    "Ala-",
]


def main():
    s = set()
    for path in glob.glob("htmls/*.html"):
        with open(path) as f:
            soup = BeautifulSoup(f.read(), "lxml")
            for k in soup.find_all("b", class_="hakunimi"):
                s.add(k.decode_contents())
    with open("names/real.csv", "w") as f:
        for w in sorted(list(s)):
            # filter out compounds such as "Haapajärven sydänmaa"
            if any(word[0].islower() for word in w.split(" ")):
                continue
            if any(w.startswith(prefix) for prefix in system_prefixes):
                continue
            print(w, file=f)


if __name__ == "__main__":
    main()
