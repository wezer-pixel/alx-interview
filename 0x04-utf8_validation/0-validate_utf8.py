#!/usr/bin/env python3

def validUTF8(data):
	"""Checks if a list of integers are valid UTF-8 codepoints.
	See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
	"""
	if not isinstance(data, list):
	raise TypeError("Input must be a list of integers.")

	skip = 0
	n = len(data)
	span = 0

	for i in range(n):
		if skip > 0:
			skip -= 1
			continue

		if type(data[i]) != int or data[i] < 0 or data[i] > 0x10FFFF:
			return False
		elif data[i] <= 0x7F:
			skip = 0
		elif data[i] & 0b11111000 == 0b11110000:
			span = 4
		elif data[i] & 0b11110000 == 0b11100000:
			span = 3
		elif data[i] & 0b11100000 == 0b11000000:
			span = 2
		else:
			return False

		if n - i >= span:
			next_body = list(map(
				lambda x: x & 0b11000000 == 0b10000000,
				data[i + 1: i + span],
			))
			if not all(next_body):
				return False
			skip = span - 1
		else:
			return False

	return True
