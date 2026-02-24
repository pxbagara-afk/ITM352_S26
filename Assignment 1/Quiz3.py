# Quiz game. Third version
# Name: Paul Bagara
# Date Feb 24, 2026
# Make questions a dictionary, to include answers options and the correct choice

Questions = {
    "What is the airspeed of a unladen swallow n miles/hr? ": ("12", ["12", "15", "20"]),
    "What is the capital of Texas? ": ("Austin", ["Austin", "Dallas", "Houston"]),
    "The last supper was a painting by which artist? ": ("Leonardo da Vinci", ["Leonardo da Vinci", "Michelangelo", "Raphael"])
}

for question, data in Questions.items():
    correct_answer, options = data
    print(f"\n{question}")
    print("Options: " + ", ".join(options))
    
    answer = input("Your answer: ")
    
    if answer == correct_answer:
        print("Correct")
    else:
        print(f"The answer is '{correct_answer}' not {answer}")