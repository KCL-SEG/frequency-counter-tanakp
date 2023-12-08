"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key_str = str(item)
        frequencies[key_str] = frequencies.get(key_str, 0) + 1
    return frequencies
  