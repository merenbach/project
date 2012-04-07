/* repetend.js
 *
 * This script provides facilities for calculating the quotient
 *   and repetend of a long-division equation.
 *
 * It is used on Andrew Merenbach's website, http://www.merenbach.com/,
 *   but you are free to use it yourself under a BSD-style license.
 *   Modify it, reuse it, and have fun with it!  If you find any bugs,
 *   please let me know.
 *
 * Copyright (c) 2010 by Andrew Merenbach.  All rights reserved.
 */

var gronsfeldStringTextField;
var dividendTextField;
var divisorTextField;
var scaleTextField;
var quotientTextArea;
var repetendTextArea;
var repetendLengthTextField;
var keyOutTextArea;
//var keyOutPaddedTextArea;
var frequencyTextArea;
var chunkSizeTextField;

var DETECT_NULL = null;
var DETECT_YES = true;
var DETECT_NO = false;

function prepareFields() {
    gronsfeldStringTextField = document.getElementById('gronsfeld');
	dividendTextField = document.getElementById('dividend');
	divisorTextField = document.getElementById('divisor');
	scaleTextField = document.getElementById('scale');
	quotientTextArea = document.getElementById('quotient');
	repetendTextArea = document.getElementById('repetend');
	repetendLengthTextField = document.getElementById('replength');
	keyOutTextArea = document.getElementById('keyout');
	//keyOutPaddedTextArea = document.getElementById('keyoutpadded');
	frequencyTextArea = document.getElementById('frequency');
	chunkSizeTextField = document.getElementById('chunk');
}

/* create a calculator object; configure its
 * instance variables; and calculate with it
 */
function process() {
	// get things ready as process begins
	prepareFields();
	
	// create and configure our calculator
	var c = new calculator();
	c.dividend = dividendTextField.value;
	c.divisor = divisorTextField.value;
	c.scale = scaleTextField.value;
	c.quotient = '';
	c.repetend = '';
	
	// determine whether or not we detect the repetend
	var repetendDetect = detectRadioValue('detect');
	switch(repetendDetect) {
		case 'yes': c.detect = DETECT_YES; break;
		case 'no': c.detect = DETECT_NO; break;
		default: c.detect = DETECT_NULL; break;
	}
	
	// launch the calculation
	c.calculate();
	
	// display the output
	quotientTextArea.value = c.quotient;
	repetendTextArea.value = c.repetend;
	repLen = '';
	if (c.detect == DETECT_YES && c.repetend != '') {
		repLen = c.repetend.length;
		conv = convert(c.repetend);
		keyOutTextArea.value = conv;
		//pd = padString(conv, 1, 'X');
		//pd = splitString(conv, 1);
		//keyOutPaddedTextArea.value = pd;
			
		var chunkSize = chunkSizeTextField.value;
		if (chunkSize <= 0) {
			chunkSize = 1;
		}
		
		var theSplit = splitString(conv, chunkSize);
		alert('hi');
		alert(theSplit);
		var fa = new FrequencyAnalyzer(theSplit);
		
		fa.analyze();
		
		var keyArray = fa.keyArray;
		var countedWords = fa.countedArray;
		var totalWords = fa.totalWords();
		
		var code = '';

		for (idx = 0; idx < keyArray.length; idx++) {
			var theKey = keyArray[idx];
			var occurr = countedWords[theKey];
			code += theKey + ' --- ' + occurr + '\n';
		}
		
		frequencyTextArea.value = code;
	}
	
	repetendLengthTextField.value = repLen;
}

function calculator() {
	this.dividend = 0;
	this.divisor = 0;
	this.scale = 0;
	this.quotient = '';
	this.repetend = '';
	this.detect = DETECT_NULL;
	
	this.calculate = calculateQuotient;
	this.validate = validateInput;
	this.divide = divideFraction;
	this.matchPattern = matchPatternLeft;
}

function calculateQuotient() {
	var dividend = this.dividend;
	var divisor = this.divisor;
	var scale = this.scale;
	
	// filter digits	
	var validatedInput = this.validate(dividend, divisor, scale);
    if (validatedInput) {
        var quotient = this.divide(dividend, divisor, scale);	
        this.quotient = quotient;
    } else {
        this.quotient = '';
    }
	
	if (this.detect) {
		// search for the repetend
		this.repetend = this.matchPattern(this.quotient);
	}
}

