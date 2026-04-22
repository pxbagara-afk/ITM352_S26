from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'itm352_paul_secret'

# Global questions list (accessible by all routes)
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris"],
        "answer": "3"  # Index of 'Paris' in the options list
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "1"  # Index of 'Mars'
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit"],
        "answer": "1"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        # Loop through questions to check the submitted form data
        for i, q in enumerate(QUESTIONS):
            user_answer = request.form.get(f'q{i}')
            if user_answer == q['answer']:
                score += 1
        
        # Store score in session so the result page can see it
        session['score'] = score
        session['total'] = len(QUESTIONS)
        return redirect(url_for('result'))

    # GET request: Show the quiz
    return render_template('quiz.html', questions=QUESTIONS)

@app.route('/result')
def result():
    score = session.get('score', 0)
    total = session.get('total', 0)
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    # Using port 5001 to avoid macOS AirPlay conflicts
    app.run(debug=True, port=5001)