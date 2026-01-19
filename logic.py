class GuessGame:
    def __init__(self, data, secret):
        self.data = data
        self.secret = secret.lower()

    def check_guess(self, guess):
        guess = guess.lower()

        if guess not in self.data:
            return None

        result = {}
        secret_data = self.data[self.secret]
        guess_data = self.data[guess]

        for key in secret_data:
            result[key] = (guess_data[key] == secret_data[key])

        return result
