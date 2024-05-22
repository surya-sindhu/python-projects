import random

print("The words will generate in random")

animals=['cat','dog','tiger','lion','giraffe','mouse','leopard','elephant']


class game:
    def __init__(self,random_word):
        self.random_word=random_word
        self.attempts=3
        self.letters=['_']*len(random_word)

    def find(self):

        while self.attempts>0:
            print(" ".join(self.letters))
            user=input("Enter a letter: ")
            user.lower()

            if user in self.random_word:
                print("correct guess")
                for i in range(len(self.random_word)):
                    if self.random_word[i]==user:
                        self.letters[i]=user
            else:
                self.attempts=self.attempts-1
                print(f"Incorrect guess, you have {self.attempts} attempts left")
                print("Hint: The word is animal")

            if '_' not in self.letters:
                print("Correct word")
                print(f"The word is {self.random_word}")
                break
        print(f"Attempts over, the word is {self.random_word}")



while True:
    random_word=random.choice(animals)
    a=game(random_word)
    a.find()
    play_again=input("willing to play again? yes/no - ")
    play_again.lower()
    if(play_again=="yes"):
            continue
    else:
        break
    
    


    
