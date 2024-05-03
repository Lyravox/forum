# app.py

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('home.html', messages=messages)

@app.route('/post_message', methods=['POST'])
def post_message():
    text = request.form['message']
    messages.append(text)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)