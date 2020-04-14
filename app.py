from flask import Flask, render_template, request
import lightLevels

app = Flask(__name__)

@app.route('/')
def get_func():
    if request.method == 'GET':
        lightLevels.low_1()
        return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post_func():
    if request.method == 'POST':
        lightLevels.high_2()
        return render_template('post.html')

if __name__ == '__main__':
    app.run()
