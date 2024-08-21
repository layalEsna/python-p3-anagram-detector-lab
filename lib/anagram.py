# your code goes here!
class Anagram:
    def __init__(self, word ):
        self.word = word

    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, word):
        for w in word:
            self._word = word.lower()

    def match(self, word_list):
        anagrams = []
        sorted_word = sorted(self.word)

        for word in word_list:
            if sorted(word.lower()) == sorted_word:
                anagrams.append(word)
        return anagrams