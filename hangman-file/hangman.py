import random

wordfile = open('words.txt')
words = wordfile.readlines()
wordfile.close()

WORD = ''
while len(WORD) < 8:
    WORD = random.choice(words).strip()

wrong = 0
guess = '**********'
guessed = []

while guess != WORD:

    print guess

    print wrong, "wrong guesses so far"
    letter = raw_input('Guess: ')
    if not letter:
        continue

    letter = letter[0]
    letter = letter.lower()
    
    if letter in guessed:
        print "Already guessed!"
        continue
    if not letter in WORD:
        print "Ups..."
        wrong = wrong + 1

    guessed.append(letter)

    guess = ''
    for w in WORD:
        if w in guessed:
            guess = guess + w
        else:
            guess = guess + '*'


print guess
print "You got it!"