function divideFraction(dividend, divisor, scale) {
	var quotient = '';
	
	// convert args to integers
	var dividend = Math.floor(dividend);
	var divisor = Math.floor(divisor);
	var scale = Math.floor(scale);
	
	// move along to the first digit
	fraction = Math.floor (dividend / divisor);
	quotient += fraction;
	dividend = 10 * (dividend - fraction * divisor);

	if (scale > 0) {
		// no decimal point unless something follows
		quotient += '.';
		
		// move along to successive digits until scale is exhausted
		while (scale--) {
			fraction = Math.floor (dividend / divisor);
			quotient += fraction;
			dividend = 10 * (dividend - fraction * divisor);
		}
	}

	return quotient;
}

function validateInput(n, d, s) {
	var flag = true;

    //var re = new RegExp('[^0-9]', 'g');
    var re = /[^0-9]/g;
    if (n != n.replace(re, '')) {
        flag = false;
    }
    if (d != d.replace(re, '')) {
        flag = false;
    }
    if (s != s.replace(re, '')) {
        flag = false;
    }

	if (n < 0) {
		// Dividend must be a nonnegative integer.
		flag = false;
	}
	if (d <= 0) {
		// Divisor must be a positive integer.
		flag = false;
	}
	if (s < 0) {
		// Scale must be a nonnegative integer.
		flag = false;
	}
	if (s > 1000000) {
		// Scale is too large.  Please select a smaller scale.
		flag = false;
	}
	if (n == NaN || d == NaN || s == NaN) {
		flag = false;
	}
	
	return flag;
}

// borrowed from Paisley
function matchPatternLeft(str) {
	var pat = '';
	//$pat = $1 if $str =~ m/(.+?)(\1+)$/so;    // original Perl
    
    //var re = new RegExp('(.+?)(\\1+)$');  // escape backslashes
	var re = /(.+?)(\1+)$/; // current JavaScript code in place of original Perl
	var match = re.exec(str);
	if (match != null) {
		pat = match[1];
	}

	/* if the output matches the input, no pattern was found;
	 * set to empty string if this is the case
     */
	//if (pat == str) pat = '';
	
	return pat;
}

var OPERATION_OPNULL = (-1);
var OPERATION_ENCODE = 0;
var OPERATION_DECODE = 1;

function convert(str) {
	// get things ready as process begins
	
    var tc = new transcoderForGronsfeld();
    tc.numbers = '0123456789';
    tc.standardAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    tc.alphabet = tc.standardAlphabet + tc.numbers;
    tc.operation = OPERATION_ENCODE;
    tc.source = gronsfeldStringTextField.value;
    tc.numericKey = str;
    tc.filter = true;
    tc.chunkSize = 0;
    //tc.primerIndex = 0;
	
	tc.process();
	
	output = tc.target;
	
	return output;
}


/* rehash (hopefully temporarily) of ciphers.js code; do not copy from here, but from ciphers.js */

function transcoderForGronsfeld() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.numbers = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.numericKey = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var numericKey = this.numericKey;
		var alphabetKey = this.alphabetKey;
		var primerIndex = this.primerIndex;
		var filter = this.filter;
		var operation = this.operation;
		var chunkSize = this.chunkSize;
		
		// filter parameters
		primerIndex = filterNumber(primerIndex);
		
		// constrain parameters
		primerIndex %= this.alphabet.length;
		
		// should we filter the input?
		if (this.filter == true) {
			input = filterAlphanumeric(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}

		// transform parameters
		input = input.toUpperCase();
		
		// filter and constrain
		numericKey = filterNumber(numericKey);
		
		//passphrase = passphrase.toUpperCase();
		//passphrase = filterString(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaGronsfeldExtended(this.alphabet, this.numbers, primerIndex);
		
		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, numericKey, table); break;
			case OPERATION_DECODE: output = this.decode(input, numericKey, table); break;
			default: operation = ''; break;	// no valid operation specified
		}
		
		// divide the string, if necessary
		if (this.filter == true) {
			if (chunkSize > 0) {
				output = splitString(output, chunkSize);
			}
		}
			
		// should we convert the output to lowercase?
		if (this.lowercase) {
			output = output.toLowerCase();
		}
		
		// display the output
		this.target = output;
	}
	
	this.encode = AMCipherUtilities.encodeGronsfeld;
	this.decode = AMCipherUtilities.decodeGronsfeld;
	
	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.numbers, this.alphabetKey);
		this.numbers = '0123456789';
	}
}