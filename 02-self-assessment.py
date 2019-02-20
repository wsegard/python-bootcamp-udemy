st = 'Print only the words that start with s in this sentence'
st_list = st.lower().split()
for i in st_list:
  if i[0] == 's':
    print i

#******************

for i in range(0,11):
  if i % 2 == 0:
    print i

list(range(0,11,2))

#******************

li = [x for x in range(0,51) if x % 3 == 0]
print(li)

#******************

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
  if len(word) % 2 == 0:
    print(word +" <-- has an even length!")

#******************

for i in range(0,101):
  if i % 15 == 0:
    print ('FizzBuzz')
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)

#******************

st = 'Create a list of the first letters of every word in this string'
print([x[0] for x in st.split() ])
