from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='Template')
# A secret key is required to use sessions (keeps track of score/progress)
app.secret_key = 'quiz_master_key' 

# Database of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    }
]

@app.route('/')
def index():
    return """
    <h1>Welcome to the Quiz!</h1>
    <a href="/start_quiz"><button>Start Game</button></a>
    """

@app.route('/start_quiz')
def start_quiz():
    session['score'] = 0
    session['question_index'] = 0
    return redirect(url_for('question'))

@app.route('/question')
def question():
    idx = session.get('question_index', 0)
    
    # Check if we finished all questions
    if idx >= len(questions):
        return redirect(url_for('results'))
    
    q = questions[idx]
    
    # Basic HTML structure for the question (usually in a template file)
    options_html = "".join([f'<input type="radio" name="answer" value="{opt}" required> {opt}<br>' for opt in q['options']])
    
    return f"""
    <h2>Question {idx + 1}</h2>
    <p>{q['question']}</p>
    <form action="/submit" method="post">
        {options_html}
        <br>
        <button type="submit">Submit Answer</button>
    </form>
    """

@app.route('/submit', methods=['POST'])
def submit():
    if 'question_index' not in session:
        return redirect(url_for('index'))

    idx = session['question_index']
    user_answer = request.form.get('answer')

    # Compare user answer to correct answer
    if user_answer == questions[idx]['answer']:
        session['score'] += 1

    # Move to next question index
    session['question_index'] += 1
    return redirect(url_for('question'))

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = len(questions)
    return f"""
    <h1>Quiz Finished!</h1>
    <p>Your Score: {score} / {total}</p>
    <a href="/start_quiz">Play Again</a>
    """

if __name__ == "__main__":
    app.run(debug=True)