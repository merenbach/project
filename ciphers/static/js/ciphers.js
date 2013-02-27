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

	function transcode_message(pane_name, transcode_callback) {
        var $pane = $(pane_name);
		var message = $pane.find($field_source).val();
		if (typeof(message) === 'string' && message !== '') {
			var message_args = {};
            message_args.container = pane_name;
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

	$(document).ready(function() {
		$('#affine .button-encode').on('click', function() {
            transcode_message('#affine', Dajaxice.ciphers.encode_affine);
        });
		$('#affine .button-decode').on('click', function() {
            transcode_message('#affine', Dajaxice.ciphers.decode_affine);
        });
		$('#atbash .button-transcode').on('click', function() {
            transcode_message('#atbash', Dajaxice.ciphers.transcode_atbash);
        });
		$('#caesar .button-encode').on('click', function() {
            transcode_message('#caesar', Dajaxice.ciphers.encode_caesar);
        });
		$('#caesar .button-decode').on('click', function() {
            transcode_message('#caesar', Dajaxice.ciphers.decode_caesar);
        });
		$('#beaufort .button-transcode').on('click', function() {
            transcode_message('#beaufort', Dajaxice.ciphers.transcode_beaufort);
        });
		$('#codeword .button-encode').on('click', function() {
            transcode_message('#codeword', Dajaxice.ciphers.encode_codeword);
        });
		$('#codeword .button-decode').on('click', function() {
            transcode_message('#codeword', Dajaxice.ciphers.decode_codeword);
        });
		$('#vigenere .button-encode').on('click', function() {
            transcode_message('#vigenere', Dajaxice.ciphers.encode_vigenere);
        });
		$('#vigenere .button-decode').on('click', function() {
            transcode_message('#vigenere', Dajaxice.ciphers.decode_vigenere);
        });
		window.onbeforeunload = function() {};
	});
})(jQuery, Dajax, Dajaxice, document, window);