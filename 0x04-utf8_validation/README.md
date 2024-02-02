# UTF-8 Validation

## Overview

This Python program (`validate_utf8.py`) is designed to validate whether a given list of integers represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding capable of encoding all possible characters (code points) in Unicode.

## Background

UTF-8 uses a variable number of bytes to represent characters, ranging from 1 to 4 bytes. The encoding scheme is such that ASCII characters are represented by a single byte, making it backward-compatible with ASCII. Other characters use multiple bytes, with the leading bits indicating the number of bytes in the sequence.

## Program Structure

The program contains a function called `validUTF8`, which takes a list of integers as input and returns `True` if the encoding is valid, and `False` otherwise. The program employs bitwise operations and string formatting to analyze the binary representation of each integer and verify whether it conforms to the UTF-8 encoding rules.

## Usage

To use the program, you can import the `validUTF8` function and pass a list of integers to it. For example:

```python
from validate_utf8 import validUTF8

data = [197, 130, 1]
result = validUTF8(data)

if result:
    print("The provided data is a valid UTF-8 encoding.")
else:
    print("The provided data is not a valid UTF-8 encoding.")
```

## How it Works

The program iterates through the list of integers, converting each integer to its binary representation using the `format` function. It then follows the UTF-8 encoding rules:

- For a single-byte character, the binary representation must start with "0."
- For multi-byte characters, the leading bytes must start with specific patterns ("110," "1110," "11110"), and the continuation bytes must start with "10."

The program keeps track of the expected number of continuation bytes and validates whether the actual bytes match the expected patterns.

## Example

Consider the input `[197, 130, 1]`. The binary representations are `11000101`, `10000010`, and `00000001`, respectively. This represents the three-byte UTF-8 encoding for the character 'Å'.

The program would return `True` for this input, indicating that it is a valid UTF-8 encoding.

## Dependencies

The program does not have external dependencies and should work with any Python 3.x version.

## License

This program is provided under the [MIT License](LICENSE). Feel free to use and modify it as needed
