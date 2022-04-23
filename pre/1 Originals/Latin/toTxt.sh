#!/bin/bash

for j in *.xml
do
cp "$j" "${j%.xml}.txt"
done