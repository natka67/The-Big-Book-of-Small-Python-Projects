import random

MAX_TRIES = 10
NUM_DIGITS = 3

class CustomValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        match self.value:
            case 1:
                return f"Your number has more or less than {NUM_DIGITS} digits."
            case 2:
                return "Your number is not an integer."
            case 3:
                return "Please enter correct value (yes or no)"
            case _:
                return "Unknown error"

def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    unique_number = ''.join(map(str, digits[:NUM_DIGITS]))
    return unique_number


def evaluate_guess(guess, computer_number):

    if len(guess) != NUM_DIGITS:
        raise CustomValueError(1)

    if not guess.isdigit():
        raise CustomValueError(2)
    guessed = 0
    guess = list(guess)
    clues = []
    for digit in guess:
        if digit in computer_number:
            guessed += 1
            if guess.index(digit) == computer_number.index(digit):
                clues.append('Fermi')
            else:
                clues.append('Pico')
    if guessed==0:
        clues.append('Bagels')
    return ' '.join(clues)


def play_again():
    try_again = ''
    while try_again not in ['yes', 'no']:
        try_again = input('Do you want to play again? (yes or no)').lower()
        if try_again == 'yes':
            return True
        elif try_again == 'no':
            return False
        else:
            print("Please enter correct value (yes or no)\n >")

def main():
    welcome_message = f"""Bagels, a deductive logic game.
Implemented by Natalia Adamczyk
  
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico."""
    print(welcome_message)
    turnOn=True
    while turnOn:
        computer_number = generate_number()
        print(computer_number)
        for round in range(1, MAX_TRIES+1):
            try:
                print(f"Guess #{round}")
                guess = input('>>\n')
                if guess == computer_number:
                    print('You got it!')
                    turnOn = play_again()
                    break
                else:
                    print(evaluate_guess(guess, list(computer_number)))
                if round == MAX_TRIES:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(computer_number))
                    turnOn = play_again()

            except CustomValueError as e:
                print(e)



if __name__ == '__main__':
    main()