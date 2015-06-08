#!/usr/local/bin/perl
#
# Copyright 1996 Trent Johnson, UserActive Media
# Created       6/30/98
# Last Modified 7/20/98
#
# For use by UserActive SUPERUSERS
#
# This script comes with no warranty, the author(s) will not be held
# liable for anything that this script does.
#
# Anyone can borrow/steal/modify this script and do what they want with it.
###########################################################################
require 'cgi-lib.pl';
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$mon++;
$ltime = "$hour:"."$min:"."$sec  "."$mon/"."$mday/"."$year";

&ReadParse;
print "Content-type: text/html\n\n";

if ($ENV{QUERY_STRING} eq "" ) {
    print "Please read the intructions for setting up your guestbook ";
    print "<a href=http://www.useractive.com/tech/guestintro.html>here</a>";
    exit;
}


($aname,$city,$comments,$country,$realname,$state,$url,$username) = sort (keys %in);
$aname=$in{$aname};
$city=$in{$city};
$comments=$in{$comments};
$country=$in{$country};
$realname=$in{$realname};
$state=$in{$state};
$url=$in{$url};
$username=$in{$username};

$aname =~ s/[^\w\d\.\-\s\'\"\(\)\@\/]/ /g;
$city =~ s/[^\w\d\.\-\s\'\"\(\)\@\/]/ /g;
$comments =~ s/[^\w\d\.\-\s\'\"\(\)\@\/]/ /g;
$country =~ s/[^\w\d\.\-\s\'\"\(\)\@\/]/ /g;
$realname =~ s/[^\w\d\.\-\s\'\"\(\)\@\/]/ /g;
$state =~ s/[^\w\d\.\-\s\'\"\(\)\@\/]/ /g;
$url =~ s/[^\w\d\.\-\s\'\"\(\)\@]/ /g; 
$username =~ s/[^\w\d\.\-\s\'\"\(\)\@]/ /g;

if ($aname eq "USERNAME" ) {
    print "You forgot to set the username variable in add.html<br>\n";
    print "Please read the intructions for setting up your guestbook ";
    print "<a href=http://www.useractive.com/tech/guestintro.html>here</a>";
    exit;
}



print "<body bgcolor=\"FFFFFF\">";
print "<TITLE>My Guestbook</TITLE>\n";
print "<center><H1>My Guestbook</H1></center>","<P>\n";
print "<BR>\n";



$user = $aname;
$guestfile = "/users/$user/guestbook/guestbook.$user.html";
$welcome = "/guestbook/guestbook.$user.html";

$url="http://" . $url;


unless (open(BOOK,"<$guestfile")) {
    open(BOOK,"/usr/local/lib/guestbook.superusers.html");
    mkdir("/users/$user/guestbook",0755);
}

for($i=0;$i<=$#lines;$i++) {
    $lines[$i] =~ s/USERNAME/$user/g;
}


@lines=<BOOK>;
close(BOOK);

$i=0;
while($i <= $#lines){
	$_ = $lines[$i];
	if(/<!--begin-->/){
		$i++;
		if($url ne ""){
		        splice(@lines,$i,0,"<a href=\"$url\">$realname</a><br>\n");
			$i++;
		}else{
		        splice(@lines,$i,0,"$realname<Br>\n");
			$i++;
		}
		if($username ne ""){
		        splice(@lines,$i,0,"<a href=\"mailto:$username\">$username</a><br>\n");
			$i++;
		}
		splice(@lines,$i,0,"<b>$comments</b><Br>\n","$city, $state $country - $ltime <hr>\n");		
	}
$i++;
}
open(BOOK,">$guestfile") || die "DIE!!";
print BOOK @lines;
close(BOOK);

print "You posted this information:", "<p>", "\n";
if($url ne ""){
	print "<a href=\"$url\">$realname</a><br>\n";
}else{
	print $realname, "<Br>\n";
}
if($username ne ""){
	print "<a href=\"mailto:$username\">$username</a><br>\n";
}
print "<b>",$comments, "</b><Br>\n";
print "$city, $state $country - $ltime <p>\n";
print "View the <a href=\"$welcome\">guestbook.</a>";
print "</body>\n";



