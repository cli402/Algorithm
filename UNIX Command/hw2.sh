#!/bin/bash

day=`date|cut -d ' ' -f 3 -s`
echo "$day>15"|bc -l|mail -s "Payday yet?" -r dgao33@gatech.edu knight951753@gmail.com
