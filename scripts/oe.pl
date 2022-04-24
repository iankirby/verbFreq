#!/usr/bin/perl

use warnings;
use strict;
use utf8;



my $name="$ARGV[0]"; my $path="$ARGV[1]"; my $file="$ARGV[2]";

my $filename=$path.$file;

# print($filename);

open(my$fh,'<: encoding(UTF-8)', $filename) or die "can't open $filename $!";

#Read the file in row by row

my $plain="";

while (my $row=<$fh>){ $plain=$plain.$row;}

# print $plain;

$plain=~s/\<[^\n]*\n//;

$plain=~s/\n(?!\n)//g;

my @asArray=split("\n",$plain);

my $i=0;

while ($i<=scalar@asArray){
    my $curr=$asArray[$i];
    # $curr=~m/(\_VB[]||)/g;
}


# print$plain;

# print$plain;
# print$file;
# print$path;