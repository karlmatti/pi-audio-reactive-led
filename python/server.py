from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        # form_data = request.form
        return "request.form"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

