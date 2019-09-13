import requests

SERVER_ADR = 'http://127.0.0.1:5000'

def result_output(nr_of_guesses, result):
    print('Number of guesses left : {}'.format(nr_of_guesses))
    print(result)

def get_game_state_detail():
    result_response = requests.get(SERVER_ADR + '/api/game/state/')
    nr_of_guesses = result_response.json()['number_of_available_guess']
    word_status = result_response.json()['latest_word_result']
    return nr_of_guesses, word_status

def get_start_request_response():
    start_response = requests.get(SERVER_ADR + '/api/game/start/')
    return start_response.json()

def get_guess_request_result(guess_input):
    guess_response = requests.post(SERVER_ADR + '/api/game/guess/', data={'guess': guess_input})
    return guess_response.json()

def play():
    start = input( 'Hello, Do you want to play hangman?  y/n ')
    if start != 'y':
        print('why not yes?')
        return
    start_response = get_start_request_response()
    print(start_response['message'])
    if start_response['status'] != 'success':
        return

    while True:
        nr_of_guesses, word_status = get_game_state_detail()
        result_output(nr_of_guesses, word_status)
        if nr_of_guesses == 0:
            print('You Lost, try again!')
            break
        guess_input = input('Please enter a letter or if you can already guess the word enter the word: ')
        guess_response = get_guess_request_result(guess_input)
        print(guess_response['message'])
        if guess_response['status'] == 'game over':
            break


if __name__ == '__main__':
    play()