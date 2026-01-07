class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt', "r") as f:
            self.words=f.readlines()
    def is_valid_word(self,word):
       for data in self.words:
        if word.upper()==data.strip():
            return True
       return False
    def is_anagram(self,word1, word2):
        word1_list = list(word1)
        word1_list.sort()
        word2_list = list(word2)
        word2_list.sort()
        return (word1_list == word2_list)

    def get_anagrams(self,word):
        anagrams=[]
        for data in self.words:
            if(self.is_anagram(data.strip(),word.upper())):
                anagrams.append(data.strip().lower())
        for anagram in anagrams:
            if anagram==word:
                anagrams.remove(anagram)
        return anagrams
      

