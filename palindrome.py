#Assignment Week 3
#PALINDROME TESTER

word = input("Enter text : ")
print("The word you Enter is",word)


test_word = list(map(str,' '.join(str(word)).split()))

test_word_rev = test_word[::-1]

if test_word == test_word_rev:
    print("The word", word, "is a Palindrome")
else:
    print("The word", word, "is Not a  Palindrome")