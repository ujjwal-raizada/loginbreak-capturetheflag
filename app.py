# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/success')
def success():
    return render_template('welcome.html')  # render a template

@app.route('/creds')
def crack():
    return render_template('creds.html')  # render a template


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'ujjwalrox' or request.form['password'] != 'crux':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
