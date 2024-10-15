from flask import Flask, render_template, random, session, redirect, request

app = Flask(__name__)

@app.route('/')
def generate_number():
    return render_template('index.html')

def random_number():
    x = random.randint(1, 100)
    if x == request.form['number']:
        return redirect('/success')
    
    if x > request.form['number']:
        return redirect('/low')
    
    if x < request.form['number']:
        return redirect('/high')
    
@app.route('/low')
def low():
    return ('low.html')

@app.route('/high')
def high():
    return ('high.html')

@app.rout('/success')
def success():
    return ('success.html')

if __name__ == '__main__':
    app.run(debug=True)