#!/usr/bin/python

#import sys
#import math
import re
import string


# todo:
#	- make use of string.ascii_uppercase and string.digits in defaults for alphabets
#	- should we use a negative value for shift when decoding caesar? probably not?
#	- should encode:/decode: call transcode:, or vice-versa?

def xgcd(a, b):
	if b == 0:
		return [1, 0, a]
	else:
		(x, y, d) = xgcd(b, a % b)
		return [y, x - (a // b) * y, d]

def prune_string(s, use_digits=False):
	rv = None
	if s:
		if use_digits:
			re_string = r'[^A-Z0-9]'
		else:
			re_string = r'[^A-Z]'
		rv = re.sub(re_string, '', s.upper())
	return rv

def filter_string(s):
	rv = None
	if s:
		rv = re.sub('[^A-Za-z0-9]', '', s)
	return rv

def unique_string(s):
	filtered = None
	if s and len(s) > 0:
		filtered = ''
		for c in s:
			if c not in filtered: filtered += c
	return filtered

def wrap_string(s, offset):
	shifted = s
	if len(s) > 0:
		offset = int(offset) % len(s)
		shifted = s[offset:] + s[:offset]
	return shifted

def split_string(s, c):
	words = [s[i:i+c] for i in xrange(0, len(s), c)]
	return ' '.join(words)

def pad_string(s, c, char='X'):
	padding = (len(s) * (c - 1)) % c
	return (s + char * padding)

def reverse_string(s):
	return s[::-1]

class CipherAlphabet:
	source_alphabet = None
	target_alphabet = None

	#canonical_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	#canonical_numbers = '0123456789'
	#padding_character = 'x'

	def __init__(self, chars, should_filter=True):
		chars = unique_string(chars).upper()
		if should_filter:
			chars = filter_string(chars)

		self.source_alphabet = chars
		self.target_alphabet = chars

class AffineAlphabet(CipherAlphabet):
	def __init__(self, chars, multiplier=1, additive=0, should_filter=True, for_encoding=True):
		chars = unique_string(chars).upper()
		if should_filter:
			chars = filter_string(chars)

		self.source_alphabet = chars

		if len(chars) > 0:
			gcd = xgcd(len(chars), multiplier)
			if multiplier % 2 != 0 and gcd[2] == 1:
				temp_target = ''
				if for_encoding:
					for i in xrange(len(chars)):
						a_prime = (int(multiplier) * i + int(additive)) % len(chars)
						temp_target += chars[a_prime]
				else:
					mult_inverse = (gcd[1] + len(chars)) % len(chars)
					for i in xrange(len(chars)):
						a_prime = (mult_inverse * (i - int(additive) + len(chars))) % len(chars)
						temp_target += chars[a_prime]
				self.target_alphabet = temp_target
			else:
				self.target_alphabet = chars
		else:
			self.target_alphabet = chars

class AtbashAlphabet(CipherAlphabet):
	def __init__(self, chars, should_filter=True):
		chars = unique_string(chars).upper()
		if should_filter:
			chars = filter_string(chars)

		self.source_alphabet = chars
		self.target_alphabet = chars[::-1]

class CaesarAlphabet(CipherAlphabet):
	def __init__(self, chars, shift, should_filter=True):
		chars = unique_string(chars).upper()
		if should_filter:
			chars = filter_string(chars)

		self.source_alphabet = chars
		self.target_alphabet = wrap_string(chars, shift)

class CodewordAlphabet(CipherAlphabet):
	def __init__(self, chars, keyword, should_filter=True):
		if chars:
			chars = unique_string(chars).upper()
			if should_filter: chars = filter_string(chars)
		if keyword:
			keyword = unique_string(keyword).upper()
			if should_filter: keyword = filter_string(keyword)

		self.source_alphabet = chars
		if keyword:
			pattern = re.compile('[' + keyword + ']')
			trimmed_alphabet = re.sub(pattern, '', chars)
			self.target_alphabet = keyword + trimmed_alphabet
		else:
			self.target_alphabet = chars

class TabulaRecta:
	table = []
	alpha_len = 0
	alpha_chars = ''

	def __init__(self, cipher_alphabet, primer=0):
		table_tmp = []

		# filter and constrain alphabet
		#alphabet = alphabet.upper()
		#alphabet = filter_string(alphabet)
		#alphabet = unique_string(alphabet)

		alphabet = cipher_alphabet.target_alphabet
		self.alpha_len = len(cipher_alphabet.target_alphabet)
		# [todo] remove this and use the abstracted-away alphabet object
		self.alpha_chars = cipher_alphabet.target_alphabet

		# filter and constrain primer index
		# [need sanity check]
		try:
			primer = int(primer)
		except ValueError as e:
			print('[WARNING] Invalid primer; using 0')
			primer = 0

		if len(alphabet) > 0:
			primer %= len(alphabet)
			table_tmp = [wrap_string(alphabet, i + primer) for i in range(len(alphabet))]
	
		self.table = table_tmp

	def transpose_character_for_character(self, c, k):
		out_c = ''
		try:
			c_temp = None

			col = self.alpha_chars.find(c)

			if col != -1:
				row = self.table[col].find(k)
				if row != -1:
					c_temp = self.alpha_chars[row]

			out_c = c_temp
		except Exception as e:
			print e
			pass
		return out_c

	def encode_char_for_char(self, c, k):
		out_c = ''
		try:
			c_temp = None

			col = self.alpha_chars.find(c)
			row = self.alpha_chars.find(k)

			if col != -1 and row != -1:
				c_temp = self.table[row][col]

			out_c = c_temp
		except Exception as e:
			print e
			pass
		return out_c

	def decode_char_for_char(self, c, k):
		out_c = ''
		try:
			c_temp = None

			col = self.alpha_chars.find(k)
			if col != -1:
				row = self.table[col].find(c)
				if row != -1:
					c_temp = self.alpha_chars[row]

			out_c = c_temp
		except Exception as e:
			print e
			pass
		return out_c

	def p(self, delimiter=' '):
		return '\n'.join([delimiter.join(list(row)) for row in self.table])

class Transcoder:
	canonical_letters = string.ascii_uppercase
	canonical_numbers = string.digits
	#padding_character = 'x'

	tabula_recta = None

	def monoalpabetic_transcode(self, message, cipher_ab, lower=False, should_filter=False, chunk=0, encode=True):
		if encode:
			source_ab = cipher_ab.source_alphabet
			target_ab = cipher_ab.target_alphabet
		else:
			source_ab = cipher_ab.target_alphabet
			target_ab = cipher_ab.source_alphabet

		output = ''

		# filter chunk size
		chunk = int(chunk)

		 # filter and pad the string (if necessary)
		if should_filter:
			message = filter_string(message)
			if chunk > 0:
				message = pad_string(message, chunk)

		# convert message to upper-case (currently necessary for processing)
		message = message.upper()

		for a in message:
			j = source_ab.find(a)
			b = ''

			if j != -1:
				# matched to the coded alphabet
				b = target_ab[j]
			else: 
				# not matched, so append verbatim; may occur with punctuation
				b = a
			output += b

		# divide the string, if necessary
		if should_filter and chunk > 0:
			output = split_string(output, chunk)

		if lower:
			output = output.lower()

		return output

class AffineTranscoder(Transcoder):
	alphabet = None

	def __init__(self):
		pass

	def transcode(self, message, multiplier=1, additive=0, lower=False, should_filter=False, chunk=0, encode=True):
		if encode:
			return self.encode(message, multiplier=multiplier, additive=additive, lower=lower, should_filter=should_filter, chunk=chunk)
		else:
			return self.decode(message, multiplier=multiplier, additive=additive, lower=lower, should_filter=should_filter, chunk=chunk)

	def encode(self, message, multiplier=1, additive=0, lower=False, should_filter=False, chunk=0):
		self.alphabet = AffineAlphabet(self.canonical_letters, multiplier=multiplier, additive=additive, for_encoding=True)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk)

	def decode(self, message, multiplier=1, additive=0, lower=False, should_filter=False, chunk=0):
		self.alphabet = AffineAlphabet(self.canonical_letters, multiplier=multiplier, additive=additive, for_encoding=False)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk)

