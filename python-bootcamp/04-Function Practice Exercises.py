def spy_game(nums):
  lst = []
  i = 0
  while lst != [0, 0, 7] and i < len(nums):
    if nums[i] == 0 and len(lst) <= 2:
      lst.append(nums[i])
    elif nums[i] == 7 and len(lst) == 2:
      lst.append(nums[i])
    i += 1
  return lst ==[0, 0, 7]

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#***************

def isPrime(n):
    if n == 2 or n == 3:
      return True
    if n % 2 == 0 or n<2:
      return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True



def count_primes(num):
  count = 0
  for i in range(2, num + 1):
    if isPrime(i):
      count += 1
  return count

print(count_primes(100))
