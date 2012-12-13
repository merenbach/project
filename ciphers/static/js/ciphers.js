(function($, Dajax, Dajaxice, document, window) {
	"use strict";
	var $field_source     = $('.field-source');
	var $field_target     = $('.field-target');
	var $field_lowercase  = $('.field-lowercase');
	var $field_filter     = $('.field-filter');
	var $field_chunk      = $('.field-chunk');
	var $field_multiplier = $('.field-multiplier');
	var $field_additive   = $('.field-additive');
	var $field_shift      = $('.field-shift');
	var $field_keyword    = $('.field-keyword');
	var $field_passphrase = $('.field-passphrase');
	var $field_primer     = $('.field-primer');
	var $field_digits     = $('.field-digits');
	// var $radio_operation  = $('input:radio[name=operation]:checked');
	var $radio_autoclave  = $('input:radio[name=autoclave]');

	function transcode_message($pane, transcode_callback) {
		var message = $pane.find($field_source).val();
		if (typeof(message) === 'string' && message !== '') {
			var message_args = {};
			message_args.message = message;
			message_args.should_filter = $pane.find($field_filter).is(':checked') ? true : false;
			message_args.lower = $pane.find($field_lowercase).is(':checked') ? true : false;
			message_args.chunk = parseInt($pane.find($field_chunk).val(), 10);
			var $field;

			try {
				message_args.multiplier = $pane.find($field_multiplier).val();
			} finally {}
			
			try {
				message_args.additive = $pane.find($field_additive).val();
			} finally {}
			
			try {
				message_args.shift = $pane.find($field_shift).val();
			} finally {}
			
			try {
				message_args.keyword = $pane.find($field_keyword).val();
			} finally {}
			
			try {
				message_args.passphrase = $pane.find($field_passphrase).val();
			} finally{}
			
			try {
				message_args.primer = $pane.find($field_primer).val();
			} finally{}
			
			try {
				$field = $pane.find($field_digits);
				if ($field.length) {
					message_args.use_digits = $field.is(':checked') ? true : false;
				}
			} finally{}
			
			// try {
			//     $field = $pane.find($radio_operation);
			//     if ($field.length) {
			//         message_args.operation = ($field.val() === 'encode') ? true : false;
			//     }
			// } finally{}
			
			try {
				$field = $pane.find($radio_autoclave).filter(':checked');
				if ($field.length) {
					message_args.autoclave = ($field.val() === 'text') ? true : false;
				}
			} finally{}

			$pane.find($field_target).val('');
			// $pane.find($field_target).val('Processing...');
			transcode_callback(Dajax.process, message_args);
		}
	}

	function encode_affine() {
		var $pane = $('#affine_pane');
		transcode_message($pane, Dajaxice.ciphers.encode_affine);
	}
	
	function decode_affine() {
		var $pane = $('#affine_pane');
		transcode_message($pane, Dajaxice.ciphers.decode_affine);
	}

	function transcode_atbash() {
		var $pane = $('#atbash_pane');
		transcode_message($pane, Dajaxice.ciphers.transcode_atbash);
	}

	function transcode_beaufort() {
		var $pane = $('#beaufort_pane');
		transcode_message($pane, Dajaxice.ciphers.transcode_beaufort);
	}

	function encode_caesar() {
		var $pane = $('#caesar_pane');
		transcode_message($pane, Dajaxice.ciphers.encode_caesar);
	}
	
	function decode_caesar() {
		var $pane = $('#caesar_pane');
		transcode_message($pane, Dajaxice.ciphers.decode_caesar);
	}

	function encode_codeword() {
		var $pane = $('#codeword_pane');
		transcode_message($pane, Dajaxice.ciphers.encode_codeword);
	}
	
	function decode_codeword() {
		var $pane = $('#codeword_pane');
		transcode_message($pane, Dajaxice.ciphers.decode_codeword);
	}

	function encode_vigenere() {
		var $pane = $('#vigenere_pane');
		transcode_message($pane, Dajaxice.ciphers.encode_vigenere);
	}

	function decode_vigenere() {
		var $pane = $('#vigenere_pane');
		transcode_message($pane, Dajaxice.ciphers.decode_vigenere);
	}

	$(document).ready(function() {
		$('.pane').hide();
		$('#cipher_input_panes').show();

		$('#scheme').change(function() {
			var el_id = $(this).val();
			$('.pane').hide();
			$('#' + el_id + '_pane').show();
		});

		$('#affine_pane .button-encode').click(encode_affine);
		$('#affine_pane .button-decode').click(decode_affine);
		$('#atbash_pane .button-transcode').click(transcode_atbash);
		$('#caesar_pane .button-encode').click(encode_caesar);
		$('#caesar_pane .button-decode').click(decode_caesar);
		$('#beaufort_pane .button-transcode').click(transcode_beaufort);
		$('#codeword_pane .button-encode').click(encode_codeword);
		$('#codeword_pane .button-decode').click(decode_codeword);
		$('#vigenere_pane .button-encode').click(encode_vigenere);
		$('#vigenere_pane .button-decode').click(decode_vigenere);

		$('#intro_pane').show();
		window.onbeforeunload = function() {};
	});
})(jQuery, Dajax, Dajaxice, document, window);