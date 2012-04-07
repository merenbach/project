/* ciphers.js
 *
 * This script provides facilities for encrypting and decrypting text
 *	within the confines of various ciphers.
 *
 * It is used on Andrew Merenbach's website, http://www.merenbach.com/,
 *   but you are free to use it yourself under a BSD-style license.
 *   Modify it, reuse it, and have fun with it!  If you find any bugs,
 *   please let me know.
 *
 * Copyright (c) 2010 by Andrew Merenbach.  All rights reserved.
 */

var cipherSchemeSelect;
var inputTextArea;
var outputTextArea;	// no cached value
var keywordTextField;
var passphraseTextArea;
var numericKeyTextField;
var alphabetKeyTextField;
var multiplierTextField;
var additiveTextField;
var primerIndexTextField;
var offsetTextField;
var chunkSizeTextField;
var filterCheckBox;
var lowerCaseCheckBox;
var cipherTextAlphabetTextField;
var plainTextAlphabetTextField;

var cachedCipherScheme = null;
var cachedInput = null;
var cachedKeyword = null;
var cachedPassphrase = null;
var cachedNumericKey = null;
var cachedAlphabetKey = null;
var cachedMultiplier = null;
var cachedAdditive = null;
var cachedPrimerIndex = null;
var cachedOffset = null;
var cachedChunkSize = null;
var cachedFilter = null;
var cachedLowercase = null;
var cachedOperation = null;	// no individual field

var OPERATION_OPNULL = (-1);
var OPERATION_ENCODE = 0;
var OPERATION_DECODE = 1;

function triggerCipherCycle() {
	// do initial update
	modifyVisibleCipher();
	window.setTimeout('kickoff()', 100);
}

function prepareFields() {
	cipherSchemeSelect = document.getElementById('scheme');
	inputTextArea = document.getElementById('source');
	outputTextArea = document.getElementById('target');
	keywordTextField = document.getElementById('keyword');
	passphraseTextField = document.getElementById('passphrase');
	numericKeyTextField = document.getElementById('numerickey');
	alphabetKeyTextField = document.getElementById('alphabetkey');
	multiplierTextField = document.getElementById('multiplier');
	additiveTextField = document.getElementById('additive');
	primerIndexTextField = document.getElementById('primerindex');
	offsetTextField = document.getElementById('offset');
	chunkSizeTextField = document.getElementById('chunksize');
	filterCheckBox = document.getElementById('filter');
	lowerCaseCheckBox = document.getElementById('lowercase');
	cipherTextAlphabetTextField = document.getElementById('ciphertextalphabet');
	plainTextAlphabetTextField = document.getElementById('plaintextalphabet');
	// no operation field
}

function parametersChanged() {
	var b1 = (cipherSchemeSelect.value != cachedCipherScheme);
	var b2 = (inputTextArea.value != cachedInput);
	var b3 = (keywordTextField.value != cachedKeyword);
	var b4 = (passphraseTextField.value != cachedPassphrase);
	var b5 = (alphabetKeyTextField.value != cachedAlphabetKey);
	var b6 = (multiplierTextField.value != cachedMultiplier);
	var b7 = (additiveTextField.value != cachedAdditive);
	var b8 = (primerIndexTextField.value != cachedPrimerIndex);
	var b9 = (offsetTextField.value != cachedOffset);
	var b10 = (chunkSizeTextField.value != cachedChunkSize);
	var b11 = (filterCheckBox.checked != cachedFilter);
	var b12 = (lowerCaseCheckBox.checked != cachedLowercase);
	var b13 = (numericKeyTextField.value != cachedNumericKey);
	
	var v = detectRadioValue('operation');
	var b14 = (v != cachedOperation);

	return (b1 || b2 || b3 || b4 || b5 || b6 || b7 || b8 || b9 || b10 || b11 || b12 || b13 || b14);
}