class AtbashTranscoder(Transcoder):
	alphabet = None

	def __init__(self):
		pass

	def transcode(self, message, lower=False, should_filter=False, chunk=0):
		self.alphabet = AtbashAlphabet(self.canonical_letters)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk)

class BeaufortTranscoder(Transcoder):
	def __init__(self):
		pass
		#self.create_tabula_recta()

	def transcode(self, message, passphrase, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0):
		# chunk_size is not yet implemented here
		output = ''

		message = message.upper()
		passphrase = passphrase.upper()
		passphrase = prune_string(passphrase, use_digits)

		if should_filter:
			message = prune_string(message, use_digits)
			if chunk > 0:
				message = pad_string(message, chunk)

		if passphrase is not None and len(passphrase) > 0:
			if not use_digits:
				self.alphabet = CodewordAlphabet(string.ascii_uppercase, keyword=keyword)
			else:
				self.alphabet = CodewordAlphabet(string.ascii_uppercase + string.digits, keyword=keyword)
			self.tabula_recta = TabulaRecta(self.alphabet, primer)

			passphrase_index = 0

			for c in message:
				k = passphrase[passphrase_index % len(passphrase)]
				char_temp = self.tabula_recta.transpose_character_for_character(c, k)
				if char_temp:
					output += char_temp
					passphrase_index += 1
				else:
					output += c
		else:
			output = message

		if should_filter and chunk > 0:
			output = split_string(output, chunk)
		
		if lower:
			output = output.lower()
		
		return output

