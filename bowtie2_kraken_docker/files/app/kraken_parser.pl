use strict;
use warnings;


open(IN, $ARGV[0])
or die "Unable to open source file $ARGV[0]\n";
open(OUT, ">>$ARGV[1]")
or die "Unable to open destination file $ARGV[1]\n";


my %tax_count;

while (my $line = <IN>)   {


   if ($line =~ /\S/)   {
      my @elements = split ("\t", $line);
      my $column1 = $elements[2];
      my $column2 = $elements[1];
      $tax_count{$column1}++;
   }
}

close(IN);



foreach my $key (keys %tax_count)  {
   
    print OUT "$key" . "\t" . "$tax_count{$key}\n";

}


close(OUT);
