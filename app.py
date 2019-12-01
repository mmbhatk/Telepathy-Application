import os
# We import 'Flask' for creating a flask application,
# 'session' to store and retrieve session variables in every view
# 'render_template' to render a HTML template with the given context variables
# 'url_for' to get the URL corresponding to a view
# 'redirect' to redirect to a given URL
# 'request' to access the request object which contains the request data
# 'flash' to display messages in the template
import sqlite3
import ast
from flask import Flask, session, render_template, url_for, redirect, request, flash


# Create a flask app and set its secret key

app = Flask(__name__)
app.secret_key = os.urandom(24)


# 'questions' dictionary contains 5 questions and their answers.
# The questions are numbered from 1 to 5

sender_questions = { "1" : { "question" : "What is this colour name?", "answer" : "Barack Obama", "option": {"Black", "White", "Blue", "Red", "Green"}},
              "2" : { "question" : "What do you feel when you are looking at this colour?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}}}
              # "3" : { "question" : "Choose any below item that you think is related with this picture.", "answer" : "Barack Obama", "option": {"Girl/Sea/Bicycle/Flower/Tree", "Fire/War/Soldier", "Sun/Old man/Car", "Window/Hotel/People"}},
              # "4" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "5" : { "question" : "What is this shape name?", "answer" : "New Delhi", "option" : {"Triangle", "Oval", "Cube", "Heart", "Arrow"}},
              # "6" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "7" : { "question" : "What is this number?", "answer" : "New Delhi", "option" : {"One", "Two", "Three", "Four", "Five"}},
              # "8" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "9" : { "question" : "Choose any below item that you think is related with this text.", "answer" : "New Delhi", "option" : {"Rain/Cloud", "Fire/War/Soldier", "Sun/Old man/Car", "Window/Hotel/People"}},
              # "10" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "11" : { "question" : "Choose any below item that you think is related with this text.", "answer" : "New Delhi", "option" : {"Bike/Book/Sandwich/Close shop", "Fire/War/Soldier", "Sun/Old man/Car", "Window/Hotel/People"}},
              # "12" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "13" : { "question" : "Choose any below item that you think is related with this Particular Name.", "answer" : "New Delhi", "option" : {"US Singer/Pop Star", "Fire/War/Soldier", "Sun/Old man/Car", "Window/Hotel/People"}},
              # "14" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "15" : { "question" : "Select the category that this name is belong to.", "answer" : "New Delhi", "option" : {"Country", "Actress", "Singer", "Family Member", "Artist"}},
              # "16" : { "question" : "What do you feel when you are looking at this picture?", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}}}

receiver_questions = { "1" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              "2" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}}}
              # "3" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "4" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "5" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "6" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "7" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "8" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "9" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "10" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "11" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "12" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "13" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "14" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}},
              # "15" : { "question" : "Select the strangest object that you find into your mind. If you received any of the below objects, select any one that is most close to your one.", "answer" : "Barack Obama", "option": {"Static vision", "Dynamic vision", "Color", "Words", "Did not receive anything"}},
              # "16" : { "question" : "Open your eyes. Please let us know what you have felt during the trail.", "answer" : "New Delhi", "option" : {"Positive", "Negative", "Lust", "No feeling change"}}}

sender_answers = []
receiver_answers = []
correct_answers = ['Color', '', 'Static vision', '', 'Static vision', '', 'Static vision', '', 'Dynamic vision', '', 'Dynamic vision', '', 'Static vision', '', 'Static vision', '']
num_ques = 2

# Route for the URL / accepting GET and POST methods
# We are using session variables to keep track of the current question
# the user is in and show him just that question even if he reloads the page
# or opens the page in a new tab.

@app.route('/')
def home():
   return render_template('first.html')

@app.route('/sender', methods=['GET', 'POST'])
def sender():
  global sender_answers
  if request.method == "POST":
    
    # The data has been submitted from the form via POST request.
    # Now we need to validate it.
    
    # entered_answer = request.form.get('answer', '')
    entered_answer = request.form.get('op')
    print("ENTERED: ", entered_answer)
    if not sender_answers and not entered_answer:
      con = sqlite3.connect("Telepathyapp.db")
      cursor = con.cursor()
      cursor.execute("INSERT INTO answers VALUES (?, ?)", (1, str(sender_answers)))
      con.commit()
    if entered_answer:
      try:
            con = sqlite3.connect("Telepathyapp.db")
            cursor = con.cursor()

            query = """SELECT * FROM answers WHERE ID=1"""
            cursor.execute(query)
            sender_answers = cursor.fetchall()
            sender_answers = ast.literal_eval((sender_answers[0][1]))
            sender_answers.append(entered_answer)

            query = """DELETE FROM answers WHERE ID=1"""
            cursor.execute(query)

            cursor.execute("INSERT INTO answers VALUES (?, ?)", (1, str(sender_answers)))
            con.commit()

            query = """SELECT * FROM answers"""
            cursor.execute(query)
            ans = cursor.fetchall()
            for row in ans:
              print("Row: ", row)

            print("Successfully committed to the database.")
      except:
          print("In except")

    
    if not entered_answer:
      flash("Please select an answer", "error") # Show error if no answer entered
    
    else:
      # The answer is correct. So set the current question to the next number
      session["current_question"] = str(int(session["current_question"])+1)
    
      if session["current_question"] in sender_questions:
        # If the question exists in the dictionary, redirect to the question
        redirect(url_for('sender'))
      
      else:
        # else redirect to the success template as the quiz is complete.
        compute()
        session["current_question"] = "1"
        return render_template("success.html")
  
  if "current_question" not in session:
    # The first time the page is loaded, the current question is not set.
    # This means that the user has not started to quiz yet. So set the 
    # current question to question 1 and save it in the session.
    session["current_question"] = "1"
  
  elif session["current_question"] not in sender_questions:
    # If the current question number is not available in the questions
    # dictionary, it means that the user has completed the quiz. So show
    # the success page.
    compute()
    session["current_question"] = "1"
    return render_template("success.html")
  
  # If the request is a GET request or the answer wasn't entered or the entered
  # answer is wrong, show the current questions with messages, if any.
  return render_template("quiz.html",
                         question=sender_questions[session["current_question"]]["question"],
                         options=sender_questions[session["current_question"]]["option"],
                         question_number=session["current_question"],
                         url = '/sender')


