from flask import render_template
from flask import request
from application import app
from application.forms import BasicForm

from application.data_provider_service import DataProviderService
# instantiating an object of DataProviderService
DATA_PROVIDER = DataProviderService()


@app.route('/thursday')
def thursday():
    return render_template('thursday.html')

@app.route('/friday')
def friday():
    return render_template('friday.html')

@app.route('/practice')
def practice():
    return render_template('practice.html', title='Practice')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='Favourites', michellelist=['holidays', 'food', 'music'],
                           pamlist=['food', 'travel', 'piano'])



@app.route('/register', methods=['GET', 'POST'])
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
            new_person_id = DATA_PROVIDER.add_person(first_name, last_name)
            success = 'Person with ID' + str(new_person_id) + ' was created. Thank you!'
            return render_template('success.html', success_message=success)

#             # return 'Thank you'
#
#     return render_template('person.html', form=form, message=error)
# # takes user to new page once required action is completed correctly

@app.route('/people', methods=['GET'])
def get_people():
    all_people = DATA_PROVIDER.get_people()
    return render_template('people.html', title="People", people=all_people)