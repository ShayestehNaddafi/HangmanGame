from flask import Flask, jsonify, request
from hangman_game import HangmanGame


app = Flask(__name__)

GAME = None

@app.route('/api/game/start/')
def start_game():
    global GAME
    GAME = HangmanGame()
    return jsonify({
            'status': 'success',
            'message' : 'Game is started'
        })

@app.route('/api/game/state/')
def get_game_state():
    return jsonify(GAME.get_latest_result())

@app.route('/api/game/guess/', methods=['POST'])
def process_guess():
    if request.method == 'POST':
        guess = request.form['guess']
        return jsonify(get_the_guess_result(guess))


def get_the_guess_result(guess):
    if GAME.is_finished():
        return {
            'status': 'error',
            'message': 'game is already finished'
        }

    if len(guess) < 1:
        return {
            'status': 'continue',
            'message': 'please enter a letter or a proper word!'
        }

    GAME.update_state(guess)
    if GAME.is_the_word_completed():
        return {
            'status': 'game over',
            'message': 'Well done, You won'
        }
    elif GAME.number_of_available_guess == 0:
        return {
            'status': 'game over',
            'message': 'You lost! {} was the secret word'.format(GAME.get_secret_word())
        }
    else:
        return {
            'status': 'continue',
            'message': 'The game is updated'
        }

    return result

if __name__ == '__main__':
    app.run(debug=True)