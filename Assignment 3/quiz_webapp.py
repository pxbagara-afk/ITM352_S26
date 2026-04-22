from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'a_very_secret_and_complex_key_string'

# Pathing to get to json files
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'user_data.json')
QUESTION_FILE = os.path.join(BASE_DIR, 'questions.json')

# --- Global State ---
USER_DATA = {}
QUESTIONS_LIST = [] # Now a global list of question objects
question_num = 0
score = 0

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
    
    # Reset quiz state for the new user session
    global question_num, score
    question_num = 0
    score = 0
    
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, score, QUESTIONS_LIST
    
    if 'user_id' not in session:
        return redirect(url_for('home'))

    # If the user submitted an answer
    if request.method == 'POST':
        current_index = question_num - 1
        current_question_obj = QUESTIONS_LIST[current_index]
        
        correct_answer = current_question_obj.get('answer')
        user_answer = request.form.get('answer')

        if user_answer == correct_answer:
            score += 1
            the_result = "Correct!"
            feedback_color = "green"
        else:
            the_result = "Incorrect"
            feedback_color = "red"
            
        return render_template('question_result.html', 
                               question_result=the_result, 
                               question=current_question_obj['question'], 
                               answer=user_answer, 
                               correct_answer=correct_answer, 
                               feedback_color=feedback_color)

    # --- GET Request Logic (Show next question) ---
    question_num += 1 
    
    if question_num > len(QUESTIONS_LIST):
        return redirect(url_for('result'))
        
    current_index = question_num - 1
    current_q = QUESTIONS_LIST[current_index]
    
    # We use the options exactly as they appear in the JSON (No Random)
    return render_template('quiz.html', 
                           num=question_num, 
                           question=current_q['question'], 
                           options=current_q['options'])

@app.route('/result') 
def result():
    global score, question_num
    user_id = session.get('user_id')
    user_info = USER_DATA.get(user_id)

    if user_info:
        user_info['history'].append({'score': score, 'total': len(QUESTIONS_LIST)})
        save_user_data()

    template = render_template('result.html', score=score, total=len(QUESTIONS_LIST))
    
    # Reset for next time
    score = 0         
    question_num = 0  
    return template 

if __name__ == '__main__':
    load_user_data() 
    
    try:
        if os.path.exists(QUESTION_FILE):
            with open(QUESTION_FILE, 'r', encoding='utf-8') as f:
                # Load as list directly
                QUESTIONS_LIST = json.load(f)
            print(f"✅ Loaded {len(QUESTIONS_LIST)} questions.")
        else:
            print(f"⚠️ Warning: {QUESTION_FILE} not found.")
    except Exception as e:
        print(f"❌ JSON Error: {e}")

    app.run(debug=True, use_reloader=False)