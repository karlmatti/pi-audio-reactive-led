import led, microphone, visualization

from flask import Flask, render_template, request

app = Flask(__name__)
global is_running


def change_reaction(reaction):
    pass


def start():
    is_running = True
    # Initialize LEDs
    led.update()
    # Start listening to live audio stream
    microphone.start_stream(visualization.microphone_update)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        reaction = request.form['reaction']
        available_reactions = ['scroll', 'energy', 'spectrum']
        if reaction in available_reactions:

            if not is_running:
                start()
            change_reaction(reaction)
            return "You chose " + reaction + ", is_running=" + is_running
        else:
            return "This kind of selection is not allowed!"


if __name__ == '__main__':
    is_running = False
    app.run(host='0.0.0.0')
