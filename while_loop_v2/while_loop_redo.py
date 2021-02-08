import random 

def start():
    while input('play again? Type "yes" to continue or press enter to quit '):
        secret = choose_secret_animal()
        result = play_game(secret)
        if result:
            print('Correct')
        else:
            print('Wrong - I was thinking of ' + secret)
        

def choose_secret_animal():
    animals = ['cat', 'tiger', 'cheetah', 'puma', 'lion']
    secret_animal = random.choice(animals)
    return secret_animal


def play_game(secret_animal):
    guess = input('Guess the animal I am thinking of? ')
    if guess == secret_animal:
        return True
    else:
        return False


def main():
    start()


if __name__ == '__main__':
    main()