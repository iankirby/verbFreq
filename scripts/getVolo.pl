#!/usr/bin/perl

use strict; use warnings; use utf8;

my $path="$ARGV[0]"; my $file="$ARGV[1]"; 

my $filename=$path.$file;

open(my $fh, '<: encoding(UTF-8)',$filename) or die "Cannot open $filename $1";

my $plain="";
while (my $row=<$fh>){$plain=$plain.$row;}
# print$plain;


my $body='<text lang="la"><body>';
$plain=~s/.* $body>//g;
print(substr($plain,0,20));

# print $filename;