function modifyVisibleCipher() {
	/* not using cached value here, for now;
	 * we may be called before it is configured
	 */
	var identifier = document.getElementById('scheme').value;
	
	var descriptionitem = document.getElementById('descriptionitem');
	
	var introductionitem = document.getElementById('introductionitem');
	var sourcetextitem = document.getElementById('sourcetextitem');
	var targettextitem = document.getElementById('targettextitem');
	var passphraseitem = document.getElementById('passphraseitem');
	var numerickeyitem = document.getElementById('numerickeyitem');
	var keyworditem = document.getElementById('keyworditem');
	var chunksizeitem = document.getElementById('chunksizeitem');
	var plaintextalphabetitem = document.getElementById('plaintextalphabetitem');
	var ciphertextalphabetitem = document.getElementById('ciphertextalphabetitem');
	var primerindexitem = document.getElementById('primerindexitem');
	var alphabetkeyitem = document.getElementById('alphabetkeyitem');
	var cipheroptionsitem = document.getElementById('cipheroptionsitem');
	var cipheroperationsitem = document.getElementById('cipheroperationsitem');
	var offsetitem = document.getElementById('offsetitem');
	var multiplieritem = document.getElementById('multiplieritem');
	var additiveitem = document.getElementById('additiveitem');
	
	var inputfieldset = document.getElementById('inputfieldset');
	var outputfieldset = document.getElementById('outputfieldset');
	
	//var descriptiondivforintro = document.getElementById('descriptionforintro');
	var descriptiondivforintro = document.getElementById('descriptionforintro');
	var descriptiondivforaffine = document.getElementById('descriptionforaffine');
	var descriptiondivforatbash = document.getElementById('descriptionforatbash');
	var descriptiondivforvigenereautokey = document.getElementById('descriptionforvigenereautokey');
	var descriptiondivforvariantautokey = document.getElementById('descriptionforvariantautokey');
	var descriptiondivforbeaufort = document.getElementById('descriptionforbeaufort');
	var descriptiondivforcaesar = document.getElementById('descriptionforcaesar');
	var descriptiondivforcodeword = document.getElementById('descriptionforcodeword');
	var descriptiondivforgronsfeld = document.getElementById('descriptionforgronsfeld');
	var descriptiondivforvariant = document.getElementById('descriptionforvariant');
	var descriptiondivforvigenere = document.getElementById('descriptionforvigenere');
	
	//var fieldsetArray = new Array();		// all fieldsets
	//var itemArray = new Array();			// all items
	var visibleFieldsetArray = new Array();	// fieldsets to remain visible
	var visibleItemArray = new Array();		// items to remain visible
	var invisibleItemArray = new Array();
	var invisibleFieldsetArray = new Array();
	
	/*fieldsetArray.push(inputfieldset);
	fieldsetArray.push(outputfieldset);
	
	//itemArray.push(introductionitem);
	itemArray.push(sourcetextitem);
	itemArray.push(targettextitem);
	itemArray.push(passphraseitem);
	itemArray.push(numerickeyitem);
	itemArray.push(keyworditem);
	itemArray.push(chunksizeitem);
	itemArray.push(plaintextalphabetitem);
	itemArray.push(ciphertextalphabetitem);
	itemArray.push(primerindexitem);
	itemArray.push(alphabetkeyitem);
	itemArray.push(cipheroptionsitem);
	itemArray.push(cipheroperationsitem);
	itemArray.push(offsetitem);
	itemArray.push(multiplieritem);
	itemArray.push(additiveitem);
	
	itemArray.push(descriptiondivforaffine);
	itemArray.push(descriptiondivforatbash);
	itemArray.push(descriptiondivforbeaufort);
	itemArray.push(descriptiondivforcaesar);
	itemArray.push(descriptiondivforcodeword);
	itemArray.push(descriptiondivforvariant);
	itemArray.push(descriptiondivforvariantautokey);
	itemArray.push(descriptiondivforvigenere);
	itemArray.push(descriptiondivforvigenereautokey);
	itemArray.push(descriptiondivforgronsfeld);*/
	
	var descriptionItemArray = new Array();
	descriptionItemArray.push(descriptiondivforintro);
	descriptionItemArray.push(descriptiondivforaffine);
	descriptionItemArray.push(descriptiondivforatbash);
	descriptionItemArray.push(descriptiondivforvigenereautokey);
	descriptionItemArray.push(descriptiondivforvariantautokey);
	descriptionItemArray.push(descriptiondivforbeaufort);
	descriptionItemArray.push(descriptiondivforcaesar);
	descriptionItemArray.push(descriptiondivforcodeword);
	descriptionItemArray.push(descriptiondivforgronsfeld);
	descriptionItemArray.push(descriptiondivforvariant);
	descriptionItemArray.push(descriptiondivforvigenere);
	
	var visibleDescriptionItem = null;
	
	switch(identifier) {
		case 'intro':
			invisibleFieldsetArray.push(inputfieldset);
			invisibleFieldsetArray.push(outputfieldset);
			visibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			invisibleItemArray.push(sourcetextitem);
			invisibleItemArray.push(targettextitem);
			invisibleItemArray.push(chunksizeitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);
			invisibleItemArray.push(cipheroptionsitem);
			invisibleItemArray.push(cipheroperationsitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(passphraseitem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(primerindexitem);
			invisibleItemArray.push(alphabetkeyitem);
			
			visibleDescriptionItem = descriptiondivforintro;
			
			break;
			
		case 'affine':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(plaintextalphabetitem);
			visibleItemArray.push(ciphertextalphabetitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			visibleItemArray.push(multiplieritem);
			visibleItemArray.push(additiveitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(passphraseitem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(primerindexitem);
			invisibleItemArray.push(alphabetkeyitem);

			visibleDescriptionItem = descriptiondivforaffine;
			
			break;
		
		case 'atbash':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(plaintextalphabetitem);
			visibleItemArray.push(ciphertextalphabetitem);
			visibleItemArray.push(cipheroptionsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(passphraseitem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(primerindexitem);
			invisibleItemArray.push(alphabetkeyitem);
			invisibleItemArray.push(cipheroperationsitem);

			visibleDescriptionItem = descriptiondivforatbash;
			
			break;
						
		case 'beaufort':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);
			invisibleItemArray.push(cipheroperationsitem);

			visibleDescriptionItem = descriptiondivforbeaufort;

			break;

		case 'beaufortx':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);
			invisibleItemArray.push(cipheroperationsitem);

			visibleDescriptionItem = descriptiondivforbeaufort;

			break;

		case 'beaufortautokey':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);
			invisibleItemArray.push(cipheroperationsitem);

			visibleDescriptionItem = descriptiondivforbeaufort;

			break;

		case 'caesar':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(plaintextalphabetitem);
			visibleItemArray.push(ciphertextalphabetitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			visibleItemArray.push(offsetitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(passphraseitem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(primerindexitem);
			invisibleItemArray.push(alphabetkeyitem);
			
			visibleDescriptionItem = descriptiondivforcaesar;
			
			break;
			
		case 'codeword':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(plaintextalphabetitem);
			visibleItemArray.push(ciphertextalphabetitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			visibleItemArray.push(keyworditem);
			
			invisibleItemArray.push(passphraseitem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(primerindexitem);
			invisibleItemArray.push(alphabetkeyitem);
			
			visibleDescriptionItem = descriptiondivforcodeword;
			
			break;
		
		case 'gronsfeld':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);

			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(numerickeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);

			invisibleItemArray.push(alphabetkeyitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(passphraseitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(primerindexitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforgronsfeld;
						
			break;
			
		case 'variant':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvariant;
			
			break;
			
		case 'variantx':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvariant;
			
			break;
		
		case 'variantautokey':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);

			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvariantautokey;
			
			break;
			
		case 'variantautokeyx':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);

			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvariantautokey;
			
			break;

		case 'vigenere':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvigenere;

			break;
			
		case 'vigenerex':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvigenereautokey;

			break;
			
		case 'vigenereautokey':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvigenereautokey;

			break;
			
		case 'vigenereautokeyx':
			visibleFieldsetArray.push(inputfieldset);
			visibleFieldsetArray.push(outputfieldset);
			invisibleItemArray.push(introductionitem);
			
			visibleItemArray.push(descriptionitem);
			visibleItemArray.push(sourcetextitem);
			visibleItemArray.push(targettextitem);
			visibleItemArray.push(passphraseitem);
			visibleItemArray.push(chunksizeitem);
			visibleItemArray.push(primerindexitem);
			visibleItemArray.push(alphabetkeyitem);
			visibleItemArray.push(cipheroptionsitem);
			visibleItemArray.push(cipheroperationsitem);
			
			invisibleItemArray.push(keyworditem);
			invisibleItemArray.push(numerickeyitem);
			invisibleItemArray.push(offsetitem);
			invisibleItemArray.push(multiplieritem);
			invisibleItemArray.push(additiveitem);
			invisibleItemArray.push(plaintextalphabetitem);
			invisibleItemArray.push(ciphertextalphabetitem);

			visibleDescriptionItem = descriptiondivforvigenereautokey;

			break;
			
		default: break;
	}
	
	// hide all fieldsets
	for (var i = 0; i < invisibleFieldsetArray.length; i++) {
		//fieldsetArray[i].style.display = 'none';			// invisible
		$("#" + invisibleFieldsetArray[i].id).fadeOut();
	}

	// display relevant fieldsets
	for (var i = 0; i < visibleFieldsetArray.length; i++) {
		//visibleFieldsetArray[i].style.display = 'block';	// visible
		$("#" + visibleFieldsetArray[i].id).fadeIn();
	}
	
	// hide all items
	for (var i = 0; i < invisibleItemArray.length; i++) {
		//itemArray[i].style.display = 'none';				// invisible
		$("#" + invisibleItemArray[i].id).fadeOut();
	}
	
	// show relevant items
	for (var i = 0; i < visibleItemArray.length; i++) {
		//visibleItemArray[i].style.display = 'block';		// visible
		$("#" + visibleItemArray[i].id).fadeIn();
	}
	
	// show or hide relevant descriptions
	for (var i = 0; i < descriptionItemArray.length; i++) {
		if (descriptionItemArray[i] != visibleDescriptionItem) {
			$("#" + descriptionItemArray[i].id).fadeOut();
		} else {
			$("#" + descriptionItemArray[i].id).fadeIn();
		}
	}
	
	if (visibleDescriptionItem == null) {
		$("#" + descriptionitem.id).fadeOut();
	}
	
	/*var visibleToChange = new Array();
	
	for (var i = 0; i < fieldsetArray.length; i++) {
		var latest = null;
		for (var j = 0; j < visibleFieldsetArray.length; j++) {
			if (visibleFieldsetArray[j] == fieldsetArray[i]) {
				latest = fieldsetArray[i];
				break;
			}
		}
		if (latest != null) {
			
		}
	}*/
}

function updateParameterCache() {
	cachedCipherScheme = cipherSchemeSelect.value;
	cachedInput = inputTextArea.value;
	cachedKeyword = keywordTextField.value;
	cachedPassphrase = passphraseTextField.value;
	cachedNumericKey = numericKeyTextField.value;
	cachedAlphabetKey = alphabetKeyTextField.value;
	cachedMultiplier = multiplierTextField.value;
	cachedAdditive = additiveTextField.value;
	cachedPrimerIndex = primerIndexTextField.value;
	cachedOffset = offsetTextField.value;
	cachedChunkSize = chunkSizeTextField.value;

	/* the cache filter checkbox determines whether chunking is enabled */
	newCachedFilter = filterCheckBox.checked;
	if (newCachedFilter != cachedFilter && newCachedFilter == false) {
		chunkSizeTextField.blur();
		chunkSizeTextField.disabled = true;
	} else if (newCachedFilter != cachedFilter && newCachedFilter == true) {
		chunkSizeTextField.blur();
		chunkSizeTextField.disabled = false;
	}
	cachedFilter = newCachedFilter;
	
	cachedLowercase = lowerCaseCheckBox.checked;
	cachedOperation = detectRadioValue('operation');
}

/* create a transcoder object; configure its
 * instance variables; and transcode with it
 */
function kickoff() {
	// get things ready as process begins
	prepareFields();
		
	if (parametersChanged()) {
		updateParameterCache();
		
		// update cipher, then determine what operation to perform
		modifyVisibleCipher();
				
		switch(cipherSchemeSelect.value) {
			case 'affine':
				// create and configure our transcoder
				var tc = new transcoderForAffine();
				tc.alphabet = AMCipherUtilities.canonicalAlphabet;
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.multiplier = multiplierTextField.value;
				tc.additive = additiveTextField.value;

				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// generate alphabets
				tc.generateAlphabets();
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;
				
				var canonicalAlphabets = tc.alphabetArray;
				plainTextAlphabetTextField.value = canonicalAlphabets[0];
				cipherTextAlphabetTextField.value = canonicalAlphabets[1];
				break;
			
			case 'atbash':
				// create and configure our transcoder
				var tc = new transcoderForAtbash();
				tc.alphabet = AMCipherUtilities.canonicalAlphabet;
				tc.source = inputTextArea.value;
				tc.target = '';
				
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// generate alphabets
				tc.generateAlphabets();
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;
				
				var canonicalAlphabets = tc.alphabetArray;
				plainTextAlphabetTextField.value = canonicalAlphabets[0];
				cipherTextAlphabetTextField.value = canonicalAlphabets[1];
				
				break;
										
			case 'beaufort':
				// create and configure our transcoder
				var tc = new transcoderForBeaufort();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
					
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
				
			case 'beaufortx':
				// create and configure our transcoder
				var tc = new transcoderForBeaufortExtended();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.standardNumbers = AMCipherUtilities.canonicalNumbers;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
					
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;

			/*case 'beaufortautokey':
				// create and configure our transcoder
				var tc = new transcoderForAutokeyBeaufort();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
					
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;*/

			case 'caesar':
				// create and configure our transcoder
				var tc = new transcoderForCaesar();
				tc.alphabet = AMCipherUtilities.canonicalAlphabet;
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.offset = offsetTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// generate alphabets
				tc.generateAlphabets();
			
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				var canonicalAlphabets = tc.alphabetArray;
				plainTextAlphabetTextField.value = canonicalAlphabets[0];
				cipherTextAlphabetTextField.value = canonicalAlphabets[1];
				break;
				
			case 'codeword':
				// create and configure our transcoder
				var tc = new transcoderForCodeword();
				tc.alphabet = AMCipherUtilities.canonicalAlphabet;
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.keyword = keywordTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// generate alphabets
				tc.generateAlphabets();
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;
				
				var canonicalAlphabets = tc.alphabetArray;
				plainTextAlphabetTextField.value = canonicalAlphabets[0];
				cipherTextAlphabetTextField.value = canonicalAlphabets[1];

				break;
				
			case 'gronsfeld':
				// create and configure our transcoder
				var tc = new transcoderForGronsfeld();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.numerickey = numericKeyTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
			
			case 'variant':
				// create and configure our transcoder
				var tc = new transcoderForVariantBeaufort();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
						
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
			
			case 'variantx':
				// create and configure our transcoder
				var tc = new transcoderForVariantBeaufortExtended();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.standardNumbers = AMCipherUtilities.canonicalNumbers;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
						
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
				
			case 'variantautokey':
				// create and configure our transcoder
				var tc = new transcoderForAutokeyVariantBeaufort();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
					
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;
				
				break;

			case 'variantautokeyx':
				// create and configure our transcoder
				var tc = new transcoderForAutokeyVariantBeaufortExtended();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.standardNumbers = AMCipherUtilities.canonicalNumbers;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
					
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;
				
				break;


			case 'vigenere':
				// create and configure our transcoder
				var tc = new transcoderForVigenere();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
				
			case 'vigenereautokey':
				// create and configure our transcoder
				var tc = new transcoderForAutokeyVigenere();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;
				
				break;
				
			case 'vigenereautokeyx':
				// create and configure our transcoder
				var tc = new transcoderForAutokeyVigenereExtended();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.standardNumbers = AMCipherUtilities.canonicalNumbers;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
				
			case 'vigenerex':
				// create and configure our transcoder
				var tc = new transcoderForVigenereExtended();
				tc.alphabetKey = alphabetKeyTextField.value;
				tc.standardAlphabet = AMCipherUtilities.canonicalAlphabet;
				tc.standardNumbers = AMCipherUtilities.canonicalNumbers;
				tc.generateAlphabet();
				tc.source = inputTextArea.value;
				tc.target = '';
				tc.passphrase = passphraseTextField.value;
				tc.primerIndex = primerIndexTextField.value;
				
				// determine the operation
				var transcodeOperation = detectRadioValue('operation');
				switch(transcodeOperation) {
					case 'encode': tc.operation = OPERATION_ENCODE; break;
					case 'decode': tc.operation = OPERATION_DECODE; break;
					default: tc.operation = OPERATION_OPNULL; break;
				}
			
				// finish configuration
				tc.chunkSize = chunkSizeTextField.value;
				tc.filter = filterCheckBox.checked;
				tc.lowercase = lowerCaseCheckBox.checked;
				
				// transcode the text and display the result
				tc.process();
				outputTextArea.value = tc.target;

				break;
			
			default: break;
		}
	}
	
	window.setTimeout('kickoff()', 100);
}

/* end test code */

/* for Beaufort */
function transcoderForBeaufort() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
		var primerIndex = this.primerIndex;
		var filter = this.filter;
		var operation = this.operation;
		var chunkSize = this.chunkSize;
		
		// should we filter the input?
		if (this.filter == true) {
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transcode the input
		output = this.transcode(input, passphrase, primerIndex);
		
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
	
	this.transcode = function(input, passphrase, primerIndex) {
		var output = '';
		
		// transform, filter, and constrain
		input = input.toUpperCase();
		passphrase = passphrase.toUpperCase();
		passphrase = filterString(passphrase);
		// do not use uniqueString() on passphrase here
		primerIndex = filterNumber(primerIndex);
		primerIndex %= this.alphabet.length;

		if (passphrase.length > 0) {
			var table = AMCipherUtilities.generateTabulaRecta(this.alphabet, primerIndex);
			
			//output = this.transcodeOperation(passphrase, message, table);
					
			var c;			// current iterated input character
			var k;			// current iterated passphrase character
			var row;		// row of the passphrase character in the table
			var col;		// col of the message character in the table
			var passphraseIndex = 0;	// current iterated passphrase character index
			var charTemp;	// copy of c

			for (var i = 0; i < input.length; i++) {
				c = input.charAt(i);
				k = passphrase.charAt(passphraseIndex);
				col = this.alphabet.indexOf(c);	// position of input char in alphabet
				charTemp = c;
				
				if (col != (-1)) {
					row = table[col].indexOf(k);
					if (row != (-1)) {
						charTemp = this.alphabet.charAt(row);
						passphraseIndex++;
						passphraseIndex %= passphrase.length;
					}
				}
				output += charTemp;
			}
		} else {
			output = input;
		}
		
		return output;
	}
	
	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
	}
}

// experimental?
/*function transcoderForAutokeyBeaufort() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
		var primerIndex = this.primerIndex;
		var filter = this.filter;
		var operation = this.operation;
		var chunkSize = this.chunkSize;
		
		// should we filter the input?
		if (this.filter == true) {
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transcode the input
		output = this.transcode(input, passphrase, primerIndex);
		
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
	
	this.transcode = function(input, passphrase, primerIndex) {
		var output = '';
		
		// transform, filter, and constrain
		input = input.toUpperCase();
		passphrase = passphrase.toUpperCase();
		passphrase = filterString(passphrase);
		// do not use uniqueString() on passphrase here
		primerIndex = filterNumber(primerIndex);
		primerIndex %= this.alphabet.length;

		if (passphrase.length > 0) {
			var table = AMCipherUtilities.generateTabulaRecta(this.alphabet, primerIndex);
			
			//output = this.transcodeOperation(passphrase, message, table);
					
			var c;			// current iterated input character
			var k;			// current iterated passphrase character
			var row;		// row of the passphrase character in the table
			var col;		// col of the message character in the table
			var passphraseIndex = 0;	// current iterated passphrase character index
			var charTemp;	// copy of c

			for (var i = 0; i < input.length; i++) {
				c = input.charAt(i);
				k = passphrase.charAt(passphraseIndex);
				col = this.alphabet.indexOf(c);	// position of input char in alphabet
				charTemp = c;
				
				if (col != (-1)) {
					row = table[col].indexOf(k);
					if (row != (-1)) {
						charTemp = this.alphabet.charAt(row);
						passphraseIndex++;
						passphraseIndex %= passphrase.length;
					}
				}
				output += charTemp;
			}
		} else {
			output = input;
		}
		
		return output;
	}
	
	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
	}
}*/

function transcoderForBeaufortExtended() {
	this.standardAlphabet = '';
	this.standardNumbers = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
		var primerIndex = this.primerIndex;
		var filter = this.filter;
		var operation = this.operation;
		var chunkSize = this.chunkSize;
		
		// should we filter the input?
		if (this.filter == true) {
			input = filterAlphanumeric(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transcode the input
		output = this.transcode(input, passphrase, primerIndex);
		
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
	
	this.transcode = function(input, passphrase, primerIndex) {
		var output = '';
		
		// transform, filter, and constrain
		input = input.toUpperCase();
		passphrase = passphrase.toUpperCase();
		passphrase = filterAlphanumeric(passphrase);
		
		// do not use uniqueString() on passphrase here
		primerIndex = filterNumber(primerIndex);
		primerIndex %= this.alphabet.length;

		if (passphrase.length > 0) {
			var table = AMCipherUtilities.generateTabulaRectaExtended(this.alphabet, primerIndex);
			
			//output = this.transcodeOperation(passphrase, message, table);
					
			var c;			// current iterated input character
			var k;			// current iterated passphrase character
			var row;		// row of the passphrase character in the table
			var col;		// col of the message character in the table
			var passphraseIndex = 0;	// current iterated passphrase character index
			var charTemp;	// copy of c

			for (var i = 0; i < input.length; i++) {
				c = input.charAt(i);
				k = passphrase.charAt(passphraseIndex);
				col = this.alphabet.indexOf(c);	// position of input char in alphabet
				charTemp = c;
				
				if (col != (-1)) {
					row = table[col].indexOf(k);
					if (row != (-1)) {
						charTemp = this.alphabet.charAt(row);
						passphraseIndex++;
						passphraseIndex %= passphrase.length;
					}
				}
				output += charTemp;
			}
		} else {
			output = input;
		}
		
		return output;
	}
	
	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.standardNumbers, this.alphabetKey);
	}
}

/*function transcoderForAutokeyBeaufortExtended() {
	this.standardAlphabet = '';
	this.standardNumbers = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
		var primerIndex = this.primerIndex;
		var filter = this.filter;
		var operation = this.operation;
		var chunkSize = this.chunkSize;
		
		// should we filter the input?
		if (this.filter == true) {
			input = filterAlphanumeric(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transcode the input
		output = this.transcode(input, passphrase, primerIndex);
		
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
	
	this.transcode = function(input, passphrase, primerIndex, isDecoding) {
		var output = '';
		
		// transform, filter, and constrain
		input = input.toUpperCase();
		passphrase = passphrase.toUpperCase();
		passphrase = filterAlphanumeric(passphrase);
		
		// do not use uniqueString() on passphrase here
		primerIndex = filterNumber(primerIndex);
		primerIndex %= this.alphabet.length;

		if (passphrase.length > 0) {
			var table = AMCipherUtilities.generateTabulaRectaExtended(this.alphabet, primerIndex);
			
			//output = this.transcodeOperation(passphrase, message, table);
					
			var c;			// current iterated input character
			var k;			// current iterated passphrase character
			var row;		// row of the passphrase character in the table
			var col;		// col of the message character in the table
			var passphraseIndex = 0;	// current iterated passphrase character index
			var charTemp;	// copy of c

			for (var i = 0; i < input.length; i++) {
				c = input.charAt(i);
				k = passphrase.charAt(passphraseIndex);
				col = this.alphabet.indexOf(c);	// position of input char in alphabet
				charTemp = c;
				
				if (col != (-1)) {
					row = table[col].indexOf(k);
					if (row != (-1)) {
						if (!isDecoding) {
							passphrase += c;
						}
						charTemp = this.alphabet.charAt(row);
						if (isDecoding) {
							passphrase += charTemp;
						}
						passphraseIndex++;
						passphraseIndex %= passphrase.length;
					}
				}
				output += charTemp;
			}
		} else {
			output = input;
		}
		
		return output;
	}
	
	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.standardNumbers, this.alphabetKey);
	}
}*/

/* for Variant Beaufort */
function transcoderForVariantBeaufort() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transform parameters
		input = input.toUpperCase();
		
		// filter and constrain
		passphrase = passphrase.toUpperCase();
		passphrase = filterString(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRecta(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.decodeVigenere;
	this.decode = AMCipherUtilities.encodeVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
	}
}

/* for Vigenere */

function transcoderForVigenere() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transform parameters
		input = input.toUpperCase();
		
		// filter and constrain
		passphrase = passphrase.toUpperCase();
		passphrase = filterString(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRecta(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.encodeVigenere;
	this.decode = AMCipherUtilities.decodeVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
	}
}

function transcoderForVigenereExtended() {
	this.standardAlphabet = '';
	this.standardNumbers = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
		passphrase = passphrase.toUpperCase();
		passphrase = filterAlphanumeric(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRectaExtended(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.encodeVigenere;
	this.decode = AMCipherUtilities.decodeVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.standardNumbers, this.alphabetKey);
	}
}

function transcoderForAutokeyVigenereExtended() {
	this.standardAlphabet = '';
	this.standardNumbers = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
		passphrase = passphrase.toUpperCase();
		passphrase = filterAlphanumeric(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRectaExtended(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.encodeAutokeyVigenere;
	this.decode = AMCipherUtilities.decodeAutokeyVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.standardNumbers, this.alphabetKey);
	}
}

function transcoderForVariantBeaufortExtended() {
	this.standardAlphabet = '';
	this.standardNumbers = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
		passphrase = passphrase.toUpperCase();
		passphrase = filterAlphanumeric(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRectaExtended(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.decodeVigenere;
	this.decode = AMCipherUtilities.encodeVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.standardNumbers, this.alphabetKey);
	}
}

function transcoderForAutokeyVariantBeaufortExtended() {
	this.standardAlphabet = '';
	this.standardNumbers = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
		passphrase = passphrase.toUpperCase();
		passphrase = filterAlphanumeric(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRectaExtended(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.decodeAutokeyVigenere;
	this.decode = AMCipherUtilities.encodeAutokeyVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabetWithNumbers(this.standardAlphabet, this.standardNumbers, this.alphabetKey);
	}
}

/*function encodeVariantBeaufort(input, key, table) {
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
				}
			
				output += c;
			}
		}
	} else {
		output = input;
	}
	
	return output;
}

function decodeVariantBeaufort(input, key, table) {
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
			}
			
			output += charTemp;
		}
	} else {
		output = input;
	}

	return output;
}*/

/* Atbash */
function transcoderForAtbash() {
	this.alphabet = '';
	this.source = '';
	this.target = '';
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.alphabetArray = null;
	this.chunkSize = null;
	
	this.process = function() {
		this.target = AMCipherUtilities.monoalphabeticTranscode(this.source, this.alphabetArray, this.filter, this.lowercase, this.chunkSize);
	}
	
	this.generateAlphabets = function() {
		var alphabets = new Array(2);
		
		var alphabet = this.alphabet;
		
		if (alphabet.length > 0) {
			var alphabet = this.alphabet;
			
			alphabet = alphabet.toUpperCase();
			alphabet = filterString(alphabet);
			alphabet = uniqueString(alphabet);
			
			alphabets[0] = alphabet;
			alphabets[1] = reverseString(alphabet);
		} else {
			alphabets[0] = '';
			alphabets[1] = '';
		}
		
		this.alphabetArray = alphabets;
	}
}

/* Caesar shift */

function transcoderForCaesar() {
	this.alphabet = '';
	this.source = '';
	this.target = '';
	this.offset = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.alphabetArray = null;
	this.chunkSize = null;
	
	this.process = function() {
		this.target = AMCipherUtilities.monoalphabeticTranscode(this.source, this.alphabetArray, this.filter, this.lowercase, this.chunkSize);
	}
	
	this.generateAlphabets = function() {
		var alphabets;
	
		switch(this.operation) {
			case OPERATION_ENCODE:
				alphabets = AMCipherUtilities.caesarAlphabetsForEncryption(this.alphabet, this.offset);
				break;
			case OPERATION_DECODE:
				alphabets = AMCipherUtilities.caesarAlphabetsForDecryption(this.alphabet, this.offset);
				break;
			default:
				alphabets = new Array(2);
				alphabets[0] = this.alphabet;
				alphabets[1] = this.alphabet;
				break;
		}
		
		this.alphabetArray = alphabets;
	}
}

/* codeword */

function transcoderForCodeword() {
	this.alphabet = '';
	this.source = '';
	this.target = '';
	this.keyword = '';
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.alphabetArray = null;
	this.chunkSize = null;
	
	this.process = function() {
		this.target = AMCipherUtilities.monoalphabeticTranscode(this.source, this.alphabetArray, this.filter, this.lowercase, this.chunkSize);
	}
	
	this.generateAlphabets = function() {
		var alphabets;
		
		switch(this.operation) {
			case OPERATION_ENCODE:
				alphabets = AMCipherUtilities.codewordAlphabetsForEncryption(this.alphabet, this.keyword);
				break;
			case OPERATION_DECODE:
				alphabets = AMCipherUtilities.codewordAlphabetsForDecryption(this.alphabet, this.keyword);
				break;
			default:
				alphabets = new Array(2);
				alphabets[0] = this.alphabet;
				alphabets[1] = this.alphabet;
				break;
		}
		
		this.alphabetArray = alphabets;
	}
}

/* affine */
function transcoderForAffine() {
	this.alphabet = '';
	this.source = '';
	this.target = '';
	this.additive = 0;
	this.multiplier = 1;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.alphabetArray = null;
	this.chunkSize = null;
	
	this.process = function() {
		this.target = AMCipherUtilities.monoalphabeticTranscode(this.source, this.alphabetArray, this.filter, this.lowercase, this.chunkSize);
	}
	
	this.generateAlphabets = function() {
		var alphabets;
		
		switch(this.operation) {
			case OPERATION_ENCODE:
				alphabets = AMCipherUtilities.affineAlphabetsForEncryption(this.alphabet, this.multiplier, this.additive);
				break;
			case OPERATION_DECODE:
				alphabets = AMCipherUtilities.affineAlphabetsForDecryption(this.alphabet, this.multiplier, this.additive);
				break;
			default:
				alphabets = new Array(2);
				alphabets[0] = this.alphabet;
				alphabets[1] = this.alphabet;
				break;
		}
		
		this.alphabetArray = alphabets;
	}
}

function transcoderForAutokeyVariantBeaufort() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transform parameters
		input = input.toUpperCase();
		
		// filter and constrain
		passphrase = passphrase.toUpperCase();
		passphrase = filterString(passphrase);
		
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRecta(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.decodeAutokeyVigenere;
	this.decode = AMCipherUtilities.encodeAutokeyVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
	}
}

function transcoderForAutokeyVigenere() {
	this.standardAlphabet = '';
	this.alphabet = '';
	this.alphabetKey = '';
	this.source = '';
	this.target = '';
	this.passphrase = '';
	this.primerIndex = 0;
	this.filter = false;
	this.lowercase = false;
	this.operation = OPERATION_OPNULL;
	this.chunkSize = null;
	
	this.process = function() {
		var input = this.source;
		var output = this.target;
		var passphrase = this.passphrase;
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
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transform parameters
		input = input.toUpperCase();
		
		// filter and constrain
		passphrase = passphrase.toUpperCase();
		passphrase = filterString(passphrase);
		
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaRecta(this.alphabet, primerIndex);

		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, passphrase, table); break;
			case OPERATION_DECODE: output = this.decode(input, passphrase, table); break;
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
	
	this.encode = AMCipherUtilities.encodeAutokeyVigenere;
	this.decode = AMCipherUtilities.decodeAutokeyVigenere;

	this.generateAlphabet = function() {
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
	}
}

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
		var passphrase = this.passphrase;
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
			input = filterString(input);
			if (chunkSize > 0) {
				input = padString(input, chunkSize, AMCipherUtilities.paddingCharacter);
			}
		}
		
		// transform parameters
		input = input.toUpperCase();
		
		var numerickey = this.numerickey;
		
		// filter and constrain
		numerickey = filterNumber(numerickey);
		
		//passphrase = passphrase.toUpperCase();
		//passphrase = filterString(passphrase);
		// do not use uniqueString() on passphrase here
		
		// genereate the table
		var table = AMCipherUtilities.generateTabulaGronsfeld(this.alphabet, this.numbers, primerIndex);
		
		// transcode the input
		switch(operation) {
			case OPERATION_ENCODE: output = this.encode(input, numerickey, table); break;
			case OPERATION_DECODE: output = this.decode(input, numerickey, table); break;
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
		this.alphabet = AMCipherUtilities.simpleCodewordAlphabet(this.standardAlphabet, this.alphabetKey);
		this.numbers = '0123456789';
	}
}

/*function codewordAlphabetsForDecryption(alphabet, keyword) {
	var alphabets = new Array(2);
	
	if (keyword.length > 0) {
		alphabet = alphabet.toUpperCase();
		alphabet = filterString(alphabet);
		alphabet = uniqueString(alphabet);
	
		keyword = keyword.toUpperCase();	// convert keyword to upper-case
		keyword = filterString(keyword);	// filter disallowed characters
		keyword = uniqueString(keyword);	// remove duplicate characters
		
		var ab = '';
		
		if (keyword != alphabet) {
			//alphabet_copy =~ s/[\Q$ab\E]//gs;
			ab = keyword;
			var re = new RegExp("[" + ab + "]", "g");
			var alphabetTrimmed = alphabet.replace(re, '');
			ab += alphabetTrimmed;
			
			var temp = '';
			
			for (var i = 0; i < ab.length; i++) {
				var c = alphabet.charAt(i);
				var j = ab.indexOf(c);
				var c2 = alphabet.charAt(j);
				
				temp += c2;
			}
			
			ab = temp;
			
		} else {
			ab = alphabet;
		}
	
		alphabets[0] = alphabet;
		alphabets[1] = ab;
	} else {
		alphabets[0] = alphabet;
		alphabets[1] = alphabet;
	}
	
	return alphabets;
}*/

/*function isLowerCase(char) {
	var re = /[:lower:]/;
	return re.test(char);
}*/

/*function isUpperCase(char) {
	var re = /[:upper:]/;
	return re.test(char);
}*/
