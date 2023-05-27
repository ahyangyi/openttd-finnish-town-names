#!/usr/bin/env python3
import jinja2
import glob
from chn import transliterate_list


def dedup(town_names, prefixes, suffixes):
    ret = []
    for w in town_names:
        dup = False
        for i in range(1, len(w)):
            if w[:i] in prefixes and w[i:] in suffixes:
                dup = True
        if not dup:
            ret.append(w)
    return ret


def main():
    with open("names/real.csv") as f:
        town_names = list(w.strip() for w in f)
        chn_town_names = transliterate_list(town_names)
    with open("parts/prefix.csv") as f:
        prefixes = list(w.strip() for w in f)
        chn_prefixes = transliterate_list(prefixes)
    with open("parts/suffix.csv") as f:
        suffixes = list(w.strip() for w in f)
        chn_suffixes = transliterate_list(suffixes)
    dedup_town_names = dedup(town_names, prefixes, suffixes)
    dedup_chn_town_names = dedup(chn_town_names, chn_prefixes, chn_suffixes)

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    context = {
        "num_town_names": len(town_names),
        "town_names": dedup_town_names,
        "prefixes": prefixes,
        "suffixes": suffixes,
        "num_chn_town_names": len(chn_town_names),
        "chn_town_names": dedup_chn_town_names,
        "chn_prefixes": chn_prefixes,
        "chn_suffixes": chn_suffixes,
        "version": 1,
    }

    for path in glob.glob("nml-template/**/*.*", recursive=True):
        new_path = "nml-project" + path[len("nml-template") :]
        print(path, new_path)

        with open(new_path, "w") as f:
            template = environment.get_template(path)
            f.write(template.render(context))


if __name__ == "__main__":
    main()
