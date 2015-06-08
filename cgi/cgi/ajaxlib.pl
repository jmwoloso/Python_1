#!/usr/bin/perl



sub parse_input

{

$whichmethod = $ENV{'REQUEST_METHOD'};
if($whichmethod eq "GET"){

       $forminfo = $ENV{"QUERY_STRING"};

}else{

$forminfo = <STDIN>; }

@key_value_pairs = split(/&/,$forminfo); 

foreach $pair (@key_value_pairs){
	($key,$value) = split(/=/,$pair);
	$value =~ s/\+/ /g; 
	$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
	$FORM_DATA{$key} = $value;
}

} 

sub print_header 

{

print "Content-type: text/html\n\n"; 

} 

return 1;