class CaesarTranscoder(Transcoder):
	alphabet = None

	def __init__(self):
		pass

	def transcode(self, message, shift=0, lower=False, should_filter=False, chunk=0, encode=True):
		if encode:
			return self.encode(message, shift, lower, should_filter, chunk)
		else:
			return self.decode(message, shift, lower, should_filter, chunk)

	def encode(self, message, shift=0, lower=False, should_filter=False, chunk=0):
		self.alphabet = CaesarAlphabet(self.canonical_letters, shift=shift)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk)

	def decode(self, message, shift=0, lower=False, should_filter=False, chunk=0):
		self.alphabet = CaesarAlphabet(self.canonical_letters, shift=shift)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk, encode=False)

class CodewordTranscoder(Transcoder):
	alphabet = None

	def __init__(self):
		pass

	def transcode(self, message, keyword=None, lower=False, should_filter=False, chunk=0, encode=True):
		if encode:
			return self.encode(message, keyword, lower, should_filter, chunk)
		else:
			return self.decode(message, keyword, lower, should_filter, chunk)

	def encode(self, message, keyword=None, lower=False, should_filter=False, chunk=0):
		self.alphabet = CodewordAlphabet(self.canonical_letters, keyword=keyword)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk)

	def decode(self, message, keyword=None, lower=False, should_filter=False, chunk=0):
		self.alphabet = CodewordAlphabet(self.canonical_letters, keyword=keyword)
		return self.monoalpabetic_transcode(message, self.alphabet, lower, should_filter, chunk, encode=False)

