from flask import Flask, render_template, request,session
import pymysql
from shared import *
@app.route('/product_description',methods=["POST","GET"])
def product_description():
    if(request.method=="POST"):
        return render_template('productinfo.html')
    elif(request.method=="GET"):
        return redirect('/farmer_check')

@app.route('/description_cost', methods=["POST","GET"])
def description_cost():
    if request.method == "POST":
        description_list=[]
        description_list.clear()
        obj222=pymysql.connect(host="localhost",user="root",database="woolyweb",password="2theeran7")
        cur222=obj222.cursor()
        cur222.execute("select fid from farmers;")
        fid_list_product_description=list(cur222.fetchall())
        description_list.append(fid_list_product_description[-1][0])
        description_list.append(request.form['desc_get'])
        description_list.append(request.form['cost_get'])
        if(not description_list[2].isdigit()):
            return "<h1>PLEASE ENTER A VALID COST</h1><br><h1>THE COST SHOULD ONLY CONTAIN NUMBERS</h1>"
        cur222.execute("Insert into description values"+str(tuple(description_list))+"")
        obj222.commit()
        obj223=pymysql.connect(host="localhost",user="root",database="woolyweb",password="2theeran7")
        cur223=obj223.cursor()
        cur223.execute("Select fid from farmers order by fid desc limit 1;")
        FARMER=cur223.fetchall()[0][0]
        x="<head><script>function home(){window.location.href='/'}</script></head><h1>REGISTERED SUCCESSFULLY</h1><br><br><h2>YOUR FARMER ID IS :"+str(FARMER)+"</h2><br><h2>PLEASE NOTE THIS FID IN A SAFE PLACE</h2><br><h2>YOU WILL NEED THIS FARMER ID WHILE LOGGING IN TO THE WEBSITE</h2><input type='button' value='Go to home page' onclick='home()'>"
        return x
    if(request.method=="GET"):
        return redirect('/farmer_check')