def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, num_questions)

def ask_question(question_info):
    question = question_info["question"]
    correct_answer = question_info["answer"]
    answer = get_answer(question, question_info)
    if answer == correct_answer:
        print("* Correct! *")
        print("Explanation:", question_info.get("explanation", ""))
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}:")
        print("Explanation:", question_info.get("explanation", ""))
        return 0

def run_quiz():
    questions_data = load_questions()
    if not questions_data:
        return
    
    num_questions = 10
    questions = prepare_questions(questions_data, num_questions)
    
    score = 0
    for num, question_info in enumerate(questions, 1):
        print(f"\nQuestion {num}:")
        score += ask_question(question_info)
    
    print(f"\nYou got {score} out of {len(questions)} questions correct.")
    save_score(score, len(questions))