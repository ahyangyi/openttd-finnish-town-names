#!/usr/bin/env bash

for ((i=1; i<23042; i+=1000))
do
    wget -O htmls/$i.html "https://kaino.kotus.fi/asutusnimihakemisto/index.php?a=listaus&p=$i&-sort=nimi"
done
