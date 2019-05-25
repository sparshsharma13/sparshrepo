#!/usr/bin/env bash
awk -F "\"*,\"*" '{ if ($17 == "SFO" )  print $15}' flightdelays.csv | head -n 3 > first3sfo.csv 
csvlook -H first3sfo.csv 
awk -F "\"*,\"*" '{  print $18 }' flightdelays.csv | sort | uniq -c | sort -nr | head -n 3 | csvlook -H
echo "Sparsh Sharma"
