import random 

def start():
    play_game()

        
def play_game():
    animals = ['cat', 'tiger', 'cheetah', 'puma', 'lion']
    secret_animal = random.choice(animals)
    guess = input('Guess the animal I am thinking of? ')
    if guess == secret_animal:
        print('Correct!')
    else:
        print('Wrong - I was thinking of ' + secret_animal)

    if input('play again? Type "yes" to continue or press enter to quit '):
        start()

def main():
    start()


if __name__ == '__main__':
    main()