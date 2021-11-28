from flask import *
from flask_pymongo import PyMongo


app = Flask(__name__)
# client = pymongo.MongoClient("mongodb+srv://pooja:Pooja2000@cluster0.krtlz.mongodb.net/detaisl?retryWrites=true&w=majority")
# db = client.get_database('total_records')
# records = db.register

mongo_client = PyMongo(app, uri="mongodb+srv://pooja:pooja2000@cluster0.krtlz.mongodb.net/total_records?retryWrites=true&w=majority")
db = mongo_client.db
records = db.register

@app.route("/")
def index():
    if 'username' in session:
        return 'You are logged as the following user:' +session['username']

    return render_template('index.html')

@app.route('/register')
def registerRoute():
    return render_template('register.html')


@app.route('/login',methods=['POST'])
def login():
    username=request.form.get("username")
    password=request.form.get("password")
    print(username,password)
    finding=records.find_one({"email":username,"password":password})
    if(finding):
        return render_template('dashboard.html')
    else:
        return " user not found"
    

@app.route('/login')
def reg():
    return render_template('login.html')

@app.route('/dashboard')
def dash():
    return render_template("dashboard.html")



@app.route('/register',methods=["GET","POST" ,])
def register():
    firstname=request.form.get("firstname")
    lastname=request.form.get("lastname")
    email=request.form.get("email")
    number=request.form.get("number")
    password=request.form.get("password")
    confirmPassword=request.form.get("confirmPassword")
    print(firstname,lastname,email,password,confirmPassword,number)
    records.insert_one({"email":email,"password":password,"firstname":firstname,"lastname":lastname,"number":number})
    return render_template('login.html')


@app.route('/forgotpassword')
def forgotpassword():
    return render_template("forgotpassword.html")

@app.route('/postpage',methods=['GET','POST'])
def blogpage():
     
    if(request.method=='POST'):
        if(request.form):
            print(dict(request.form))
            records.insert_one(dict(request.form))
            return "posted successfully"
        else:
           return "please fill all fields" 
    return render_template('blogpage.html')

@app.route('/blogsdashboard',methods=['GET'])
def dashboard():
    return render_template('blogsdashboard.html')


@app.route('/updatepage')
def update():
    return "update page"

@app.route('/deletepage')
def delete():
    return "Delete page"


if __name__=='__main__':
    app.secret_key='secretivekeyagain'
    app.run(debug=True)

 