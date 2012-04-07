/* paisley.js
 *
 * This script provides facilities for determining
 *   repeating, textual patterns in strings.
 *
 * It is used on Andrew Merenbach's website, http://www.merenbach.com/,
 *   but you are free to use it yourself under a BSD-style license.
 *   Modify it, reuse it, and have fun with it!  If you find any bugs,
 *   please let me know.
 *
 * Copyright (c) 2010 by Andrew Merenbach.  All rights reserved.
 */

var sourceTextArea;
var outputTextArea;

var DIRECTION_NULL = (-1);
var DIRECTION_NO = 0;
var DIRECTION_LT = 1;
var DIRECTION_RT = 2;

function prepareFields() {
	sourceTextArea = document.getElementById('source');
	outputTextArea = document.getElementById('pattern');
}

/* create a detector object; configure its
 * instance variables; and search with it
 */
function search() {
	// get things ready as process begins
	prepareFields();
	
	// create and configure our detector
	var d = new detector();
	d.source = sourceTextArea.value;
	d.target = '';
	
	// determine the direction for searching
	var directionDetect = detectRadioValue('direction');
	switch(directionDetect) {
		case 'none': d.direction = DIRECTION_NO; break;
		case 'left': d.direction = DIRECTION_LT; break;
		case 'right': d.direction = DIRECTION_RT; break;
		default: d.direction = DIRECTION_NULL; break;
	}
	
	// search for patterns and display the results
	d.detect();
	outputTextArea.value = d.target;
}

function detector() {
	this.source = '';
	this.target = '';
	this.direction = DIRECTION_NULL;
	
	this.detect = determinePattern;
	this.matchNone = match_pattern_none;
	this.matchLeft = match_pattern_left;
	this.matchRight = match_pattern_right;
}

function determinePattern() {
	source = this.source;
	pattern = '';
	
	switch(this.direction) {
		case DIRECTION_NO: pattern = this.matchNone(source); break;
		case DIRECTION_LT: pattern = this.matchLeft(source); break;
		case DIRECTION_RT: pattern = this.matchRight(source); break;
		default: pattern = ''; break;	// do nothing
	}
	
	this.target = pattern;
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
