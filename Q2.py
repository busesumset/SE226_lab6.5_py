def palindromes(strings):

  return [string for string in strings if string == string[::-1]]

strings = ['apple', 'banana', 'orange', 'grape','noon', 'tenet', 'pop', 'watermelon', 'kiwi', 'mango', 'pineapple']


palindromes = palindromes(strings)

print(palindromes)

