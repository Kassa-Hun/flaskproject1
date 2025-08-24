from flask import Flask, render_template, request, redirect, url_for, flash
app=Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/')
def index():
    return 'Hello world!'  
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)