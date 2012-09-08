from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
#from dajaxice.core import dajaxice_functions
from cypher import *
import random
from django.utils.encoding import smart_unicode

@dajaxice_register(method='GET')
def transcode_affine(request, message='', multiplier=1, additive=0, lower=False, should_filter=False, chunk=0, encode=True):
	tc = AffineTranscoder()
	result = tc.transcode(message=message, multiplier=int(multiplier), additive=int(additive), lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign('#af_target', 'value', smart_unicode(result))
	dajax.assign('#af_plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign('#af_ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_atbash(request, message='', lower=False, should_filter=False, chunk=0):
	tc = AtbashTranscoder()
	result = tc.transcode(message=message, lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk))
	dajax = Dajax()
	dajax.assign('#at_target', 'value', smart_unicode(result))
	dajax.assign('#at_plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign('#at_ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_beaufort(request, message='', passphrase='', keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0):
	tc = BeaufortTranscoder()
	result = tc.transcode(message=message, passphrase=passphrase, keyword=keyword, primer=int(primer), use_digits=bool(use_digits), lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk))
	dajax = Dajax()
	dajax.assign('#bf_target', 'value', smart_unicode(result))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_caesar(request, message='', shift=0, lower=False, should_filter=False, chunk=0, encode=True):
	tc = CaesarTranscoder()
	result = tc.transcode(message=message, shift=shift, lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign('#cr_target', 'value', smart_unicode(result))
	dajax.assign('#cr_plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign('#cr_ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_codeword(request, message='', keyword=None, lower=False, should_filter=False, chunk=0, encode=True):
	tc = CodewordTranscoder()
	result = tc.transcode(message=message, keyword=keyword, lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign('#cw_target', 'value', smart_unicode(result))
	dajax.assign('#cw_plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign('#cw_ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_vigenere(request, message='', passphrase='', autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0, encode=True):
	tc = VigenereTranscoder()
	result = tc.transcode(message=message, passphrase=passphrase, autoclave=bool(autoclave), keyword=keyword, use_digits=bool(use_digits), lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign('#vi_target', 'value', smart_unicode(result))
	return dajax.json()

