from flask import Flask, render_template
import pymysql
from shared import *
@app.route('/farmers_dashboard_home/<id>')
def farmers_dashboard_home(id):
    global Farmerid
    Farmerid=id
    return render_template('personal_details_dashboard.html',value="h",Fid=Farmerid)

@app.route('/Personal_details')
def personal_details():
    obj=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur=obj.cursor()
    s="Select * from farmers where fid="+str(Farmerid)+";"
    cur.execute(s)
    farmersfield=["ID","NAME","AGE","ADDRESS","CITY","STATE","PHONE NUMBER","AADHAR NUMBER","TYPE OF SHEEP","NO OF SHEEP","INVENTORY ACCESS","VERFICATION","PROCESSING ACCESS","GENDER"]
    return render_template('personal_details_dashboard.html',value="pd",farmersData=cur.fetchall()[0],field=farmersfield,Fid=Farmerid)
@app.route('/Processing_details')
def processing_details():
    obj=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur=obj.cursor()
    s="select processing from farmers where fid="+str(Farmerid)+";"
    cur.execute(s)
    if(cur.fetchall()[0][0]=="n"):
        return render_template('personal_details_dashboard.html',value="pn",Fid=Farmerid)
    return render_template('personal_details_dashboard.html',value="py",Fid=Farmerid)
# @app.route('/help')
# def help():
#     return render_template('help.html')

# if __name__ == '__main__':
#     app.run(debug=True)