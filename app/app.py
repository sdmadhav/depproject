import re
from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
from datetime import date
import mysql.connector
from mysql.connector import errorcode

config = {
    "apiKey": "AIzaSyDrdiYaeeC_kFwgiR27apzWhX-dzoacOCI",
    "authDomain": "indent-for-purchase.firebaseapp.com",
    "projectId": "indent-for-purchase",
    "storageBucket": "indent-for-purchase.appspot.com",
    "messagingSenderId": "655214437659",
    "appId": "1:655214437659:web:61c24f217752a9358a1fbe",
    "measurementId": "G-5JPWPNQ52F",
    "databaseURL": "https://indent-for-purchase-default-rtdb.asia-southeast1.firebasedatabase.app/"
}



# Construct connection string

# try:
#    cnx = mysql.connector.connect(user="depy9", password="PASSword@123", host="dep.mysql.database.azure.com", port=3306, database="geeklogin", ssl_ca="C:\\Users\\2019c\\Downloads\\DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
#   #  conn = mysql.connector.connect(**config)
#    print("Connection established")
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with the user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cursor = cnx.cursor()

#   # Drop previous table of same name if one exists
# #   cursor.execute("DROP TABLE IF EXISTS accounts;")
# #   print("Finished dropping table (if existed).")

#   # Create table
# #   cursor.execute("CREATE TABLE accounts (id int AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50),password VARCHAR(50),email VARCHAR(100));")
# #   print("Finished creating table.")

# #   # Insert some data into table
# #   cursor.execute("INSERT INTO accounts VALUES (NULL, %s, %s, %s);", ("sahdev","sahdev","sahdev@gmail.com"))
# #   print("Inserted",cursor.rowcount,"row(s) of data.")
  

#   # Cleanup
#   cnx.commit()
#   cursor.close()
#   cnx.close()
#   print("Done.")

# Store this code in 'app.py' file


app = Flask(__name__)

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app.secret_key = 'your secret key'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'UMAkashi@123'
# app.config['MYSQL_DB'] = 'geeklogin'
# # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# mysql = MySQL(app)


