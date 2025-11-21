class WordGame:
    def __init__(self, *words):
        self._words = words # list of possible worfd
        self._guesses = set() # set of correct guessed letters
        self._letters=  set() # set of all letters in the words
        self._numer_guesses =0 # number of gusses made by user
        self._word= None

    def choose_Words(self):
        import random
        self._word = random.choice(self._words)
        for letter in self._word:
            self._letters.add(letter)
        print(self._word)
        print(self._letters)

    def run(self):
        self.choose_Words()

def main():
    game = WordGame('python', 'java', 'kotlin', 'javascript')
    game.run()
main()