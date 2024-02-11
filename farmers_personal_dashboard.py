from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('personal_details_dashboard.html')

@app.route('/Personal_details')
def personal_details():
     obj7=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
     cur7=obj7.cursor()
     return render_template('personal_detail_dashboard.html',value="pd")

# @app.route('/help')
# def help():
#     return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)