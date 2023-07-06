from flask import Flask, render_template, url_for, flash, redirect, request
from forms import BookForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd945cba4a6b3c7a43288ea10bc2e63d7'
proxied = FlaskBehindProxy(app)

@app.route("/")
def hello_world():
    bookform = BookForm()
    # if bookform.validate_on_submit():
    #     author = fbookform.author.data
    #     num_books = bookform.numBooks.data
    #     sorting = bookform.sorting.data
    
    return render_template('index.html', subtitle='Home Page', text='This is the home page', form=bookform)

# @app.route("/update_server", methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         repo = git.Repo('/home/Registation/Registration')
#         origin = repo.remotes.origin
#         origin.pull()
#         return 'Updated PythonAnywhere successfully', 200
#     else:
#         return 'Wrong event type', 400

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit(): # checks if entries are valid
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home')) # if so - send to home page
#     return render_template('register.html', title='Register', form=form)


@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")