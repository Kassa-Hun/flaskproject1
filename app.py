from flask import Flask, render_template, request, redirect, url_for, flash,session
app=Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/')
def index():
    return 'Hello world!' 
@app.route('/hello/<name>')
def  hello(name):
    if name != 'admin':
        flash('You are not authorized to access this page.', 'error')
        return redirect(url_for('index'))
    session['username']=name
    return render_template('hello.html', name=session['username']) 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)