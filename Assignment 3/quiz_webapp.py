from flask import Flask, render_template, request, redirect, url_for, session
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'a_very_secret_and_complex_key_string'

# --- Path Configuration ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'user_data.json')
QUESTION_FILE = os.path.join(BASE_DIR, 'questions.json')

# --- Global State ---
USER_DATA = {}
QUESTIONS = {}
questions_list = []
question_num = 0
score = 0
NUM_QUESTIONS_PER_QUIZ = 10

def load_user_data():
    global USER_DATA
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                USER_DATA = json.load(f)
            except json.JSONDecodeError:
                USER_DATA = {}

def save_user_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(USER_DATA, f, indent=2)

def prepare_questions(all_questions, num_questions):
    if not all_questions:
        return []
    # This picks a random sample of the dictionary items (key-value pairs)
    num_to_pick = min(num_questions, len(all_questions))
    selected_items = random.sample(list(all_questions.items()), k=num_to_pick)
    
    # item[0] is the Question Text (the key)
    # item[1] is the dictionary containing 'options' and 'answer'
    return [(item[0], item[1]['options']) for item in selected_items]

@app.route('/')
def home():
    user_id = session.get('user_id')
    user_info = USER_DATA.get(user_id, {})
    username = user_info.get('username')
    history = user_info.get('history', [])
    return render_template('index.html', username=username, history=history)

@app.route('/set_name', methods=['POST'])
def set_name():
    new_username = request.form.get('name')
    if not new_username:
        return redirect(url_for('home'))
        
    session['user_id'] = new_username
    if new_username not in USER_DATA:
        USER_DATA[new_username] = {'username': new_username, 'history': []}
    
    save_user_data()
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, QUESTIONS, score, questions_list
    
    if 'user_id' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        current_index = question_num - 1
        current_text = questions_list[current_index][0]
        
        # Use .get() with defaults to avoid KeyErrors
        correct_answer = QUESTIONS[current_text].get('answer')
        user_answer = request.form.get('answer')

        if user_answer == correct_answer:
            score += 1
            the_result = " Correct!"
            feedback_color = "green"
        else:
            the_result = "Incorrect"
            feedback_color = "red"
            
        return render_template('question_result.html', 
                               question_result=the_result, 
                               question=current_text, 
                               answer=user_answer, 
                               correct_answer=correct_answer, 
                               feedback_color=feedback_color)

    # --- GET Request Logic ---
    question_num += 1 
    
    if question_num > len(questions_list):
        return redirect(url_for('result'))
        
    current_index = question_num - 1
    question_text = questions_list[current_index][0]
    options = questions_list[current_index][1]
    
    # Shuffle options for display
    shuffled_options = random.sample(options, len(options))

    return render_template('quiz.html', num=question_num, question=question_text, options=shuffled_options)

@app.route('/result') 
def result():
    global score, question_num, questions_list
    user_id = session.get('user_id')
    user_info = USER_DATA.get(user_id)

    if user_info:
        user_info['history'].append({'score': score, 'total': len(questions_list)})
        save_user_data()

    template = render_template('result.html', score=score, total=len(questions_list))
    
    score = 0         
    question_num = 0  
    return template 

if __name__ == '__main__':
    load_user_data() 
    
    try:
        if os.path.exists(QUESTION_FILE):
            with open(QUESTION_FILE, 'r', encoding='utf-8') as f:
                QUESTIONS = json.load(f)
            questions_list = prepare_questions(QUESTIONS, NUM_QUESTIONS_PER_QUIZ)
            print(f"✅ Loaded {len(QUESTIONS)} questions.")
        else:
            print(f"⚠️ Warning: {QUESTION_FILE} not found.")
    except Exception as e:
        print(f"❌ JSON Error: {e}")

    app.run(debug=True, use_reloader=False)