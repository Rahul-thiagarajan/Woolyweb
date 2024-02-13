from flask import Flask, render_template,request
import json;
import pymysql
import yagmail
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
    s="select processing_access from farmers where fid="+str(Farmerid)+";"
    cur.execute(s)
    if(cur.fetchall()[0][0].lower()=="n"):
        return render_template('personal_details_dashboard.html',value="pn",Fid=Farmerid)
    return render_template('personal_details_dashboard.html',value="py",Fid=Farmerid)

@app.route('/Processing_details_change',methods=["POST","GET"])
def processing_details_change():
    obj=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur=obj.cursor()
    if(request.method=="POST"):
        if('requesting_processing' in request.form and request.form['requesting_processing'] == 'y'):
            a="Update farmers set processing_access='y' where fid="+str(Farmerid)+";"
            cur.execute(a)
            obj.commit()
            return render_template('personal_details_dashboard.html',value="py",Fid=Farmerid)
        else:
            a="Update farmers set processing_access='n' where fid="+str(Farmerid)+";"
            cur.execute(a)
            obj.commit()
            return render_template('personal_details_dashboard.html',value="pn",Fid=Farmerid)
@app.route('/inventory',methods=["POST","GET"])
def inventory():
    con2=pymysql.connect(user="root",host="localhost",password="abcd",database="woolyweb")
    cursorob2=con2.cursor()
    cursorob2.execute("select inventory_access from farmers where fid=%s",Farmerid)
    choice=cursorob2.fetchone()[0]
    if(choice=='y'):
        con=pymysql.connect(user="root",host="localhost",password="abcd",database="inventory")
        cursorob=con.cursor()
        cursorob.execute("select name,address,city,state,max_quantity,cost_per_day from inventory_details")
        all_inven=cursorob.fetchall()
        jon= [{"name": d[0], "address": d[1], "city": d[2], "state": d[3], "max_quantity": d[4], "cost_per_day": d[5]} for d in all_inven]
        jon2=json.dumps(jon)
        return render_template('personal_details_dashboard.html',inven=jon2,value="pz",Fid=Farmerid)
    else:
        return render_template('personal_details_dashboard.html',value="pz2",Fid=Farmerid)
@app.route('/inventory_access_change',methods=["POST","GET"])
def inventory_access_change():
    con=pymysql.connect(user="root",host="localhost",password="abcd",database="woolyweb")
    cursorob=con.cursor()
    cursorob.execute("select inventory_access from farmers where fid=%s",Farmerid)
    status=cursorob.fetchone()[0]
    if(status=='n'):
        cursorob.execute("update farmers set inventory_access='y' where fid=%s",Farmerid)
        con.commit()
    else:
        cursorob.execute("update farmers set inventory_access='n' where fid=%s",Farmerid)
        con.commit()
    return redirect('/inventory')

@app.route('/inventory_to_mail',methods=["POST","GET"])
def inventory_to_mail():
    inven_req=[request.form["name"],request.form["address"],request.form["city"],request.form["state"],request.form["max_quantity"],request.form["cost_per_day"]]
    con1=pymysql.connect(user="root",host="localhost",password="abcd",database="woolyweb")
    con2=pymysql.connect(user="root",host="localhost",password="abcd",database="inventory")
    cursorob1=con1.cursor()
    cursorob2=con2.cursor()
    cursorob1.execute("select fname,no_of_sheeps,phone_number from farmers where fid=%s",Farmerid)
    mail_content1=cursorob1.fetchone()
    cursorob2.execute("select name,email from inventory_details where name=%s and address=%s and city=%s and state=%s and max_quantity=%s and cost_per_day=%s",inven_req)
    mail_content2=cursorob2.fetchone()
    print(type(mail_content1[1]),type(mail_content1[2]))
    yag = yagmail.SMTP('woolywebonline@gmail.com', 'mqiglhdbgnmjneya')
    yag.send(
    to=mail_content2[1],
    subject='Request for Inventory',
    contents="Hi " +mail_content2[0]+","+"\n"+"A farmer has requested your inventory service,"+"\n\n"+"FARMER NAME: "+mail_content1[0]+"\n"+"NO. SHEEPS OWNED: "+str(mail_content1[1])+"\n"+"CONTACT INFO: "+mail_content1[2]
)
    return "<h1 style='text-align:center;'>MESSAGE SENT SUCCESSFULLY</h1>"



# @app.route('/help')
# def help():
#     return render_template('help.html')

# if __name__ == '__main__':
#     app.run(debug=True)