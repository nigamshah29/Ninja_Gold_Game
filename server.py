from flask import Flask, render_template, redirect, session, flash, request

app=Flask(__name__)
app.secret_key='some random key74'
import random

@app.route('/')
def index():
    if 'history' not in session:
        session['total_gold'] = 0
        session['history'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        farm_gold = random.randrange(10,21)
        session['total_gold'] += farm_gold
        history = session['history']
        history.insert(0,'Earned ' + str(farm_gold) + ' golds from the farm!')
        session['history'] = history
    elif request.form['building'] == 'cave':
        cave_gold = random.randrange(5,11)
        session['total_gold'] += cave_gold
        history = session['history']
        history.insert(0,'Earned ' + str(cave_gold) +  ' golds from the cave!')
        session['history'] = history
    elif request.form['building'] == 'house':
        house_gold = random.randrange(2,6)
        session['total_gold'] += house_gold
        history = session['history']
        history.insert(0,'Earned ' + str(house_gold) +  ' golds from the house!')
        session['history'] = history
    elif request.form['building'] == 'casino':
        casino_gold = random.randrange(-50,51)
        session['total_gold'] += casino_gold
        if casino_gold < 0:
            history = session['history']
            history.insert(0,'Entered a casino and lost ' + str(casino_gold) +  ' golds...Ouch...')
            session['history'] = history
        elif casino_gold > 0:
            history = session['history']
            history.insert(0,'Earned ' + str(casino_gold) +  ' golds from the casino!')
            session['history'] = history
    return redirect('/')


@app.route('/playAgain', methods=['POST'])
def playAgain():
    session.clear()
    return redirect('/')


app.run(debug=True)
