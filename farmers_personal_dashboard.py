from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('personal_details.dashboard.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/help')
# def help():
#     return render_template('help.html')

# if __name__ == '__main__':
#     app.run(debug=True)