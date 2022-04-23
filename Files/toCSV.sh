#!/bin/bash

for j in $1
do
cp $j "${j%.txt}.csv"
done
