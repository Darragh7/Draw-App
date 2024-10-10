import math
'''
def create_staircase0(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

print(create_staircase0([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(create_staircase0([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


def create_staircase1(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets

print(create_staircase1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(create_staircase1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))




def reverse_word(word):
    reversed = ""
    for letter in word:
      reversed = letter + reversed
    return reversed

def check_all_palindromes(arr):
    if arr[0] == reverse_word(arr[0]):
      if arr[1] == reverse_word(arr[1]):
        if arr[2] == reverse_word(arr[2]):
          return True
    return False

print(check_all_palindromes(["dad", "mom", "racecar"]))
print(check_all_palindromes(["dad", "mom", "car"]))


def reverse_word(word):
    reversed = ""
    for letter in word:
      reversed = letter + reversed
    return reversed

def is_palindrome(word):
    return word == reverse_word(word)

def check_all_palindromes(arr):
    for word in arr:
      if is_palindrome(word) == False:
        return False
    return True

print(check_all_palindromes(["dad", "mom", "racecar"]))
print(check_all_palindromes(["dad", "mom", "car"]))


def reverse_word(word):
    reversed = ""
    for letter in word:
      reversed = letter + reversed
    return reversed

def check_all_palindromes(arr):
    reversed1 = reverse_word(arr[0])
    reversed2 = reverse_word(arr[1])
    reversed3 = reverse_word(arr[2])
    if arr[0] != reversed1:
      return False
    if arr[1] != reversed2:
      return False
    if arr[2] != reversed3:
      return False
    return True

print(check_all_palindromes(["dad", "mom", "racecar"]))
print(check_all_palindromes(["dad", "mom", "car"]))



def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True

print(isPrime(4))


def isPrime(n):
      factors = range(2, n)
      for i in factors:
        if n % i != 0:
          factors.pop(i)
      if factors != []:
        return False
      return True
  
print(isPrime(2))
print(isPrime(4))




def isPrime(n):
    for i in range(2, n):
        if i != 1 and n and n % i == 0:
            return False
            
    return True

print(isPrime(4))
'''


def decode(message_file):
  # Read the contents of the file
  with open(message_file, 'r') as file:
    lines = file.readlines()

  # Extract the numbers and words from each line
  pairs = [line.strip().split(' ') for line in lines]

  # Sort the pairs based on the numbers
  sorted_pairs = sorted(pairs, key=lambda pair: int(pair[0]))

  # Extract the words from the sorted pairs
  words = [pair[1] for pair in sorted_pairs]

  # Join the words into a single string
  decoded_message = ' '.join(words)

  return decoded_message

print(decode('message.txt'))