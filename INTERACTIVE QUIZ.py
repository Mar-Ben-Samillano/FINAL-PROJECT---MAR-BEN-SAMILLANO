def run_quiz():
    questions = {
        "What is the largest mammal in the world?": "Whale",
        "What planet in our solar system is known for having a ring??": "Saturn",
        "How many sides does a triagle have?": "3"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + answer)

    print("Quiz completed! You scored {} out of {}.".format(score, len(questions)))

if __name__ == "__main__":
    run_quiz()