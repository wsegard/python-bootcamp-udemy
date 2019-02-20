import math

def vol(rad):
  return float(4) / float(3) * math.pi * rad**3

print(vol(2))

#*****************

def ran_check(num, low, high):
  if low <= num <= high:
    return True
  else:
    return False

def ran_check_bis(num, low, high):
  return num in range(low, high + 1)

print(ran_check(3,1,10))

#*****************

def up_low(s):
  nb_up = 0
  nb_low = 0
  for letter in s:
    if letter.isupper():
      nb_up += 1
    elif letter.islower():
      nb_low += 1
  return "No. of Upper case characters : {}\nNo. of lower case characters : {}".format(nb_up,nb_low)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))

#*****************

def unique_list(lst):
  lstf = []
  for i in lst:
    if not(i in lstf):
      lstf.append(i)
  return lstf

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#*****************

def multiply(numbers):
  p = 1
  for i in numbers:
    p *= i
  return p

print(multiply([1,2,3,-4]))

#*****************

def palindrome(s):
  s = s.replace(' ','')
  if s == s[::-1]:
    return True
  else:
    return False

def palindrome_bis(s):
  s = s.replace(' ','')
  return s == s[::-1]

print(palindrome('helleh'))

#*****************

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
  r = True
  for letter in alphabet:
    if not(letter in list(str1.lower())):
      r = False
      break
  return r

def ispangram_bis(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))




















