from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = dict(name='Chris', email='wcbeard10@gmail.com')
    return render_template('index.html',
        user=user)

# from flask import Flask, jsonify, render_template, request
# app = Flask(__name__)
# app.debug = True

# # @app.route('/_add_numbers')
# # def add_numbers():
# #     """Add two numbers server side, ridiculous but well..."""
# #     a = request.args.get('a', 0, type=int)
# #     b = request.args.get('b', 0, type=int)
# #     return jsonify(result=a + b)


# @app.route('/')
# def index():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)