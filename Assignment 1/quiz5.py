# Quiz game. Third version
# Name: Paul Bagara
# Date Feb 24, 2026
# Make questions a dictionary, to include answers options and the correct choice
#Allwow for user to choose from multiple options, and check if the answer is correct or not.
#Create a scare board to keep track of the user's score, and display it at the end of the quiz.
Questions = {
    "What is the airspeed of a unladen swallow n miles/hr? ": ("12", ["12", "15", "20"]),
    "What is the capital of Texas? ": ("Austin", ["Austin", "Dallas", "Houston"]),
    "The last supper was a painting by which artist? ": ("Leonardo da Vinci", ["Leonardo da Vinci", "Michelangelo", "Raphael"])
}d

for question, data in Questions.items():
    correct_answer, options = data
    print(f"\n{question}")
    print("Options: " + ", ".join(options))
    
    answer = input("Your answer: ")
    
    if answer == correct_answer:
        print("Correct")
    else:
        print(f"The answer is '{correct_answer}' not {answer}")

    sort_options= sorted(options)
    print(f"Sorted options: {', '.join(sort_options)}"
for alternative in enumerate(options, start=1):
    print(f"{alternative[0]}. {alternative[1]}")

answer_label=int(input (input(question+":"))
                 
answer = sorted_options[answer_label-1]
        print("correct)"
                "else:
                    print(f"The answer is '{correct_answer}' not {answer}")



num_correct = 0
for num (questions,otpions) in enumerate(Questions.items(), start=1):
    print(f"Question {num}:"
    answer = input("Your answer: ")
    if answer == correct_answer:
        num_correct += 1
print(f"You got {num_correct} out of {len(Questions)} correct!")
labeled_alternatives=dict(enumerate(ip(ascii_uppercase, start=1))
                          )

answer_label = inpuut("Choice?")
# Quiz game.  Fifth version.
# Name: Rick Kazman
# Date: Feb. 24, 2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.
# Improve look and usability. Keep track of correct answers.

from string import ascii_lowercase

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
    }


num_correct = 0
for num, (question, options) in enumerate(QUESTIONS.items(), start=1):
    print(f"Question {num}:")
    print(question)
    correct_answer = options[0]  # The first option is the correct answer
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options)))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}. {alternative}")
    
    answer_label = input("Choice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is '{correct_answer}' not {answer!r}")

print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")