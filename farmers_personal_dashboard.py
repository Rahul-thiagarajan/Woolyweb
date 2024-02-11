from flask import Flask, render_template
import pymysql
from shared import *
@app.route('/farmers_dashboard_home/<value>')
def farmers_dashboard_home(value):
    global Farmerid
    Farmerid=value
    return render_template('personal_details_dashboard.html',value="h")

@app.route('/Personal_details')
def personal_details():
    obj=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur=obj.cursor()
    s="Select * from farmers where fid="+str(Farmerid)+";"
    cur.execute(s)
    farmersfield=["ID","NAME","AGE","ADDRESS","CITY","STATE","PHONE NUMBER","AADHAR NUMBER","TYPE OF SHEEP","NO OF SHEEP","INVENTORY ACCESS","VERFICATION","PROCESSING ACCESS","GENDER"]
    return render_template('personal_details_dashboard.html',value="pd",farmersData=cur.fetchall()[0],field=farmersfield)

# @app.route('/help')
# def help():
#     return render_template('help.html')

# if __name__ == '__main__':
#     app.run(debug=True)