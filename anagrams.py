from anagram_checker import AnagramChecker
while True:
    word=input("Enter a word to find the anagrams or exit by writting X: ")
    if word=='X':
        print("Exit")
        break
    elif len(word.split())>1:
        print("Only a single word is allowed.")
    elif word.isalpha()==False:
        print("Only alphabetic characters are allowed. No numbers or special characters.")
    else:
        print(f"YOUR WORD : {word.upper()}")
        A=AnagramChecker()
        if(A.is_valid_word(word)):
            print("This is a valid English word.")
            myAnagramList=A.get_anagrams(word)
            print(f"Anagrams for your word: {' '.join(myAnagramList)}")
        else:
            print("Your word doesn't have an anagram")


