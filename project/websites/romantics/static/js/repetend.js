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
 * All portions copyright (c) 2010 by Andrew Merenbach unless otherwise
 *  noted.  All rights reserved.
 */

var dividendTextField;
var divisorTextField;
var scaleTextField;
var quotientTextArea;
var repetendTextArea;
var repetendLengthTextField;

var DETECT_NULL = null;
var DETECT_YES = true;
var DETECT_NO = false;

function prepareFields() {
    dividendTextField = document.getElementById('dividend');
    divisorTextField = document.getElementById('divisor');
    scaleTextField = document.getElementById('scale');
    quotientTextArea = document.getElementById('quotient');
    repetendTextArea = document.getElementById('repetend');
    repetendLengthTextField = document.getElementById('replength');
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

function convertRadix(number, fromRadix, toRadix) {
    fromRadix = parseInt(fromRadix, 10);
    number = parseInt(number, fromRadix);
    toRadix = parseInt(toRadix, 10);
    var result = number.toString(toRadix);
    return result.toUpperCase();
}


/*dividend = convertRadix(dividend, 10, 6);
  divisor = convertRadix(divisor, 10, 6);
 */
/* A mod B = A - (B * floor(A/B))
   dividend % divisor = dividend - (divisor * floor(dividend / divisor))
 */

function divideFraction(dividend, divisor, scale) {
    var quotient = new StringBuffer();

    // convert args to integers
    var dividend = Math.floor(dividend);
    var divisor = Math.floor(divisor);
    var scale = Math.floor(scale);

    // move along to the first digit
    quotient.append(Math.floor(dividend / divisor).toString());

    if (scale > 0) {
        // no decimal point unless something follows
        quotient.append('.');

        // move along to successive digits until scale is exhausted
        while (scale--) {
            //dividend = 10 * (dividend - fraction * divisor);
            dividend = 10 * (dividend % divisor);
            quotient.append(Math.floor(dividend / divisor).toString());
        }
    }

    return quotient.toString();
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
