# Ahyangyi's Finnish Town Name List for OpenTTD.
Step-by-step scripts to create a Finnish town name NewGRF for OpenTTD.

## Step 1
Run `./crawler.sh` to fetch the web pages containing location names (not included in this repo).

## Step 2
Run `./analyze.py` to create name list (already included).

## Step 3
Run `./compound-finder.py` to discover common parts of Finnish location names.

## Step 4
Run `./nmlgen.py` to generate the needed NML files.

## Step 5
```
cd nml-project/main
make
```
To generate the `.grf` file. Similar process works for the Chinese transliteration version.

## Caveat
Different Finland places have different official langauges (Finnish, Swedish or different dialects of Sami), but since the compound finder (step 3) uses a frequency-based filter, non-Finnish roots seem to be filtered out, and no attempts have been made to create separate generators for them.

The Chinese Transliteration uses a lookup table, and does not properly work with non-Finnish name.
