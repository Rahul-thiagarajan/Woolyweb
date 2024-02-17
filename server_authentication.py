from flask import Flask, jsonify, render_template,session,request
import pymysql
from shared import *
import pymysql
import yagmail
list_min_max=[0,0]
#app = Flask(__name__)
farmers=[]
@app.route('/server_authentication',methods=["POST","GET"])
def server_authentication():
    if(request.method=="POST"):
        return render_template("server_authentication2.html")
    elif(request.method=="GET"):
        return redirect('/servers_login')
@app.route('/get_data')
def get_data():
    print(list_min_max)
    farmers.clear()
    obj13=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur13=obj13.cursor()
    cur13.execute("select fid,fname,age,no_of_sheeps,type_of_sheep,address,city,state from farmers where verification='n';")
    list_of_farmers_server_authentication=cur13.fetchall()
    for i in list_of_farmers_server_authentication:
        data = {'fid':i[0],'name':i[1],'age':i[2],'No_of_sheeps':i[3],'Type_of_sheep':i[4],'address':i[5],'city':i[6],'state':i[7]}
        farmers.append(data)
    return jsonify(farmers)
@app.route('/prices', methods=['POST'])
def get_price():
    list_min_max[0]=request.args.items("min-price")
    list_min_max[1]=request.args.items("max-price")
    print(list_min_max)
    return "SUCCESSFULLY UPDATED THE PRICES"
@app.route('/verify', methods=['POST'])
def verify():
    obj13=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur13=obj13.cursor()
    data = request.get_json()
    print(f"update farmers set verification='y' where fid={int(data['fid'])};")
    cur13.execute(f"update farmers set verification='y' where fid={int(data['fid'])};")
    obj13.commit()
    print("Done")
    return jsonify({"message": "Response recorded successfully"})
@app.route('/send_transport_mail',methods=["POST","GET"])
def send_tranport():
    return render_template('send_transport_mail.html')
@app.route('/to_driver',methods=["POST","GET"])
def to_driver():
    return render_template('loc.html')

@app.route('/toprint',methods=["POST","GET"])
def toprint():
    tid=1
    print(tid)
    print(request.form['lat'])
    print(request.form['long'])
    con=pymysql.connect(user="root",host="localhost",password="abcd",database="transport")
    curob=con.cursor()
    curob.execute("update transport_details set lat=%s,lon=%s where t_id=%s",(request.form['lat'],request.form['long'],tid))
    con.commit()
    return redirect('/to_driver')
    
@app.route('/to_map',methods=["POST","GET"])
def to_map():
    tid=request.form['tid']
    con=pymysql.connect(user="root",host="localhost",password="abcd",database="transport")
    curob=con.cursor()
    curob.execute("select lat,lon from transport_details where t_id=%s",tid)
    val=curob.fetchone()
    float_tuple = tuple(float(v) for v in val)
    lat=float_tuple[0]
    lon=float_tuple[1]
    print(lat,lon)
    return render_template('jsmaps.html',lat=lat,lon=lon);
@app.route('/to_mail',methods=["POST","GET"])
def to_mail():
    city=request.form['tcity']
    mail=request.form['tmail']
    link="http://127.0.0.1:5000/to_driver"
    yag = yagmail.SMTP('2022it0003@svce.ac.in', 'Rahulsai@2004')
    yag.send(
    to="2022it0121@svce.ac.in",
    subject='Request for Inventory',
    contents="Hi " +city+","+"\n"+"A farmer has requested your inventory service,"+"\n\n"+"FARMER NAME: "+link+"\n"+"NO. SHEEPS OWNED: "+city+"\n"+"CONTACT INFO: "+city
)
    return "<h1>mail has been sent</h1>"
'''if __name__ == '__main__':
    app.run(debug=True)'''
