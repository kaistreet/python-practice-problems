#Problem 7.1: Create a Unicode string called mystery and assign it the value '\U0001f4a9'. Print mystery. Look up the Unicode name for mystery.
import unicodedata
mystery = '\U0001f4a9'
print(str(mystery) + ' is a ' + unicodedata.name(mystery))

"""Skipping a few problems because they're irrelevant."""

#Problem 7.8: Import the re module to use Python's regular expresson functions. Use re.findall() to print the number of times Romeo is mentioned
import re
romeo_juliet = "O Romeo, Romeo, wherefore art thou Romeo? Deny thy father and refuse thy name. Or if thou wilt not, be but sworn my love, And I’ll no longer be a Capulet. ‘Tis but thy name that is my enemy: Thou art thyself, though not a Montague. What’s Montague? It is nor hand nor foot Nor arm nor face nor any other part Belonging to a man. O be some other name. What’s in a name? That which we call a rose By any other name would smell as sweet; So Romeo would, were he not Romeo call’d, Retain that dear perfection which he owes Without that title. Romeo, doff thy name, And for that name, which is no part of thee, Take all myself."
pattern = r'\bRo\w*'
print(str(re.findall(pattern,romeo_juliet)[0]) + ' is mentioned ' + str(len(re.findall(pattern,romeo_juliet))) + ' times in the poem.')

"""Alternatively, you can use count method."""
print(romeo_juliet.count('Romeo'))
