import random
import itertools
from wonderwords import RandomWord  # remove when done

r = RandomWord()  # REMOVE WHEN DONE

# think of how you'll choose your secret word -> list, .txt, or wonderwords (save it in your head for later)


# starting game values 
secret_word: str = r.word()  # using this to test while we code our game -EDIT BACK TO BANANA
guessed_letters: list[str] = []  # stores all leters guessed in game 
all_players: list[str] = [] # stores players in our game

# shows our incorrect letters
def show_correct_letters():
    # title
    print('\nStatus:')

    # for each letter in the secret word, if it's guessed and in secret word, display, otherwise show _
    for letter in secret_word:
        if letter in guessed_letters and letter in secret_word:
            print(letter, end=' ')  # end= lets all text appear on the same line
        else:
            print('_ ', end='')


# makes our hungry caterpillar and incorrect letters
def show_caterpillar_body():
    print('\nThe hungry letter-pillar')
    caterpillar: str = '@_@'  # creates our caterpillar face
    print(caterpillar, end='')  # prints our caterpillar face

    # makes our caterpillar body
    for letter in guessed_letters:
        if len(letter) > 1:  # checks if user inputed a letter not word
            if letter != secret_word:
                print(f'_{letter}', end='')
        elif letter not in secret_word:
            print(f'_{letter}', end='')  # adds our letter to the caterpillar body


# choose how many players you want and add the players to the all_players list
def choose_number_players():
    how_many_players = int(input('How many players?: '))
    if how_many_players == 1:
        player_name: str = str(input('Lonely world, huh? -_- Your name?: '))
        all_players.append(player_name)
    else:
        for num in range(how_many_players):
            player_name: str = str(input(f'Player {num + 1} name?: '))
            all_players.append(player_name)


# sees if all the letters have been revealed but haven't been guessed
def check_reveal() -> bool:
    correct_letters: set = {*secret_word}  # unpacks all singular letters in secret word
    for letter in correct_letters:
        if letter not in guessed_letters:
            return False

    return True 


# our actual game!
def start_game():
    # user enters player names
    choose_number_players()

    # a list of messages we can say when it's someone's turn
    messages_on_player_turn: list[str] = [
        'May the letters be in your favor',
        'Don\'t feed the hungry letter-pillar',
        'It\'s your turn',
        'Guess a letter'
    ]
    # using iterools helps us cycle through each player for turns
    player = itertools.cycle(all_players)  # current player


    # attempt values. Max can be adjusted to your preference.
    maximum_attempts: int = 7
    current_attempts: int = 0


    # game in action:
    while True:
        # progress screens
        # displays our caterpillar body and correct guesses
        show_caterpillar_body()
        print()
        show_correct_letters()
        print()

        # prints how many attempts we've used
        print(f'The caterpillar\'s belly: {current_attempts}/{maximum_attempts}')        
        
        # turns
        # says random message and displays whose turn it is
        current_player: str = next(player)
        guess_a_letter = str(input(f'{random.choice(messages_on_player_turn)}, {current_player} ->: '))

        # guessing logic
        # conditions if user asks for a word
        if len(guess_a_letter) > 1:  # checks for word

            # if users guesses secret word
            if guess_a_letter.lower() == secret_word:
                print(f'YOU WON {current_player}! The secret word was {secret_word}!!')
                break  # ends the game

            # if users guesses a word that's already been guessed
            elif guess_a_letter in guessed_letters:
                print(f'Already tried the word "{guess_a_letter}"')

            # if user guesses a wrong word
            else:
                print(f'WRONG! {guess_a_letter} is not the secret word.')
                current_attempts += 1
        
        # conditions if user guesses a letter
        # user guesses a letter that's already been guessed
        elif guess_a_letter in guessed_letters:
            print(f'Already tried "{guess_a_letter}"')
        # user guesses a correct letter
        elif guess_a_letter in secret_word:
            print('Correct.')
        # user guesses incorrect letter
        elif guess_a_letter not in secret_word:
            print('Wrong.')
            current_attempts += 1

        # adds our guessed letter/words to the list
        guessed_letters.append(guess_a_letter)

        # end game statememts LOSING
        # check if all the letters were revealed but no one guesssed it - we'll create a new function
        # check if all attempts were used
        if check_reveal():
            print(f'TIE!\nThe secret word "{secret_word}" has been discovered. But no one guessed it.')
            break

        if current_attempts >= maximum_attempts:
            print(f'GAME OVER\nRAN OUT OF ATTEMPTS\nThe secret word was {secret_word}')
            break        


start_game()