@app.route('/receiver', methods=['GET', 'POST'])
def receiver():
  global receiver_answers
  if request.method == "POST":
    
    # The data has been submitted from the form via POST request.
    # Now we need to validate it.
    
    # entered_answer = request.form.get('answer', '')
    entered_answer = request.form.get('op')
    print("ENTERED: ", entered_answer)
    if not receiver_answers and not entered_answer:
      con = sqlite3.connect("Telepathyapp.db")
      cursor = con.cursor()
      cursor.execute("INSERT INTO answers VALUES (?, ?)", (2, str(receiver_answers)))
      con.commit()
    if entered_answer:
      print("HERE")
      try:
            con = sqlite3.connect("Telepathyapp.db")
            cursor = con.cursor()

            query = """SELECT * FROM answers WHERE ID=2"""
            cursor.execute(query)
            receiver_answers = cursor.fetchall()
            receiver_answers = ast.literal_eval((receiver_answers[0][1]))
            receiver_answers.append(entered_answer)

            query = """DELETE FROM answers WHERE ID=2"""
            cursor.execute(query)

            cursor.execute("INSERT INTO answers VALUES (?, ?)", (2, str(receiver_answers)))
            con.commit()

            query = """SELECT * FROM answers"""
            cursor.execute(query)
            ans = cursor.fetchall()
            for row in ans:
              print("Row: ", row)

            print("Successfully committed to the database.")
      except:
          print("In except")

    
    if not entered_answer:
      flash("Please select an answer", "error") # Show error if no answer entered
    
    else:
      # The answer is correct. So set the current question to the next number
      session["current_question"] = str(int(session["current_question"])+1)
    
      if session["current_question"] in receiver_questions:
        # If the question exists in the dictionary, redirect to the question
        redirect(url_for('receiver'))
      
      else:
        # else redirect to the success template as the quiz is complete.
        compute()
        session["current_question"] = "1"
        return render_template("success.html")
  
  if "current_question" not in session:
    # The first time the page is loaded, the current question is not set.
    # This means that the user has not started to quiz yet. So set the 
    # current question to question 1 and save it in the session.
    session["current_question"] = "1"
  
  elif session["current_question"] not in receiver_questions:
    # If the current question number is not available in the questions
    # dictionary, it means that the user has completed the quiz. So show
    # the success page.
    session["current_question"] = "1"
    return render_template("success.html")
  
  # If the request is a GET request or the answer wasn't entered or the entered
  # answer is wrong, show the current questions with messages, if any.
  return render_template("quiz.html",
                         question=receiver_questions[session["current_question"]]["question"],
                         options=receiver_questions[session["current_question"]]["option"],
                         question_number=session["current_question"],
                         url = '/receiver')

@app.route('/results')
def results():
  res = compute()
  score, percentage = res[0], res[1]
  return render_template('results.html', score = score, percentage = percentage)

def compute():
  print("In compute.")
  con = sqlite3.connect("Telepathyapp.db")
  cursor = con.cursor()
  
  query = """SELECT * FROM answers WHERE ID=1"""
  cursor.execute(query)
  sender_answers = cursor.fetchall()
  if sender_answers: sender_answers = ast.literal_eval((sender_answers[-1][1]))
  else: return
  
  query = """SELECT * FROM answers WHERE ID=2"""
  cursor.execute(query)
  receiver_answers = cursor.fetchall()
  if receiver_answers: receiver_answers = ast.literal_eval((receiver_answers[-1][1]))
  else: return
  
  print("OKAY, I AM IN COMPUTE")

  score = 0
  # for i in range(len(sender_answers)):
  for i in range(2):
    if correct_answers[i]: score += (correct_answers[i] == receiver_answers[i])
    else: score += (sender_answers[i] == receiver_answers[i])
  percentage = (score/16) * 100
  return (score, percentage)


# Runs the app using the web server on port 80, the standard HTTP port
if __name__ == '__main__':
  app.run(host="127.0.0.1", port = int("5000"), debug = True)