from flask import render_template, request
from application import app
from application.forms import BasicForm

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

    if len(first_name) == 0 or len(last_name) == 0:
        # if length of first/last name = 0 - show error message
        error = "Please supply both first and last name."
    else:
        return 'Thank you'

    return render_template('home.html', form=form, message=error)
# takes user to new page once required action is completed correctly



