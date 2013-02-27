from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
#from dajaxice.core import dajaxice_functions
from cypher import *
import random
from django.utils.encoding import smart_unicode

@dajaxice_register(method='GET')
def encode_affine(request, container, message='', multiplier=1, additive=0, lower=False, should_filter=False, chunk=0):
    return _transcode_affine(request, container, message=message, multiplier=multiplier, additive=additive, lower=lower, should_filter=should_filter, chunk=chunk, encode=True)

@dajaxice_register(method='GET')
def decode_affine(request, container, message='', multiplier=1, additive=0, lower=False, should_filter=False, chunk=0):
    return _transcode_affine(request, container, message=message, multiplier=multiplier, additive=additive, lower=lower, should_filter=should_filter, chunk=chunk, encode=False)

def _transcode_affine(request, container, message='', multiplier=1, additive=0, lower=False, should_filter=False, chunk=0, encode=True):
	tc = AffineTranscoder()
	result = tc.transcode(message=message, multiplier=int(multiplier), additive=int(additive), lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign(container + ' .field-target', 'value', smart_unicode(result))
	dajax.assign(container + ' .field-plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign(container + ' .field-ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_atbash(request, container, message='', lower=False, should_filter=False, chunk=0):
	tc = AtbashTranscoder()
	result = tc.transcode(message=message, lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk))
	dajax = Dajax()
	dajax.assign(container + ' .field-target', 'value', smart_unicode(result))
	dajax.assign(container + ' .field-plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign(container + ' .field-ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def transcode_beaufort(request, container, message='', passphrase='', keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0):
	tc = BeaufortTranscoder()
	result = tc.transcode(message=message, passphrase=passphrase, keyword=keyword, primer=int(primer), use_digits=bool(use_digits), lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk))
	dajax = Dajax()
	dajax.assign(container + ' .field-target', 'value', smart_unicode(result))
	return dajax.json()

@dajaxice_register(method='GET')
def encode_caesar(request, container, message='', shift=0, lower=False, should_filter=False, chunk=0):
    return _transcode_caesar(request, container, message=message, shift=shift, lower=lower, should_filter=should_filter, chunk=chunk, encode=True)

@dajaxice_register(method='GET')
def decode_caesar(request, container, message='', shift=0, lower=False, should_filter=False, chunk=0):
    return _transcode_caesar(request, container, message=message, shift=shift, lower=lower, should_filter=should_filter, chunk=chunk, encode=False)

def _transcode_caesar(request, container, message='', shift=0, lower=False, should_filter=False, chunk=0, encode=True):
	tc = CaesarTranscoder()
	result = tc.transcode(message=message, shift=shift, lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign(container + ' .field-target', 'value', smart_unicode(result))
	dajax.assign(container + ' .field-plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign(container + ' .field-ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def encode_codeword(request, container, message='', keyword=None, lower=False, should_filter=False, chunk=0):    
    return _transcode_codeword(request, container, message=message, keyword=keyword, lower=lower, should_filter=should_filter, chunk=chunk, encode=True)

@dajaxice_register(method='GET')
def decode_codeword(request, container, message='', keyword=None, lower=False, should_filter=False, chunk=0):
    return _transcode_codeword(request, container, message=message, keyword=keyword, lower=lower, should_filter=should_filter, chunk=chunk, encode=False)

def _transcode_codeword(request, container, message='', keyword=None, lower=False, should_filter=False, chunk=0, encode=True):
	tc = CodewordTranscoder()
	result = tc.transcode(message=message, keyword=keyword, lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign(container + ' .field-target', 'value', smart_unicode(result))
	dajax.assign(container + ' .field-plaintext', 'value', str(tc.alphabet.source_alphabet))
	dajax.assign(container + ' .field-ciphertext', 'value', str(tc.alphabet.target_alphabet))
	return dajax.json()

@dajaxice_register(method='GET')
def encode_vigenere(request, container, message='', passphrase='', autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0, encode=True):
    return _transcode_vigenere(request, container, message=message, passphrase=passphrase, autoclave=autoclave, keyword=keyword, primer=primer, use_digits=use_digits, lower=lower, should_filter=should_filter, chunk=chunk, encode=True)

@dajaxice_register(method='GET')
def decode_vigenere(request, container, message='', passphrase='', autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0, encode=True):
    return _transcode_vigenere(request, container, message=message, passphrase=passphrase, autoclave=autoclave, keyword=keyword, primer=primer, use_digits=use_digits, lower=lower, should_filter=should_filter, chunk=chunk, encode=False)

def _transcode_vigenere(request, container, message='', passphrase='', autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0, encode=True):
	tc = VigenereTranscoder()
	result = tc.transcode(message=message, passphrase=passphrase, autoclave=bool(autoclave), keyword=keyword, use_digits=bool(use_digits), lower=bool(lower), should_filter=bool(should_filter), chunk=int(chunk), encode=bool(encode))
	dajax = Dajax()
	dajax.assign(container + ' .field-target', 'value', smart_unicode(result))
	return dajax.json()

