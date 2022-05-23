from flask import Flask, render_template, request, redirect, \
url_for, flash, make_response, session
# from flask import Flask, render_template, redirect, request, session
app = Flask (__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    if 'key_name' in session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")


    return render_template('count.html') 

#...
@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))

@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'
#...


if __name__ == '__main__':
    app.run(debug=True)