@app.route('/myapplications/<username>')
def myapplications(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            # print(i[1]['user'])
            if(i[1]["user"]==username):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                if(i[1]["statusA1"]=="false" and i[1]["statusR1"]=="false"):
                    mydic1.append("Pending by level 1")
                elif(i[1]["statusR1"]=="true"):
                    mydic1.append("Rejected by level 1")
                elif(i[1]["statusR2"]=="false" and i[1]["statusA2"]=="false"):
                    mydic1.append("Pending by level 2")
                elif(i[1]["statusR2"]=="true"):
                    mydic1.append("Rejected by level 2")
                elif(i[1]["statusR3"]=="false" and i[1]["statusA3"]=="false"):
                    mydic1.append("Pending by level 3")
                elif(i[1]["statusR3"]=="true"):
                    mydic1.append("Rejected by level 3")
                elif(i[1]["statusR4"]=="false" and i[1]["statusA4"]=="false"):
                    mydic1.append("Pending by level 4")
                elif(i[1]["statusR4"]=="true"):
                    mydic1.append("Rejected by level 4")
                elif(i[1]["statusR4"]=="false" and i[1]["statusA4"]=="true"):
                    mydic1.append("Your Application is approved")
                mydic.append(mydic1)
                j=j+1
    except:
        pass
    # return render_template("indenterDashboard.html", parent_list=mydic)
    return render_template("sakhd.html", parent_list=mydic)



@app.route('/approversP1/<username>')
def approversP1(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA1"]=="false" and i[1]["statusR1"]=="false"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1
    except:
        pass
    return render_template("SupdtPending1.html", parent_list=mydic)

@app.route('/approversP2/<username>')
def approversP2(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA1"]=="true" and i[1]["statusA2"]=="false" and i[1]["statusR2"]=="false"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1

    except:
        pass
    return render_template("SupdtPending2.html", parent_list=mydic)

@app.route('/approversP3/<username>')
def approversP3(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA2"]=="true" and i[1]["statusA3"]=="false" and i[1]["statusR3"]=="false"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                
                mydic.append(mydic1)

            j=j+1
    except:
        pass
    return render_template("SupdtPending3.html", parent_list=mydic)

@app.route('/approversP4/<username>')
def approversP4(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA3"]=="true" and i[1]["statusA4"]=="false" and i[1]["statusR4"]=="false"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1

    except:
        pass
    return render_template("SupdtPending4.html", parent_list=mydic)

@app.route('/approversA1/<username>')
def approversA1(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA1"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1
    except:
        pass
    return render_template("SupdtApproved1.html", parent_list=mydic)

@app.route('/approversA2/<username>')
def approversA2(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA2"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1
    except:
        pass
    return render_template("SupdtApproved2.html", parent_list=mydic)

@app.route('/approversA3/<username>')
def approversA3(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA3"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                
                mydic.append(mydic1)

            j=j+1
    except:
        pass
    return render_template("SupdtApproved3.html", parent_list=mydic)

@app.route('/approversA4/<username>')
def approversA4(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusA4"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1

    except:
        pass
    return render_template("SupdtApproved4.html", parent_list=mydic)


@app.route('/approversR1/<username>')
def approversR1(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusR1"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1
    except:
        pass
    return render_template("SupdtRejected1.html", parent_list=mydic)

@app.route('/approversR2/<username>')
def approversR2(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusR2"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1

    except:
        pass
    return render_template("SupdtRejected2.html", parent_list=mydic)

@app.route('/approversR3/<username>')
def approversR3(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusR3"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)

            j=j+1
    except:
        pass
    return render_template("SupdtRejected3.html", parent_list=mydic)

@app.route('/approversR4/<username>')
def approversR4(username):
    try:
        todo = db.child("form").get()
        jsondata = todo.val()
        mydic = []
        j = 1
        for i in jsondata.items():
            mydic1=[]
            if(i[1]["statusR4"]=="true"):
                mydic1.append(j)
                mydic1.append(i[0])
                mydic1.append(i[1]["date"])
                mydic.append(mydic1)
                j=j+1
    except:
        pass
    return render_template("SupdtRejected4.html", parent_list=mydic)

@app.route('/approver1Preview/<appId>')
def approver1applicationReview(appId):
    todo = db.child("form").child(appId).get()
    dict1=todo.val()
    dict1["appId"]=appId
    return render_template("approver1Preview.html", dict_item=dict1)

@app.route('/approver2Preview/<appId>')
def approver2applicationReview(appId):
    todo = db.child("form").child(appId).get()
    dict1=todo.val()
    dict1["appId"]=appId
    return render_template("approver2Preview.html", dict_item=dict1)

@app.route('/approver3Preview/<appId>')
def approver3applicationReview(appId):
    todo = db.child("form").child(appId).get()
    dict1=todo.val()
    dict1["appId"]=appId
    return render_template("approver3Preview.html", dict_item=dict1)

@app.route('/approver4Preview/<appId>')
def approver4applicationReview(appId):
    todo = db.child("form").child(appId).get()
    dict1=todo.val()
    dict1["appId"]=appId
    return render_template("approver4Preview.html", dict_item=dict1)

@app.route('/approver1Action/<appId>',methods=['GET', 'POST'])
def approver1Action(appId):
    if (request.form["submit"]=="approved"):
        db.child("form").child(appId).update({"statusA1": "true"})
    else:
        db.child("form").child(appId).update({"statusR1": "true"})
    return redirect(url_for('approversA1',username=session['username']))

@app.route('/approver2Action/<appId>',methods=['GET', 'POST'])
def approver2Action(appId):
    if (request.form["submit"]=="approved"):
        db.child("form").child(appId).update({"statusA2": "true"})
    else:
        db.child("form").child(appId).update({"statusR2": "true"})
    return redirect(url_for('approversA2',username=session['username']))
@app.route('/approver3Action/<appId>',methods=['GET', 'POST'])
def approver3Action(appId):
    if (request.form["submit"]=="approved"):
        db.child("form").child(appId).update({"statusA3": "true"})
    else:
        db.child("form").child(appId).update({"statusR3": "true"})
    return redirect(url_for('approversA3',username=session['username']))
@app.route('/approver4Action/<appId>',methods=['GET', 'POST'])
def approver4Action(appId):
    if (request.form["submit"]=="approved"):
        db.child("form").child(appId).update({"statusA4": "true"})
    else:
        db.child("form").child(appId).update({"statusR4": "true"})
    return redirect(url_for('approversA4',username=session['username']))

@app.route('/preview/<appId>')
def applicationReview(appId):
    todo = db.child("form").child(appId).get()
    return render_template("previewin.html", dict_item=todo.val())


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cnx = mysql.connector.connect(user="depy9", password="PASSword@123", host="dep.mysql.database.azure.com", port=3306, database="geeklogin", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = cnx.cursor()
        cursor.execute(
            'SELECT * FROM accounts WHERE username = %s AND password = %s;', (username, password))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            if (account[4]==0):
                return redirect(url_for('myapplications',username=session['username']))
            elif (account[4]==1):
                return redirect(url_for('approversP1',username=session['username']))
            elif (account[4]==2):
                return redirect(url_for('approversP2',username=session['username']))
            elif (account[4]==3):
                return redirect(url_for('approversP3',username=session['username']))                
            elif (account[4]==4):
                return redirect(url_for('approversP4',username=session['username']))
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html',msg=msg)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        userlevel=request.form['Category']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cnx = mysql.connector.connect(user="depy9", password="PASSword@123", host="dep.mysql.database.azure.com", port=3306, database="geeklogin", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = cnx.cursor()
        cursor.execute(
            'SELECT * FROM accounts WHERE username = %s AND password = %s;', (username, password))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute(
                'INSERT INTO accounts VALUES (NULL, %s, %s, %s,%s);', (username, password, email,int(userlevel)))
            # mysql.connection.commit()
            cnx.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


@app.route('/action/<username>', methods=['GET', 'POST'])
def basic(username):
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            dic = {}
            dic["user"] = username
            dic["Indenter"] = request.form['Indenter']
            dic["Budget"] = request.form['Budget']
            dic["Cost"] = request.form['Cost']
            dic["Item"] = request.form['Item']
            dic["Category"] = request.form['Category']
            dic["Budgetary_Approval"] = request.form['Budgetary_Approval']
            dic["is_space_ready"] = request.form['is_space_ready']
            dic["is_for_research"] = request.form['is_for_research']
            dic["GeM_Purchase"] = request.form['GeM_Purchase']
            dic["Mode_of_Enquiry"] = request.form['Mode_of_Enquiry']
            dic["no_of_quotations"] = request.form['no_of_quotations']
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            dic["date"] = d1
            dic["item_recom"] = request.form['item_recom']
            dic["quotation_no"] = request.form['quotation_no']
            dic["mode_of_payment"] = request.form['mode_of_payment']
            dic["delivery_period"] = request.form['delivery_period']
            dic["statusA1"]="false"
            dic["statusA2"]="false"
            dic["statusA3"]="false"
            dic["statusA4"]="false"
            dic["statusR1"]="false"
            dic["statusR2"]="false"
            dic["statusR3"]="false"
            dic["statusR4"]="false"
            dic["input0name0"] = request.form['input0name0']
            dic["input1name0"] = request.form['input1name0']
            dic["input2name0"] = request.form['input2name0']
            dic["input3name0"] = request.form['input3name0']
            dic["gate"]=request.form['gate']
            dic["tax"] = request.form['tax']
            dic["total"] = request.form['total']
            db.child("form").push(dic)
            todo = db.child("form").get()
            print(todo)
            to = todo.val()
            return render_template('previewin.html', dict_item=dic)
        elif request.form['submit'] == 'delete':
            db.child("form").remove()
        return redirect(url_for('login'))
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
