from flask import Flask, jsonify, render_template,session
import pymysql
from shared import *
#app = Flask(__name__)
farmers_marketplace = []
@app.route('/marketplace/<cust_username>',methods=["POST","GET"])
def marketplace(cust_username):
    global custUser
    custUser=cust_username
    if(request.method=="POST"):
        return render_template("marketplace.html")
    elif(request.method=="GET"):
        return redirect('/')

@app.route('/get_data_market')
def get_data_market():
    farmers_marketplace.clear()
    obj24 = pymysql.connect(host="localhost", user="root", password="abcd", database="woolyweb")
    cur24 = obj24.cursor()
    cur25 = obj24.cursor()
    cur24.execute("select link,farmers.fid from farmers, photos where farmers.fid = photos.fid and farmers.verification = 'y';")
    cur25.execute("select product_description, price from farmers, description where farmers.fid = description.fid and farmers.verification = 'y';")
    list_of_authenticated_farmers = list(cur24.fetchall())
    list_of_description = list(cur25.fetchall())
    data = []
    for i in range(len(list_of_authenticated_farmers)): 
        dic = {}
        dic['link'] = list_of_authenticated_farmers[i][0]
        dic['description'] = list_of_description[i][0]
        dic['price'] = list_of_description[i][1]
        dic['fid']= list_of_authenticated_farmers[i][1]
        data.append(dic)
    print(data)
    return jsonify(data)
@app.route('/checkout',methods=["POST","GET"])
def checkout():
    print("Ulle vaaa")
    if(request.method=="POST"):
        fid=int(request.form["farmer2"])
        stri='Select cust_address,cust_city,cust_state from general_customer where username="'+str(custUser)+'";'
        obj1=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
        obj2=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
        cursor=obj1.cursor()
        cursor.execute(stri)
        temp=cursor.fetchall()
        cus_add=str(temp[0][0])
        cus_city=str(temp[0][1])
        cus_state=str(temp[0][2])
        cursor2=obj2.cursor()
        dest_address=cus_add+","+cus_city+","+cus_state
        str2='Insert into orders(fid,custid,destaddress) values('+str(fid)+',"'+str(custUser)+'","'+dest_address+'");'
        cursor2.execute(str2)
        obj2.commit()
        return '<body><h1>Order placed successfully</h1><form action="/"><input type="submit" value="Go to Home"></form><body>'
    elif(request.method=="GET"):
        return redirect('/')
    
    
@app.route('/checkout2',methods=["POST","GET"])
def checkout2():
    if(request.method=="POST"):
        return render_template('checkout.html')
    elif(request.method=="GET"):
        return redirect('/')



'''if __name__ == '__main__':
    app.run(debug=True)'''
