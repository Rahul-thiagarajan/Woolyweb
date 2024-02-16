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
        
        return render_template('checkout.html')
    elif(request.method=="GET"):
        fid=request.form["farmer2"]
        print(fid)
        return "Order placed successfully"
    
    
@app.route('/checkout2',methods=["POST","GET"])
def checkout2():
    if(request.method=="POST"):
        return render_template('checkout.html')
    elif(request.method=="GET"):
        return redirect('/')



'''if __name__ == '__main__':
    app.run(debug=True)'''
