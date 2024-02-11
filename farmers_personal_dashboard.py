from flask import Flask, render_template
import pymysql
from shared import *
@app.route('/farmers_dashboard_home/<value>')
def farmers_dashboard_home(value):
    
    return render_template('personal_details_dashboard.html')

@app.route('/Personal_details')
def personal_details():
     return render_template('personal_details_dashboard.html',value="pd")

# @app.route('/help')
# def help():
#     return render_template('help.html')

# if __name__ == '__main__':
#     app.run(debug=True)