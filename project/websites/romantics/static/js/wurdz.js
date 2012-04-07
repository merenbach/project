/* vigenere.js
 *
 * This script provides facilities for encrypting and decrypting text
 *	according to the Vigenere tableau.
 *
 * It is used on Andrew Merenbach's website, http://www.merenbach.com/,
 *   but you are free to use it yourself under a BSD-style license.
 *   Modify it, reuse it, and have fun with it!  If you find any bugs,
 *   please let me know.
 *
 * Copyright (c) 2010 by Andrew Merenbach.  All rights reserved.
 */

var inputTextArea;
var outputTextArea;
var keywordTextField;
var offsetTextField;
var filterCheckBox;
var lowerCaseCheckBox;

var OPERATION_OPNULL = (-1);
var OPERATION_ENCODE = 0;
var OPERATION_DECODE = 1;

function prepareFields() {   
	inputTextArea = document.getElementById('source');
	outputTextArea = document.getElementById('target');
	keywordTextField = document.getElementById('keyword');
	offsetTextField = document.getElementById('offset');
	filterCheckBox = document.getElementById('filter');
	lowerCaseCheckBox = document.getElementById('lowercase');
}

/* create a transcoder object; configure its
 * instance variables; and transcode with it
 */
function processInput() {
	// get things ready as process begins
	prepareFields();
	
	var p = new processor();
	p.source = inputTextArea.value;
	p.target = '';
	
	p.process();
	
	outputTextArea.value = p.target;
}

function processor() {
	this.source = '';
	this.target = '';
	this.process = processText;
}

function processText() {
	inputString = this.source;
	pattern = '';
	
	var fa = new FrequencyAnalyzer(inputString);

	fa.analyze();
	
	var keyArray = fa.keyArray;
	var countedWordsArray = fa.countedArray;
	var totalWords = fa.totalWords();

	
	var code = '';
	code += "Statistics:\n";
	
	code += "\trepetitions\tfrequency\tword\n";
	code += "\t-----------\t---------\t----\n";
	
	// how many decimal places?
	var pScale = 100.0;
	
	for (idx = 0; idx < keyArray.length; idx++) {
		var theKey = keyArray[idx];
		var occurrences = countedWordsArray[theKey];
		var percent = occurrences / totalWords * 100.0;
		
        var o = occurrences;	//formatted occurrences
		var p = Math.round(percent * pScale) / pScale;
        var w = theKey;   // formatted word
		
		code += '\t' + o + '\t\t' + p + '%\t\t' + w + "\n";
	}

	this.target = code;
		     
	/*
    var sortedKeys = countedWords;
	sortedKeys.sort();
	
	//{$counted_words{$main::b} <=> $counted_words{$main::a}} keys %counted_words;

	for (idx = 0; idx < sortedKeys.length; idx++) {
		var sortKey = sortedKeys[idx];
        var occurrences = countedWords[sortKey];
        var percent = occurrences / totalWords * 100.0;
        
        var o = "\t" + occurrences;	//formatted occurrences
		var p = percent;
//        var p = sprintf("\t\t%.2f%%", $percent);    # formatted percentage
var p = percent;
        var w = "\t\t" + sortKey;   // formatted word
		
		code += o + p + w + "\n";
    }
	
	this.target = code;*/
}

/*sub main() {
    my %opts = ();
    
    if (!getopts('f:h', \%opts)) {
        die "Usage: wurdz.pl -f <filename> [-h]\n";
    }
    
    my $f = $opts{'f'};
    my $h = $opts{'h'};
    
    pod2usage(-verbose => 2) if defined $h;
    
    process_file($f) if defined $f;
}

sub read_file_with_path($) {
    my $MAX_FILE_READ_LEN = 2 ** 20 - 1;

    my $filename = shift;
    my $in = '';
    
    my $handle;
    open $handle, "<$filename" or die "Can't find file2 `$filename'.\n";
    read $handle, $in, $MAX_FILE_READ_LEN;
    close $handle;
    
    return $in;
}

sub process_file($) {
    my $filename = shift;

    my %counted_words = ();
    my $input_string = read_file_with_path($filename);
    my $total_words = 0;
    
    my $string = lc $input_string;
    
    my @words = split /\b/, $string;
    my $word;
        
    foreach (@words) {
        if (m/(\w+)/os) {
            if (defined $counted_words{$1}) {
                ++$counted_words{$1};
            }
            else {
                $counted_words{$1}++;
            }
            ++$total_words;
        }
    }
    
    my $word_plural_conditional = ($total_words != 1) ? 'words' : 'word';
    
    print "Statistics for file `$filename' ($total_words total $word_plural_conditional):\n";
    
    print "\trepetitions\tfrequency\tword\n";
    print "\t-----------\t---------\t----\n";
    
    my @keys_sorted = sort {$counted_words{$main::b} <=> $counted_words{$main::a}} keys %counted_words;
    
    foreach (@keys_sorted) {
        my $occurrences = $counted_words{$_};
        my $percent = $occurrences / $total_words * 100;
        
        my $o = "\t$occurrences";   # formatted occurrences
        my $p = sprintf("\t\t%.2f%%", $percent);    # formatted percentage
        my $w = "\t\t$_";   # formatted word

        print $o, $p, $w, "\n";
    }
}
*/
