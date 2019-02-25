def word_lengths(phrase):
   return list(map(lambda x: len(x),phrase.split()))

print(word_lengths('How long are the words in this phrase'))


from functools import reduce

def digits_to_num(digits):
  return reduce(lambda x,y: 10*x+y,digits)

print(digits_to_num([3,4,3,2,1]))

def filter_words(word_list, letter):
  return list(filter(lambda x: x[0] == letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

def concatenate(L1, L2, connector):
  results = []
  for a, b in zip(L1, L2):
    results.append(a + connector + b)
  return results

print(concatenate(['A','B'],['a','b'],'-'))

def d_list(L):
  results = {}
  for index, item in enumerate(L):
    results[item] = index
  return results

print(d_list(['a','b','c']))

def count_match_index(L):
  s = 0
  for index, item in enumerate(L):
    if index == item:
      s += 1
  return s

print(count_match_index([0,2,2,1,5,5,6,10]))
