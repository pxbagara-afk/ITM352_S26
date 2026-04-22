import os
import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'simple_quiz_key'

#Had trouble with file pathing. Used A.I to fix it. Prompt:" How to fix file pathing issues in flask app"
def load_questions_from_file():
    folder_where_this_script_lives = os.path.dirname(os.path.abspath(__file__))
    full_path_to_json_file = os.path.join(folder_where_this_script_lives, 'questions.json')
    with open(full_path_to_json_file, 'r') as open_file:
        return json.load(open_file)

# Variable in order to call for question
ALL_QUIZ_QUESTIONS = load_questions_from_file()

#Route to home page, ask for name, in order to save score history, and to start quiz
@app.route('/')
def home():
    return render_template('index.html', 
                           player_name=session.get('player_name'), 
                           past_game_scores=session.get('game_history', []))

#Route to start quiz and to start a quiz sesion if didn't exist already
@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    # Set up everything for a brand new game. Had to use A.I to handle for errors with starting game. WOuld provide error if didn't
    session['player_name'] = request.form['name']
    session['current_score'] = 0
    session['current_question_index'] = 0
    # Get thes question titles such as Question 1, 2,3,. Used A.I in order to create a title for each questino since List does not have these titles
    session['list_of_question_titles'] = list(ALL_QUIZ_QUESTIONS.keys())
    #Requirement 9: Create a list to store result of all questions
    session['quiz_summary'] = []
    #directs to quiz page. and used A.I to suggest using this since it would refresh back to home page even after presssing start
    return redirect(url_for('quiz_page'))


#ROute to quiz page, has question title and information on current question, 
@app.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    question_titles = session.get('list_of_question_titles', [])
    current_index = session.get('current_question_index', 0)

    # Check if the player has finished all questions. Used A.I in order to account for when player finish game. Prompt used "How to check if player has finished quiz in flask app"
    if current_index >= len(question_titles):
        return redirect(url_for('show_final_results'))

    # Get the specific data for the current question and how much more questions there are
    title_of_current_question = question_titles[current_index]
    data_for_current_question = ALL_QUIZ_QUESTIONS[title_of_current_question]

#Checks to see if player has submitted answer and if it is correct wrong. Adds points to session if correct. Used A.I in order to handle logic statements
    if request.method == 'POST':
        player_choice = request.form.get('answer')
        actual_correct_answer = data_for_current_question['answer']
        
        if player_choice == actual_correct_answer:
            session['current_score'] = session['current_score'] + 1
            feedback_message = "Correct!"
            is_correct_bool = True
        else:
            feedback_message = "Incorrect"
            is_correct_bool = False

        # Requirement 9 save question data for summary page. So player knows what they got right and wrong and why. 
        question_result_data = {
            'title': title_of_current_question,
            'player_choice': player_choice,
            'correct_answer': actual_correct_answer,
            'is_correct': is_correct_bool
        }
        
        # Get the current list from session, add the new result, and save it back
        summary_list = session.get('quiz_summary', [])
        summary_list.append(question_result_data)
        session['quiz_summary'] = summary_list

#Summary data does not work without this. USed A.I in order to handle error of answer not being saved to summary sheet
        session.modified = True 

        # Counts up so the next page shows the next questions starts from 0
        session['current_question_index'] = session['current_question_index'] + 1
        
        #Shows all infomration in results page
        return render_template('questions_results.html', 
                               result_text=feedback_message, 
                               question_text=title_of_current_question, 
                               player_answer=player_choice, 
                               correct_answer=actual_correct_answer, 
                               why_it_is_correct=data_for_current_question['explanation'])

#In order to loop through questions and move on to the next ones. Used A.I in order to handle looping through questions and moving on to the next one.
    return render_template('quiz.html', 
                           question_number=current_index + 1, 
                           question_text=title_of_current_question, 
                           list_of_options=data_for_current_question['options'])


#After the end of the game final score is shown and saved in player history.
@app.route('/result')
def show_final_results():
    final_score = session.get('current_score', 0)
    total_questions = len(session.get('list_of_question_titles', []))
    
    # Get the compiled list of all question results to show on the final page
    all_question_results = session.get('quiz_summary', [])
    
    # Update the player's history list
    game_history = session.get('game_history', [])
    game_history.append({'score': final_score, 'total': total_questions})
    session['game_history'] = game_history
    session.modified = True
    #Added a data from questions results compiled to show results with result page
    return render_template('result.html', 
                           final_score=final_score, 
                           total_questions=total_questions,
                           summary=all_question_results) # Added summary data here


if __name__ == '__main__':
    app.run(debug=True)