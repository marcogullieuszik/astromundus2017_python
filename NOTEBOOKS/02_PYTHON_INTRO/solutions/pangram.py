import string

alpha = string.ascii_lowercase
def is_pangram(str):
  found = []
  for c in str.lower():
    if c in alpha and c not in found:
      found.append(c)
  if len(found) == len(alpha):
    return True
  else:
    return False

#test
s1="The quick brown fox jumps over the lazy dog."
s2="Obviously not a pangram"
print (is_pangram(s1))
print (is_pangram(s2))
    