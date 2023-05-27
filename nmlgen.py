#!/usr/bin/env python3
import jinja2
import glob


def main():
    with open("names/real.csv") as f:
        town_names = list(w.strip() for w in f)
    with open("parts/prefix.csv") as f:
        prefixes = list(w.strip() for w in f)
    with open("parts/suffix.csv") as f:
        suffixes = list(w.strip() for w in f)

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    context = {
        "town_names": town_names,
        "prefixes": prefixes,
        "suffixes": suffixes,
    }

    for path in glob.glob("nml-template/**/*"):
        new_path = "nml-project" + path[len("nml-template"):]

        with open(new_path, "w") as f:
            template = environment.get_template(path)
            f.write(template.render(context))


if __name__ == "__main__":
    main()
