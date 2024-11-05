#Christopher Kenny
#CS 175
#Q9: Create a program that finds all anagram pairs in a list of words

words = {'listen', 'enlist', 'hello', 'world', 'drowl'}

def anagrams(words):
  anagram_list = []
  for word1 in words:
    for word2 in words:
      if word1 != word2 and sorted(word1) == sorted(word2):
        anagram_list.append((word1, word2))
  return anagram_list


anagram_pairs = anagrams(words)
print(f'Anagram pairs:', anagram_pairs)
