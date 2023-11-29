# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for w in word_list:
            w_lower = w.lower()
            if sorted(w_lower) == sorted_word and w_lower != self.word:
                matches.append(w)
        
        return matches
