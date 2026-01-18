class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current = 0

    def get_current_question(self):
        return self.questions[self.current]

    def check_answer(self, choice):
        correct = self.get_current_question()["answer"]
        if choice == correct:
            self.score += 1
            return True
        return False

    def next_question(self):
        self.current += 1
        return self.current < len(self.questions)