class VigenereTranscoder(Transcoder):
	def __init__(self):
		pass
		#self.create_tabula_recta()

	def encode(self, message, passphrase, autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0):
		return self.transcode(message=message, passphrase=passphrase, autoclave=autoclave, keyword=keyword, primer=primer, use_digits=use_digits, lower=lower, should_filter=should_filter, encode=True)

	def decode(self, message, passphrase, autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0):
		return self.transcode(message=message, passphrase=passphrase, autoclave=autoclave, keyword=keyword, primer=primer, use_digits=use_digits, lower=lower, should_filter=should_filter, encode=False)

	def transcode(self, message, passphrase, autoclave=False, keyword=None, primer=0, use_digits=False, lower=False, should_filter=False, chunk=0, encode=True):
		# chunk_size is not yet implemented here
		output = ''

		message = message.upper()
		passphrase = passphrase.upper()
		passphrase = prune_string(passphrase, use_digits)

		if should_filter:
			message = prune_string(message, use_digits)
			if chunk > 0:
				message = pad_string(message, chunk)

		#if autoclave and encode:
		#	passphrase += message

		if passphrase is not None and len(passphrase) > 0:
			if not use_digits:
				self.alphabet = CodewordAlphabet(string.ascii_uppercase, keyword=keyword)
			else:
				self.alphabet = CodewordAlphabet(string.ascii_uppercase + string.digits, keyword=keyword)
			self.tabula_recta = TabulaRecta(self.alphabet, primer)

			passphrase_index = 0

			for c in message:
				k = passphrase[passphrase_index % len(passphrase)]

				if encode:
					char_temp = self.tabula_recta.encode_char_for_char(c, k)
				else:
					char_temp = self.tabula_recta.decode_char_for_char(c, k)
				if char_temp:
					if autoclave:
						if encode:
							passphrase += c
						else:
							passphrase += char_temp
					output += char_temp
					passphrase_index += 1
				else:
					output += c
		else:
			output = message

		if should_filter and chunk > 0:
			output = split_string(output, chunk)
		
		if lower:
			output = output.lower()
		
		return output


#x = VigenereTranscoder()
#print 'WSLZ RO GIWW SOB KEWWU1234 <= should be this for standard'
#print 'WSLZ RO GESL FDN KMWWA1234 <= should be this for autoclave'
#
#phrase1 = "these are the times that try men's souls these are the times that try men's souls these are the times that try men's souls these are the times that try men's souls"
#key1 = "in the course of our nation's history in"
#key2 = "in the course of our nation's history in these are the times that try men's souls these are the times that try men's souls these are the times that try men's souls these are the times that try men's souls"
#y = x.transcode(phrase1, passphrase=key2, encode=True, use_digits=True, autoclave=True)
#y2 = x.transcode(y, passphrase=key2, encode=False, use_digits=True, autoclave=True)


#x = AffineTranscoder()
#y = x.transcode('what da dill man hello', multiplier=3, additive=4, encode=False)
#y2 = x.decode(y, multiplier=3, additive=4)
#print(y)
#print(y2)
#y = x.transcode('WHAT da dill man hello1234', passphrase='all good', use_digits=True)
#y2 = x.transcode(y, passphrase='all good', use_digits=True)
#print(y)
#print(y2)

#x = BeaufortTranscoder()
#y = x.transcode('WHAT da dill man hello1234', passphrase='all good', use_digits=True)
#y2 = x.transcode(y, passphrase='all good', use_digits=True)
#print(y)
#print(y2)
#x = VigenereTranscoder()
#print 'WSLZ RO GIWW SOB KEWWU1234 <= should be this for standard'
#print 'WSLZ RO GESL FDN KMWWA1234 <= should be this for autoclave'
#y = x.transcode('WHAT da dill man hello1234', passphrase='all good', encode=True, use_digits=True, autoclave=True)
#y2 = x.transcode(y, passphrase='all good', encode=False, use_digits=True, autoclave=True)
###x = AtbashTranscoder()
#print(y)
#print y2

#shift_value = 3
#ca = CipherAlphabet('abcdedfghijklmnopqrstuvwxyz', shift=shift_value, keyword='cute')
#print('shift +{} source: {}'.format(shift_value, ca.source_alphabet))
#print('shift +{} target: {}'.format(shift_value, ca.target_alphabet))
#
#ca = CipherAlphabet('abcdedfghijklmnopqrstuvwxyz', shift=-shift_value, keyword='cute')
#print('shift -{} source: {}'.format(shift_value, ca.source_alphabet))
#print('shift -{} target: {}'.format(shift_value, ca.target_alphabet))


#print(wrap_string('12345678', 9))

#t = TabulaRecta('abcdeFFfg', 'a')
#t = Transcoder()
#t.create_tabula_recta()
#print(t.tabula_recta.p())

#a = CipherAlphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '')
#print(a.alphabet)
