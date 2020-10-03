from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) # initiating app

# @app.route('/')
# @app.route('/<username>')
# @app.route('/<username>/<int:post_id>') # creates url
# def hello_world(username=None, post_id=None):
#     return render_template('./index.html', username=username, post_id=post_id)


@app.route('/')
def hello_world():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET']) # get - save data
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # getting all form info as dictionary
            print(data)
            write_to_csv(data)
            return redirect('/thank_you.html ')
        except:
            return 'file is now saved'
    else:
        return 'smth is wrong'

def write_to_csv(data): 
    with open('db.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # fieldames = ['email', 'subject', 'message']
        csv_writer = csv.writer(csvfile, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# def write_to_file(data):
#     with open('db.txt', 'a') as f:
#         for key, val in data.items():
#             f.write(f'{key}: {val}\n')
#         f.write('\n')



# @app.route('/works.html')
# def works():
#     return render_template('./works.html')

# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('./components.html')
