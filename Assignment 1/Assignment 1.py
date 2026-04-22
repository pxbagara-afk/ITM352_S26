import json
import random
from pathlib import Path
from string import ascii_lowercase

# --- Configuration
QUESTIONS_FILE = "questions.json"
HISTORY_FILE = "score_history.json"
NUM_QUESTIONS_PER_QUIZ = 5

def load_questions():
    #Loads the JSON data safely.
    try:
        with open(QUESTIONS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {QUESTIONS_FILE} not found in this folder.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {QUESTIONS_FILE} contains invalid JSON formatting.")
        return None

def get_answer(question_text, options_list):
    """Displays question/options and returns the user's choice."""
    print(f"\n{question_text}")
    
    # Shuffle the options and pair them with a, b, c, d
    random.shuffle(options_list)
    labeled_options = dict(zip(ascii_lowercase, options_list))
    
    for label, text in labeled_options.items():
        print(f"  {label}) {text}")

    while True:
        choice = input("\nYour Choice: ").lower().strip()
        if choice in labeled_options:
            return labeled_options[choice]
        print(f"⚠️  Please enter a valid letter: {', '.join(labeled_options.keys())}")

def save_score(score, total):
    """Appends the result to the score history file."""
    path = Path(HISTORY_FILE)
    history = []
    
    if path.exists():
        with open(path, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []

    history.append({"score": score, "total": total})
    
    with open(path, "w") as f:
        json.dump(history, f, indent=2)

def run_quiz():
    """Main function to run the quiz."""
    all_data = load_questions()
    if not all_data:
        return

    # Convert dictionary to list of items if necessary to avoid TypeErrors
    if isinstance(all_data, dict):
        # Format: {"Question": {"options": [], "answer": ""}}
        question_pool = list(all_data.items())
    else:
        # Format: [{"question": "", "options": [], "answer": ""}]
        question_pool = all_data

    # Select random questions
    num_to_ask = min(NUM_QUESTIONS_PER_QUIZ, len(question_pool))
    selected_questions = random.sample(question_pool, num_to_ask)
    
    score = 0
#Fix for the quiz game. dictionary and list handling. UsEed AI
    for num, item in enumerate(selected_questions, 1):
        print(f"\n--- Question {num} ---")
        

        if isinstance(item, tuple):
            q_text, info = item
        else:
            q_text, info = item["question"], item

        user_answer = get_answer(q_text, info["options"])
        
        if user_answer == info["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer was: {info['answer']}")

    print(f"{'='*20}")
    print(f"FINAL SCORE: {score} out of {num_to_ask}")
    print(f"{'='*20}")
    
    save_score(score, num_to_ask)

if __name__ == "__main__":
    run_quiz()
    