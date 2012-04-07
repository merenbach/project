/* convert.js
 *
 * This script provides facilities for determining
 *   repeating, textual patterns in strings.
 *
 * It is used on Andrew Merenbach's website, http://www.merenbach.com/,
 *   but you are free to use it yourself under a BSD-style license.
 *   Modify it, reuse it, and have fun with it!  If you find any bugs,
 *   please let me know.
 *
 * All portions copyright (c) 2010 by Andrew Merenbach unless otherwise
 *  noted.  All rights reserved.
 *
 */

var sourceTextArea;
var outputTextArea;

function prepareFields() {
	sourceTextArea = document.getElementById('source');
	outputTextArea = document.getElementById('pattern');
}

/* create a detector object; configure its
 * instance variables; and search with it
 */
function convert() {
	// get things ready as process begins
	prepareFields();
	
	var source = sourceTextArea.value;
	
	var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
	
	var nums = new Array();
	
	var tmp = '';
	
	for (var i = 0; i < source.length; i++) {
		if (tmp == '') {
			tmp = source.charAt(i);
		} else {
			tmp += source.charAt(i);
			nums.push(tmp);
			tmp = '';
		}
	}
	
	if (tmp != '') {
		tmp += '0';
		nums.push(tmp);
	}
	
	var nums2 = '';
	
	for (var i = 0; i < nums.length; i++) {
		var n = parseInt(nums[i]) % alphabet.length;
		nums2 += alphabet.charAt(n);
	}
	
	output = nums2;
	
	outputTextArea.value = output;
}

// find patterns in a string that may have a non-pattern *prefix*
function match_pattern_left(str) {
	var pat = '';
	//$pat = $1 if $str =~ m/(.+?)(\1+)$/so;    // original Perl
	
	re = /(.+?)(\1+)$/; // current JavaScript code in place of original Perl
	var match = re.exec(str);
	if (match != null) {
		pat = match[1];
	}
	
	// if the output matches the input, no pattern was found;
	// set to empty string if this is the case
	//if (pat == str) pat = '';
	
	return pat;
}

// find patterns in a string that may have a non-pattern *suffix*
function match_pattern_right(str) {
	var pat = '';
	//$pat = $1 if $str =~ m/(.+?)(\1+)$/so;    // original Perl

	re = /^(.+)(\1+)/; // current JavaScript code in place of original Perl
	var match = re.exec(str);
	if (match != null) {
		pat = match[1];
	}

	// if the output matches the input, no pattern was found;
	// set to empty string if this is the case
	//if (pat == str) pat = '';
	
	return pat;
}

// find patterns in a string that comprises repeating instances of one string
function match_pattern_none(str) {
	var pat = '';
	//$pat = $1 if $str =~ m/(.+?)(\1+)$/so;    // original Perl

	re = /^(.+?)(\1+)$/; // current JavaScript code in place of original Perl
	var match = re.exec(str);
	if (match != null) {
		pat = match[1];
	}

	// if the output matches the input, no pattern was found;
	// set to empty string if this is the case
	//if (pat == str) pat = '';
	
	return pat;
}

