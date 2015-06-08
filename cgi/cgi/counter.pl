#!/usr/local/bin/perl
# Counter script written for UserActive Media
# Trent Johnson
# Created  :  6/29/98
# Modified :  6/29/98
# 
# COPYRIGHT NOTICE
# Copyright 1998 Trent Johnson
#
# This script comes with no warranty, Trent Johnson will not be held
# liable for anything that this script does.
#
# Anyone can borrow/steal/modify this script and do whatever they 
# want with it.
###########################################################################


# The user could change these if they wanted to use thier own digits
$width="24";
$height="24";
$imagedir = "/usr/local/lib/digits";


# Setup some variables for later use
# These should be right for everyone at UserActive
$username = $ENV{QUERY_STRING};
if ($username eq "") {
  print "Content-type:text/html\n\nMust have a username.<br>\n";
  print "Please see <a href=http://useractive.com/tech/counterintro.html>this</a>";
  exit;
}
unless ($username =~ /^[\w\d\-]+$/) { exit(1); }
$countfile = "/users/$username/count.txt";
$logfile = "/users/$username/access_log";
$fly = "/usr/local/bin/fly -q";
$tmp = "/users/$username/tmpfile";

# Do the actual count
$command = "echo \"0\">$countfile\n";
(-e $countfile) || system($command);
open(COUNT,"$countfile") || die "Can't open countfile for reading\n"; 
$count = <COUNT>;
close(COUNT);
if ($count =~ /\n$/) { chop($count); }
$count++;
open(COUNT,">$countfile") || die "Can't open countfile for writing\n";
print COUNT "$count";
close(COUNT);

# Get the image hacked together
$length = length($count);
$i=0;
while ($i<$length) { # perl for loops are broken have to use while
    $foo = substr($count,$i,1);
    $nums[$i] = $foo;
    $i++;
}
$totwidth = ($width * $length);
open(TMP,">$tmp") || die "Can't open tempfile for writing\n";
print TMP "new\n";
print TMP "size $totwidth,$height\n";

$i=0;
$cpwidth=0;
while ($i<$length) { # Yet another while where I want a for
  print TMP "copy $cpwidth,0,-1,-1,-1,-1,$imagedir/$nums[$i].gif\n";
  $cpwidth += $width;
  $i++;
}

close(TMP);

# Write the image
$foo = `$fly -i $tmp`;
print "Content-type: image/gif\n\n";
print "$foo";

unlink($tmp);

# Delete everything after this if you dont want a log
# Make a log entry
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
if ($sec < 10)  { $sec = "0$sec";   }
if ($min < 10)  { $min = "0$min";   }
if ($hour < 10) { $hour = "0$hour"; }
if ($mday < 10) { $mday = "0$mday"; }
if ($mon < 10)  { $monc = "0$mon";  }
$date = "$hour\:$min\:$sec $mon/$mday/$year";

# Write to the log
open(LOG,">>$logfile") || die "Can't Open User Access Log: $!\n";
print LOG "[$date] $ENV{'REMOTE_HOST'} -  $ENV{'HTTP_USER_AGENT'}\n";
close(LOG);

open(AAA,">/users/$username/envtest");
$aa = $ENV{'HTTP_REFERER'};
print AAA "$aa\n";
close(AAA);










