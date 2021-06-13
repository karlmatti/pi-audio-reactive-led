from flask import Flask, render_template, request

import led
from microphone import hello, start_stream
import visualization

app = Flask(__name__)
state = {'isRunning': False}

def change_reaction(reaction):
    pass


def start():
    state['isRunning'] = True
    # Initialize LEDs
    led.update()
    print(hello())
    # Start listening to live audio stream
    start_stream(visualization.microphone_update)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        reaction = request.form['reaction']
        available_reactions = ['scroll', 'energy', 'spectrum']
        if reaction in available_reactions:

            if not state['isRunning']:
                start()
            change_reaction(reaction)
            return "You chose " + reaction + ", is_running=" + str(state['isRunning'])
        else:
            return "This kind of selection is not allowed!"

@app.route('/microphone', methods=['GET'])
def microphone():
    return "Microphone2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
