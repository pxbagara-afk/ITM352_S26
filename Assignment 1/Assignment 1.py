
"""
Interactive multiple-choice quiz.

Features:
- Loads questions from questions.json (file in same folder).
- Presents each question with options a-d.
- Validates input (only a/b/c/d allowed). Re-prompts on invalid input.
- 50/50 lifeline (type '50' instead of an answer) that removes two incorrect options, usable once.
- Per-question timer; records time-to-answer for correct answers.
- Awards 1 point per correct answer.
- Awards 1 bonus point to the fastest correct answer.
- Awards 1 bonus point if total quiz time is under 60 seconds.
- Well-documented and uses non-trivial function `ask_question`.
"""

import json
import os
import time
import random
from typing import Dict, Tuple, List

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "questions.json")
TOTAL_TIME_BONUS_THRESHOLD = 60.0  # seconds

def load_questions(path: str) -> List[Dict]:
    """Load questions from a JSON file. Each entry must have 'question', 'options', 'answer'."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def apply_5050(options: Dict[str, str], correct: str) -> Dict[str, str]:
    """
    Return a reduced options dict after applying 50/50: keep the correct answer and one random wrong.
    """
    wrong_keys = [k for k in options.keys() if k != correct]
    keep_wrong = random.choice(wrong_keys)
    reduced = {correct: options[correct], keep_wrong: options[keep_wrong]}
    # Ensure ordering a-d is preserved in display; return dict sorted by key
    return dict(sorted(reduced.items()))

def prompt_choice(valid_choices: List[str], lifeline_available: bool) -> str:
    """
    Prompt the user until they enter a valid choice.
    If lifeline_available is True, '50' (use 50/50) is accepted and returned.
    """
    prompt = f"Enter your answer ({'/'.join(valid_choices)})"
    if lifeline_available:
        prompt += " or type '50' to use 50/50 lifeline (once)"
    prompt += ": "
    while True:
        choice = input(prompt).strip().lower()
        if lifeline_available and choice == "50":
            return "50"
        if choice in valid_choices:
            return choice
        print(f"Invalid response: '{choice}'. Please enter one of {', '.join(valid_choices)}.")

def ask_question(q: Dict, lifeline_available: bool) -> Tuple[bool, float, bool]:
    """
    Ask a single question to the user.

    Returns:
    - correct (bool): whether user answered correctly
    - elapsed (float): time taken to submit the final answer (seconds)
    - lifeline_used (bool): whether lifeline was used for this question
    """
    print("\nQuestion:")
    print(q["question"])
    options: Dict[str, str] = q["options"]
    correct = q["answer"].lower()

    # Display options in a-d order
    for k in sorted(options.keys()):
        print(f"  {k}) {options[k]}")

    lifeline_used = False
    start_time = time.time()

    choice = prompt_choice(sorted(options.keys()), lifeline_available)
    if choice == "50":
        # Apply lifeline
        lifeline_used = True
        lifeline_available = False
        reduced = apply_5050(options, correct)
        print("50/50 applied. Remaining options:")
        for k in sorted(reduced.keys()):
            print(f"  {k}) {reduced[k]}")
        choice = prompt_choice(sorted(reduced.keys()), False)

    elapsed = time.time() - start_time
    is_correct = (choice == correct)
    if is_correct:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was '{correct}) {options[correct]}'")
    return is_correct, elapsed, lifeline_used

def main():
    try:
        questions = load_questions(QUESTIONS_FILE)
    except Exception as e:
        print(f"Error loading questions file: {e}")
        return

    print("Welcome to the Interactive Quiz!")
    print("You will be asked multiple-choice questions (a-d).")
    print("Type the letter of your choice and press Enter.")
    print("You may use the 50/50 lifeline once by typing '50' when prompted.\n")

    total_score = 0
    lifeline_available = True
    correct_times: List[float] = []
    total_start = time.time()

    for q in questions:
        correct, elapsed, used = ask_question(q, lifeline_available)
        if used:
            lifeline_available = False
        if correct:
            total_score += 1
            correct_times.append(elapsed)

    total_elapsed = time.time() - total_start

    # Bonus: fastest correct answer +1 (if any correct)
    fastest_bonus = 0
    if correct_times:
        fastest = min(correct_times)
        fastest_bonus = 1
        total_score += fastest_bonus
    # Bonus: total time under threshold
    time_bonus = 0
    if total_elapsed <= TOTAL_TIME_BONUS_THRESHOLD:
        time_bonus = 1
        total_score += time_bonus

    # Results
    print("\nQuiz complete.")
    print(f"Base correct answers: {len(correct_times)} / {len(questions)}")
    if fastest_bonus:
        print(f"Bonus: +{fastest_bonus} point for fastest correct answer (fastest {fastest:.2f} sec)")
    if time_bonus:
        print(f"Bonus: +{time_bonus} point for total time under {TOTAL_TIME_BONUS_THRESHOLD:.0f} seconds")
    print(f"Total time: {total_elapsed:.2f} seconds")
    print(f"Final score: {total_score}")

if __name__ == "__main__":
    main()