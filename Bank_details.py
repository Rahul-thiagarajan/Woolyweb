import pymysql
from en_de import *
from flask import Flask,render_template,url_for,request,redirect,session
import json
from shared import*
x_bank=["bank name","ifsc code","acc number"]
@app.route("/submit_bank",methods=["POST","GET"])
def submit_bank():
    if(request.method=="POST"):
        dic={}
        for i in x_bank:
            dic[i]=request.form[i]
        return redirect(url_for("complete_bank",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return "<H1 style='font-family:arial;text-align:center;color:red;'>YOU CANNOT DIRECTLY ACCESS THIS PAGE</H1>";
r_bank=[]
@app.route("/complete_bank/<a>",methods=["POST","GET"])
def complete_bank(a):
    if (request.method=="POST"):
        lst=[]
        obj2012=pymysql.connect(host="localhost",user="root",database="woolyweb",password="2theeran7")
        cur2012=obj2012.cursor()
        cur2012.execute("Select fid from farmers;")
        lst=list(cur2012.fetchall())
        a=decrypt(a)
        a=json.loads(a)
        print(lst)
        for i in x_bank:
            r_bank.append(a[i])
        r_bank.append(lst[-1][0])
        cur2012.execute("select ifsc_code,account_number from account_details;")
        temp=cur2012.fetchall()
        
        if(len(r_bank[1])!=12):
            return "<h1>REGISTRATION UNSUCCESSFUL..!!<h1><br><h1>INVALID IFSC CODE<h1>"
        if(not r_bank[2].isdigit()):
            return "<h1>REGISTRATION UNSUCCESSFUL..!!<h1><br><h1>INVALID ACCOUNT NUMBER<h1>"
        if(len(r_bank[2])!=15):
            return "<h1>REGISTRATION UNSUCCESSFUL..!!<h1><br><h1>INVALID ACCOUNT NUMBER<h1>"
        if(r_bank[1] in [x[0] for x in temp]):
            return "<h1>REGISTRATION UNSUCCESSFUL..!!<h1><br><h1>THIS IFSC IS ALREADY REGISTERED<h1>"
        if(r_bank[2] in [y[1] for y in temp]):
            return "<h1>REGISTRATION UNSUCCESSFUL..!!<h1><br><h1>THIS ACCOUNT NUMBER IS ALREADY REGISTERED<h1>"
        try:
            cur2012.execute("Insert into account_details(bank_name,ifsc_code,account_number,fid) values"+str(tuple(r_bank))+";")
        except Exception as e:
            return "WEBSITE FAILED TO LOAD PLEASE TRY AGAIN" + e
        obj2012.commit()
        return redirect(url_for('photo_upload'),code=307)
    elif(request.method=="GET"):
        return redirect('/')

'''if __name__=="__main__":
    app.run(debug=True)'''

