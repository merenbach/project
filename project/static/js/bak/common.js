/* common.js
 *
 * This script provides supportive features and utility functions for the
 *	various functions on Andrew's Lab.  Furthermore, it includes
 *	 facilities to help transcode text according to various ciphers.
 *
 * It is used on Andrew Merenbach's website, http://www.merenbach.com/,
 *	 but you are free to use it yourself under a BSD-style license.
 *	 Modify it, reuse it, and have fun with it!	 If you find any bugs,
 *	 please let me know.
 *
 * All portions copyright (c) 2010 by Andrew Merenbach unless otherwise
 *  noted.  All rights reserved.
 */

function detectRadioValue(name) {
    var value = null;
    var r = document.getElementsByName(name);
    for (var i = 0; i < r.length; i++) {
        var item = r.item(i);
        if (item.checked) {
            value = item.value;
            break;
        }
    }
    return value;
}

function filterAlphanumeric(input) {
    var output = '';
    var string = input.toString();
    if (string.length > 0) {
        var re = /[^0-9A-Za-z]/g;
        output = string.replace(re, '');
    }
    return output;
}

function filterString(input) {
    var output = '';
    var string = input.toString();
    if (string.length > 0) {
        var re = /[^A-Za-z]/g;
        output = string.replace(re, '');
    }
    return output;
}

function filterNumber(input) {
    var output = 0;
    var string = input.toString();
    if (string.length > 0) {
        var re = /[^0-9]/g;
        output = string.replace(re, '');
    }
    return output;
}

function uniqueString(input) {
    var output = '';

    for (var i = 0; i < input.length; i++) {
        var c = input.charAt(i);
        if (input.indexOf(c) == i) {
            output += c;
        }
    }

    return output;
}

/*function filter_digits(str) {
//my $count = $$ref =~ tr/0-9//cd;
$$ref = 0 if ($$ref eq '' || $count > 0);
}*/

function extendedGCD(a, b) {
    var solution = new Array(3);
    if (b == 0) {
        solution[0] = 1;
        solution[1] = 0;
        solution[2] = a;
    } else {
        var gcd = extendedGCD(b, a % b);
        var x = gcd[0];
        var y = gcd[1];
        var d = gcd[2];
        solution[0] = y;
        solution[1] = x - y * Math.floor(a / b);
        solution[2] = d;
    }
    return solution;
}

function wrapString(string, offset) {
    var shifted = '';

    if (string.length > 0) {
        offset = filterNumber(offset);
        offset %= string.length;

        var initial = string.substring(offset, string.length);
        var remainder = string.substring(0, offset);

        shifted = initial + remainder;
    }

    return shifted;
}

function reverseString(string) {
    var output = '';

    if (string.length > 0) {
        for (var i = string.length - 1; i >= 0; i--) {
            output += string.charAt(i);
        }
    }

    return output;
}

// padding necessary to extend "string" to a multiple of "chunk"
function paddingNeeded(string, chunk) {
    return (string.length * (chunk - 1)) % chunk;
}

function padString(string, chunk, c) {
    var padding = paddingNeeded(string, chunk);
    for (var i = 0; i < padding; i++) {
        string += c;
    }
    return string;
}

function splitString(string, size) {
    var output = '';
    size = filterNumber(size);
    for (var i = 0; i < string.length; i++) {
        if (i % size == 0 && i > 0) {
            output += ' ';
        }
        output += string.charAt(i);
    }
    return output;
}

Array.prototype.contains = function(obj) {
    var i = this.length;
    while (i--) {
        if (this[i] === obj) {
            return true;
        }
    }
    return false;
}

/* analyzes frequency of (generally-speaking) words */
function FrequencyAnalyzer(str) {
    this.sourceText = str;
    this.wordArray = new Array();
    this.countedArray = new Array();
    this.keyArray = new Array();

    this.analyze = function() {
        var convertedString = this.sourceText.toLowerCase();
        var re = /\W+/g;

        this.wordArray = convertedString.split(re);

        var newCountedArray = new Array();
        var newKeyArray = new Array();

        for (idx = 0; idx < this.wordArray.length; idx++) {
            word = this.wordArray[idx];

            if (newCountedArray[word] >= 1) {
                newCountedArray[word]++;
            } else {
                newCountedArray[word] = 1;
                newKeyArray.push(word);
            }
        }

        this.countedArray = newCountedArray;
        this.keyArray = sortByValueDesc(newKeyArray, newCountedArray);
    }

    this.totalWords = function() {
        var total = 0;

        for (idx = 0; idx < this.keyArray.length; idx++) {
            var theKey = this.keyArray[idx];
            total += this.countedArray[theKey];
        }

        return total;
    }
}

