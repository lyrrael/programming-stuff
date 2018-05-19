pyg = 'ay'

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
#  print original
  word = original.lower()
  first = word[0]
  word = word + first
#  print word
  second = word[1]
  word = word + second
  third = word[2]
  word = word + third + pyg
  s = word
  print s[2:len(word)]
else:
  print 'empty'
