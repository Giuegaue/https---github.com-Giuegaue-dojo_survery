from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'S_Key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/survey', methods = ['POST'])
def survey_submit():
    print(request.form)

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    
    return redirect('/survey_info')

@app.route('/survey_info')
def survey_info():
    print(request.form)
    return render_template(
        'return.html',
        name = session['name'],
        location = session['location'],
        language = session['language'],
        comment = session['comment']
    )



if __name__ == "__main__":
    app.run(debug=True)