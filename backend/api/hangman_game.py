from random_word import RandomWords


def get_random_word():
    r = RandomWords()
    return r.get_random_word()


class HangmanGame:
    def __init__(self):
        self.secret_word = get_random_word()
        self.number_of_available_guess = 9
        self.latest_result = ['_' for _ in self.secret_word]

    def get_secret_word(self):
        return self.secret_word

    def get_latest_result(self):
        return {
            'status': 'success',
            'latest_word_result' : ' '.join(self.latest_result),
            'number_of_available_guess': self.number_of_available_guess
        }

    def update_state(self, guess):
        if len(guess) == 1:
            if guess in self.secret_word:
                char_positions = [i for i, char in enumerate(self.secret_word) if char == guess]
                for i in char_positions:
                    self.latest_result[i] = guess
                return
        else:
            if guess == self.secret_word:
                self.latest_result = guess
                return

        self.number_of_available_guess -= 1

    def is_the_word_completed(self):
        if '_' in self.latest_result:
            return False
        return True

    def is_finished(self):
        if self.number_of_available_guess == 0 and self.is_the_word_completed():
            return True
        return False