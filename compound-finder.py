#!/usr/bin/env python3


def main():
    with open("names/real.csv") as f:
        town_names = list(w.strip() for w in f)
    with open("words/kotus-sanalista_v1.txt") as f:
        word_set = set(w.strip().strip("-").lower() for w in f)

    prefixes = {}
    suffixes = {}

    for t in town_names:
        for i in range(1, len(t)):
            p, s = t[:i], t[i:]
            if p.lower() in word_set and s.lower() in word_set:
                prefixes[p] = prefixes.get(p, 0) + 1
                suffixes[s] = suffixes.get(s, 0) + 1

    prefixes = list(sorted(p for p, c in prefixes.items() if c * (len(p) - 2) >= 10))
    suffixes = list(sorted(s for s, c in suffixes.items() if c * (len(s) - 2) >= 10))

    with open("parts/prefix.csv", "w") as f:
        for p in prefixes:
            print(p, file=f)

    with open("parts/suffix.csv", "w") as f:
        for s in suffixes:
            print(s, file=f)


if __name__ == "__main__":
    main()
