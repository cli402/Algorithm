#!/bin/bash
tr ',' '\n' < restaurants.txt | cut -d";" -f1 |sort |uniq -c |sort -r |head -10
cat restaurants.txt | cut -d";" -f2|sort|uniq -c |sort -nr|head -10
cat restaurants.txt |cut -d";" -f 1|tr ',' ' '|sort|uniq|head -10|split -l 1
cat restaurants.txt |cut -d";" -f 1|tr ',' ' '|sort|uniq|head -10|split -l 1|wc -w ???|tr -d 'a-z'
tr 'A-Z' 'a-z' < Frankenstein.txt | sed -n '255,298p'|tr ' ' '\n'| tr -cd 'a-z\n'|sort|uniq -c|sort -nr|head -10 