/*function sortByValue(keyArray, valueMap) {
  return keyArray.sort(function(a,b){return valueMap[a]-valueMap[b];});
  }*/

function sortByValueDesc(keyArray, valueMap) {
    return keyArray.sort(function(b,a){return valueMap[a]-valueMap[b];});
}

var AMCipherUtilities = {
canonicalAlphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                   canonicalNumbers: '0123456789',
                   paddingCharacter: 'x',

                   generateTabulaRecta: function(alphabet, primerIndex) {
                       var table = new Array();

                       // filter and constrain alphabet
                       alphabet = filterString(alphabet);
                       alphabet = uniqueString(alphabet);
                       alphabet = alphabet.toUpperCase();

                       // filter and constrain primer index
                       primerIndex = filterNumber(primerIndex);
                       primerIndex %= alphabet.length;

                       if (primerIndex < alphabet.length) {
                           for (var i = 0; i < alphabet.length; i++) {
                               var ab = wrapString(alphabet, i + parseInt(primerIndex));
                               table.push(ab);
                           }
                       }
                       return table;
                   },

generateTabulaRectaExtended: function(alphabet, primerIndex) {
                                 var table = new Array();

                                 // filter and constrain alphabet
                                 alphabet = filterAlphanumeric(alphabet);
                                 alphabet = uniqueString(alphabet);
                                 alphabet = alphabet.toUpperCase();

                                 // filter and constrain primer index
                                 primerIndex = filterNumber(primerIndex);
                                 primerIndex %= alphabet.length;

                                 if (primerIndex < alphabet.length) {
                                     for (var i = 0; i < alphabet.length; i++) {
                                         var ab = wrapString(alphabet, i + parseInt(primerIndex));
                                         table.push(ab);
                                     }
                                 }
                                 return table;
                             },

generateTabulaGronsfeld: function(alphabet, digits, primerIndex) {
                             var table = new Array();

                             // filter and constrain alphabet
                             alphabet = filterString(alphabet);
                             alphabet = uniqueString(alphabet);
                             alphabet = alphabet.toUpperCase();

                             // filter and constrain primer index		
                             primerIndex = filterNumber(primerIndex);
                             primerIndex %= alphabet.length;

                             if (primerIndex < digits.length) {
                                 for (var i = 0; i < digits.length; i++) {
                                     var ab = wrapString(alphabet, i + parseInt(primerIndex));
                                     table.push(ab);
                                 }
                             }

                             return table;
                         },

generateTabulaGronsfeldExtended: function(alphabet, digits, primerIndex) {
                                     var table = new Array();

                                     // filter and constrain alphabet
                                     alphabet = filterAlphanumeric(alphabet);
                                     alphabet = uniqueString(alphabet);
                                     alphabet = alphabet.toUpperCase();

                                     // filter and constrain primer index
                                     primerIndex = filterNumber(primerIndex);
                                     primerIndex %= alphabet.length;

                                     if (primerIndex < digits.length) {
                                         for (var i = 0; i < digits.length; i++) {
                                             var ab = wrapString(alphabet, i + parseInt(primerIndex));
                                             table.push(ab);
                                         }
                                     }
                                     return table;
                                 },

simpleCodewordAlphabet: function(alphabet, keyword) {
                            var ab = '';

                            // filter and constrain keyword
                            keyword = keyword.toUpperCase();	// convert keyword to upper-case
                            keyword = filterString(keyword);	// filter disallowed characters
                            keyword = uniqueString(keyword);	// remove duplicate characters

                            if (keyword.length > 0) {
                                ab = keyword;

                                if (ab.length != alphabet.length) {
                                    //alphabet_copy =~ s/[\Q$ab\E]//gs;
                                    var re = new RegExp("[" + ab + "]", "g");
                                    var alphabetTrimmed = alphabet.replace(re, '');
                                    ab += alphabetTrimmed;
                                }
                            } else {
                                ab = alphabet;
                            }

                            return ab;
                        },

simpleCodewordAlphabetWithNumbers: function(alphabet, numbers, keyword) {
                                       var ab = '';

                                       // filter and constrain keyword
                                       keyword = keyword.toUpperCase();	// convert keyword to upper-case
                                       keyword = filterAlphanumeric(keyword);	// filter disallowed characters
                                       keyword = uniqueString(keyword);	// remove duplicate characters

                                       alphabet += numbers;

                                       if (keyword.length > 0) {
                                           ab = keyword;

                                           if (ab.length != alphabet.length) {
                                               //alphabet_copy =~ s/[\Q$ab\E]//gs;
                                               var re = new RegExp("[" + ab + "]", "g");
                                               var alphabetTrimmed = alphabet.replace(re, '');
                                               ab += alphabetTrimmed;
                                           }
                                       } else {
                                           ab = alphabet;
                                       }

                                       return ab;
                                   },

monoalphabeticTranscode: function(input, alphabets, shouldFilter, shouldDemote, chunkSize) {
                             var output = '';

                             var a;	// pre-transcoded character
                             var b;	// post-transcoded character
                             var j;	// index of pre-transcoded character in canonical alphabet

                             // filter chunk size
                             chunkSize = filterNumber(chunkSize);

                             // filter and pad the string (if necessary)
                             if (shouldFilter == true) {
                                 input = filterString(input);
                                 if (chunkSize > 0) {
                                     input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
                                 }
                             }

                             // convert input to upper-case (currently necessary for processing)
                             input = input.toUpperCase();

                             for (var i = 0; i < input.length; i++) {
                                 a = input.charAt(i);
                                 j = alphabets[0].indexOf(a);
                                 b = '';
                                 if (j != (-1)) {
                                     // matched to the coded alphabet
                                     b = alphabets[1].charAt(j);
                                 } else {
                                     // not matched, so append verbatim; may occur with punctuation
                                     b = a;
                                 }
                                 output += b;
                             }

                             // divide the string, if necessary
                             if (shouldFilter == true) {
                                 if (chunkSize > 0) {
                                     output = splitString(output, chunkSize);
                                 }
                             }

                             if (shouldDemote == true) {
                                 output = output.toLowerCase();
                             }

                             return output;
                         },

affineAlphabetsForEncryption: function(alphabet, multiplier, additive) {
                                  var alphabets = new Array(2);

                                  // filter alphabet... for now
                                  //	(unless we wish to expand the character set)
                                  alphabet = alphabet.toUpperCase();
                                  alphabet = filterString(alphabet);
                                  alphabet = uniqueString(alphabet);

                                  // filter parameters
                                  multiplier = filterNumber(multiplier);
                                  additive = filterNumber(additive);

                                  // constrain parameters
                                  multiplier %= alphabet.length;
                                  additive %= alphabet.length;

                                  if (alphabet.length > 0) {
                                      var alphabetLength = alphabet.length;

                                      var gcd = extendedGCD(alphabetLength, multiplier);
                                      if (multiplier % 2 != 0 && gcd[2] == 1) {
                                          var temp = '';
                                          for (var i = 0; i < alphabetLength; i++) {
                                              // if we're a letter, transpose
                                              var aPrime = (parseInt(multiplier) * i + parseInt(additive)) % alphabetLength;
                                              temp += alphabet.charAt(aPrime);	// append alphabet character
                                          }
                                          alphabets[0] = alphabet;
                                          alphabets[1] = temp;
                                      } else {
                                          alphabets[0] = '';
                                          alphabets[1] = '';
                                      }
                                  } else {
                                      alphabets[0] = '';
                                      alphabets[1] = '';
                                  }

                                  return alphabets;
                              },

affineAlphabetsForDecryption: function(alphabet, multiplier, additive) {
                                  var alphabets = new Array(2);

                                  // filter alphabet... for now
                                  //	(unless we wish to expand the character set)
                                  alphabet = alphabet.toUpperCase();
                                  alphabet = filterString(alphabet);
                                  alphabet = uniqueString(alphabet);

                                  // filter parameters
                                  multiplier = filterNumber(multiplier);
                                  additive = filterNumber(additive);

                                  // constrain parameters
                                  multiplier %= alphabet.length;
                                  additive %= alphabet.length;

                                  if (alphabet.length > 0) {
                                      var alphabetLength = alphabet.length;

                                      var gcd = extendedGCD(alphabetLength, multiplier);
                                      if (multiplier % 2 != 0 && gcd[2] == 1) {
                                          var temp = '';
                                          var multiplicativeInverse = (gcd[1] + alphabetLength) % alphabetLength;
                                          for (var i = 0; i < alphabetLength; i++) {
                                              // if we're a letter, transpose
                                              var aPrime = (multiplicativeInverse * (i - parseInt(additive) + alphabetLength)) % alphabetLength;
                                              temp += alphabet.charAt(aPrime);	// append alphabet character
                                          }
                                          alphabets[0] = alphabet;
                                          alphabets[1] = temp;
                                      } else {
                                          alphabets[0] = '';
                                          alphabets[1] = '';
                                      }
                                  } else {
                                      alphabets[0] = '';
                                      alphabets[1] = '';
                                  }

                                  return alphabets;
                              },

codewordAlphabetsForEncryption: function(alphabet, keyword) {
                                    var alphabets = new Array(2);

                                    // filter alphabet
                                    alphabet = alphabet.toUpperCase();
                                    alphabet = filterString(alphabet);
                                    alphabet = uniqueString(alphabet);

                                    // filter keyword
                                    keyword = keyword.toUpperCase();	// convert keyword to upper-case
                                    keyword = filterString(keyword);	// filter disallowed characters
                                    keyword = uniqueString(keyword);	// remove duplicate characters

                                    if (alphabet.length > 0) {
                                        if (keyword.length > 0) {
                                            var ab = '';

                                            if (keyword != alphabet) {
                                                //alphabet_copy =~ s/[\Q$ab\E]//gs;
                                                ab = keyword;
                                                var re = new RegExp("[" + ab + "]", "g");
                                                var alphabetTrimmed = alphabet.replace(re, '');
                                                ab += alphabetTrimmed;
                                            } else {
                                                ab = alphabet;
                                            }

                                            alphabets[0] = alphabet;
                                            alphabets[1] = ab;
                                        } else {
                                            alphabets[0] = alphabet;
                                            alphabets[1] = alphabet;
                                        }
                                    } else {
                                        alphabets[0] = '';
                                        alphabets[1] = '';
                                    }

                                    return alphabets;
                                },

codewordAlphabetsForDecryption: function(alphabet, keyword) {
                                    var alphabets = new Array(2);

                                    // filter alphabet
                                    alphabet = alphabet.toUpperCase();
                                    alphabet = filterString(alphabet);
                                    alphabet = uniqueString(alphabet);

                                    // filter keyword
                                    keyword = keyword.toUpperCase();	// convert keyword to upper-case
                                    keyword = filterString(keyword);	// filter disallowed characters
                                    keyword = uniqueString(keyword);	// remove duplicate characters

                                    if (alphabet.length > 0) {
                                        if (keyword.length > 0) {
                                            var ab = '';

                                            if (keyword != alphabet) {
                                                //alphabet_copy =~ s/[\Q$ab\E]//gs;
                                                ab = keyword;
                                                var re = new RegExp("[" + ab + "]", "g");
                                                var alphabetTrimmed = alphabet.replace(re, '');
                                                ab += alphabetTrimmed;
                                            } else {
                                                ab = alphabet;
                                            }

                                            alphabets[0] = ab;
                                            alphabets[1] = alphabet;
                                        } else {
                                            alphabets[0] = alphabet;
                                            alphabets[1] = alphabet;
                                        }
                                    } else {
                                        alphabets[0] = '';
                                        alphabets[1] = '';
                                    }

                                    return alphabets;
                                },

caesarAlphabetsForEncryption: function(alphabet, offset) {
                                  var alphabets = new Array(2);

                                  // constrain alphabet
                                  alphabet = alphabet.toUpperCase();
                                  alphabet = filterString(alphabet);
                                  alphabet = uniqueString(alphabet);

                                  // constrain offset
                                  offset = filterNumber(offset);
                                  offset %= alphabet.length;

                                  if (alphabet.length > 0) {
                                      var temp = '';

                                      if (offset >= 0) {
                                          temp = wrapString(alphabet, offset);
                                      } else {
                                          temp = alphabet;
                                      }

                                      alphabets[0] = alphabet;
                                      alphabets[1] = temp;
                                  } else {
                                      alphabets[0] = '';
                                      alphabets[1] = '';
                                  }

                                  return alphabets;
                              },

caesarAlphabetsForDecryption: function(alphabet, offset) {
                                  var alphabets = new Array(2);

                                  // constrain alphabet
                                  alphabet = alphabet.toUpperCase();
                                  alphabet = filterString(alphabet);
                                  alphabet = uniqueString(alphabet);

                                  // constrain offset
                                  offset = filterNumber(offset);
                                  offset %= alphabet.length;

                                  if (alphabet.length > 0) {
                                      var temp = '';

                                      if (offset >= 0) {
                                          temp = wrapString(alphabet, offset);
                                      } else {
                                          temp = alphabet;
                                      }

                                      alphabets[0] = temp;
                                      alphabets[1] = alphabet;
                                  } else {
                                      alphabets[0] = '';
                                      alphabets[1] = '';
                                  }

                                  return alphabets;
                              },

encodeVigenere: function(input, key, table) {
                    var output = '';

                    if (key.length > 0) {
                        var passphraseIndex = 0;	// current iterated passphrase character index

                        var c;	// current iterated input character
                        var k;	// current iterated passphrase character
                        var row;	// row of the passphrase character in the table
                        var col;	// col of the message character in the table
                        var charTemp;	// copy of c

                        for (var i = 0; i < input.length; i++) {
                            c = input.charAt(i);
                            k = key.charAt(passphraseIndex % key.length);
                            row = this.alphabet.indexOf(k) % this.alphabet.length;
                            col = this.alphabet.indexOf(c) % this.alphabet.length;

                            charTemp = c;

                            if (row != (-1) && col != (-1)) {
                                charTemp = table[row].charAt(col);
                                passphraseIndex++;
                                passphraseIndex %= key.length;
                            }

                            output += charTemp;
                        }
                    } else {
                        output = input;
                    }

                    return output;
                },

decodeVigenere: function(input, key, table) {
                    var output = '';

                    if (key.length > 0) {
                        var passphraseIndex = 0;	// current iterated passphrase character index

                        var c;		// current iterated message character
                        var k;		// current iterated passphrase character
                        var col;	// col of the message character in the table
                        var row;	// row of the passphrase character in the table

                        for (var i = 0; i < input.length; i++) {
                            var c = input.charAt(i);
                            var k = key.charAt(passphraseIndex % key.length); 
                            var col = this.alphabet.indexOf(k);

                            if (col != (-1)) {
                                var row = table[col].indexOf(c);

                                if (row != (-1)) {
                                    c = this.alphabet.charAt(row);
                                    passphraseIndex++;
                                    passphraseIndex %= key.length;
                                }

                                output += c;
                            }
                        }
                    } else {
                        output = input;
                    }

                    return output;
                },

encodeAutokeyVigenere: function(input, key, table) {
                           var output = '';

                           if (key.length > 0) {
                               // add input (filtered) to passphrase
                               //key += filterString(input);
                               /* This has the unintended side effect of stripping out numbers,
                                * which may be desirable (say with a custom tableau).  Instead,
                                * we'll add characters to the passphrase one by one once they
                                * have passed alphabet "validation" or "verification" below;
                                * viz., they'll need to be present in the alphabet and tableau
                                * before they go on to the key.  This is a good way to avert
                                * the generation of indecipherable gibberish.
                                */

                               var passphraseIndex = 0;	// current iterated passphrase character index

                               var c;	// current iterated input character
                               var k;	// current iterated passphrase character
                               var row;	// row of the passphrase character in the table
                               var col;	// col of the message character in the table
                               var charTemp;	// copy of c

                               for (var i = 0; i < input.length; i++) {
                                   c = input.charAt(i);
                                   k = key.charAt(passphraseIndex % key.length);
                                   row = this.alphabet.indexOf(k) % this.alphabet.length;
                                   col = this.alphabet.indexOf(c) % this.alphabet.length;

                                   charTemp = c;

                                   if (row != (-1) && col != (-1)) {
                                       charTemp = table[row].charAt(col);
                                       key += c;	// add plaintext char to passphrase
                                       passphraseIndex++;
                                       passphraseIndex %= key.length;
                                   }

                                   output += charTemp;
                               }
                           } else {
                               output = input;
                           }

                           return output;
                       },

decodeAutokeyVigenere: function(input, key, table) {
                           var output = '';

                           if (key.length > 0) {
                               var passphraseIndex = 0;	// current iterated passphrase character index

                               var c;		// current iterated message character
                               var k;		// current iterated passphrase character
                               var col;	// col of the message character in the table
                               var row;	// row of the passphrase character in the table

                               for (var i = 0; i < input.length; i++) {
                                   var c = input.charAt(i);
                                   var k = key.charAt(passphraseIndex % key.length); 
                                   var col = this.alphabet.indexOf(k);

                                   if (col != (-1)) {
                                       var row = table[col].indexOf(c);

                                       if (row != (-1)) {
                                           c = this.alphabet.charAt(row);
                                           key += c;
                                           passphraseIndex++;
                                           passphraseIndex %= key.length;
                                       }

                                       output += c;
                                   }
                               }
                           } else {
                               output = input;
                           }

                           return output;
                       },

encodeGronsfeld: function(input, key, table) {
                     var output = '';

                     if (key.length > 0) {
                         var passphraseIndex = 0;	// current iterated passphrase character index

                         var c;	// current iterated input character
                         var k;	// current iterated passphrase character
                         var row;	// row of the passphrase character in the table
                         var col;	// col of the message character in the table
                         var charTemp;	// copy of c

                         for (var i = 0; i < input.length; i++) {
                             c = input.charAt(i);
                             k = key.charAt(passphraseIndex % key.length);

                             row = this.numbers.indexOf(k) % this.numbers.length;
                             col = this.alphabet.indexOf(c) % this.alphabet.length;

                             charTemp = c;

                             if (row != (-1) && col != (-1)) {
                                 charTemp = table[row].charAt(col);
                                 passphraseIndex++;
                                 passphraseIndex %= key.length;
                             }

                             output += charTemp;
                         }
                     } else {
                         output = input;
                     }

                     return output;
                 },

decodeGronsfeld: function(input, key, table) {
                     var output = '';

                     if (key.length > 0) {
                         var passphraseIndex = 0;	// current iterated passphrase character index

                         var c;		// current iterated message character
                         var k;		// current iterated passphrase character
                         var col;	// col of the message character in the table
                         var row;	// row of the passphrase character in the table

                         for (var i = 0; i < input.length; i++) {
                             var c = input.charAt(i);
                             var k = key.charAt(passphraseIndex % key.length); 
                             var col = this.numbers.indexOf(k);

                             if (col != (-1)) {
                                 var row = table[col].indexOf(c);

                                 if (row != (-1)) {
                                     c = this.alphabet.charAt(row);
                                     passphraseIndex++;
                                     passphraseIndex %= key.length;
                                 }

                                 output += c;
                             }
                         }
                     } else {
                         output = input;
                     }

                     return output;
                 }

}


/* courtesy of Lasse Reichstein Nielsen */
/* found on http://www.softwaresecretweapons.com/jspwiki/javascriptstringconcatenation */
function StringBuffer() { 
    this.buffer = []; 
} 

StringBuffer.prototype.append = function append(string) { 
    this.buffer.push(string); 
    return this; 
}; 

StringBuffer.prototype.toString = function toString() { 
    return this.buffer.join(""); 
};

/*var buf = new StringBuffer();

  buf.append("hello");
  buf.append("world");

  alert(buf.toString());

 */
