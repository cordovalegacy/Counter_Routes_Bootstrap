from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = 'this is a secret key for the counter assignment'


@app.route('/')
def index():
    if 'route_count' in session:
        session['route_count'] += 2
        print(session['route_count'])
    else:
        session['route_count'] = 0
        print('Nothing to see here')
    return render_template('index.html', requested_count = session['route_count'])


@app.route('/countform', methods=['POST'])
def count_form():
        session['route_count'] += int(request.form['counter']) - 2
        return redirect('/')

@app.route('/countbutton', methods=['POST'])
def count_button():
    session['route_count'] += 2 -2
    return redirect('/')


@app.route('/destroy_session')
def reset_count():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
