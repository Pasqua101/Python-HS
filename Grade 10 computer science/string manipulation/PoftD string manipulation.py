#Question 1
word = raw_input("User, please enter two words: ")
word1 = word[0:word.find(' ')+1]
word2 = word[word.find(" ")+1:]
print word2, word1
#Bouns question
word = raw_input("Enter three words: ")
word1 = word[0:word.find(' ')]
word2 = word[word.find(" ")+1:word.rfind(" ")]
word3 = word[word.rfind(" ")+1:]
print word3, word1, word2