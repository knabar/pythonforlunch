from bottle import route, run, debug, request

WORD = 'helicopter'

wrong = 0
guess = '**********'
guessed = []


@route('/play')
def play():
    
    global wrong, guess, guessed, WORD
    
    output = '<h1>Hangman</h1>'

    letter = request.GET.get('letter')
    if letter:
        letter = letter[0].lower()
        if letter in guessed:
            output += '<div>You already guessed %s</div>' % letter
        elif not letter in WORD:
            output += '<div>Ups... %s is not in the word</div>' % letter
            wrong += 1
    
        guessed.append(letter)
    
        guess = ''
        for w in WORD:
            guess += w if w in guessed else '*'

    output += '<div>%s (%s wrong guesses so far)</div>' % (guess, wrong)
    
    if guess == WORD:        
        output += '<div>You win!</div>'
    else:
        output += """
        <form>
            <div>Guess a letter: <input name="letter" /><input type="submit" /></div>
        </form>"""
        
    return output


debug()
run(host='localhost', port=8080, reloader=True)
