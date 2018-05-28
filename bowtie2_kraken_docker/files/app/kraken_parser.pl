use strict;
use warnings;


open(IN, $ARGV[0])
or die "Unable to open source file $ARGV[0]\n";
open(OUT, ">>$ARGV[1]")
or die "Unable to open destination file $ARGV[1]\n";


my %tax_count;
my %tax_score;
my $score;

while (my $line = <IN>)   {


   if ($line =~ /\S/)   {
      my @elements = split ("\t", $line);
      my $column1 = $elements[2];
      my $column3 = $elements[4];

      


      if ($column3 =~ /^P=(.....)/) {
          $score = $1;
         
 
      
          $tax_count{$column1}++;
          $tax_score{$column1}+=$score;
      
      
       }
   }
}

close(IN);



foreach my $key (keys %tax_count)  {
   
    my $avg = $tax_score{$key}/$tax_count{$key};

    print OUT "$key" . "\t" . "$tax_count{$key}" . "\t" . $avg . "\n";
 

}


close(OUT);
