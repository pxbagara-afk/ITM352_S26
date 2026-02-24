#Quz game. Second verion
#Name: Paul Bagara
#Date Feb 24, 2026
#Make a list with the questions and correct answers
questions = [
    ("What is the airspeed of a unladen swallow n miles/hr?", "12"),
    ("What is the capital of Texas?", "Austin")
    ("The last supper was a painting by which artist?", "Leonardo da Vinci")
]

for question, correct_answer in questions:
    answer = input(question)
    if answer == correct_answer:
        print("Correct")
    else:
        print(f"The answer is '{correct_answer}' not {answer}")