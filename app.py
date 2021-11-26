from flask import Flask , render_template,url_for,request,session,redirect
import pymongo


app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://pooja:Pooja2000@cluster0.krtlz.mongodb.net/detaisl?retryWrites=true&w=majority")
db = client.get_database('total_records')
records = db.register

@app.route("/")
def index():
    if 'username' in session:
        return 'You are logged as the following user:' +session['username']

    return render_template('index.html')

@app.route("/register")
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
    password=request.form.get("password")
    confirmPassword=request.form.get("confirmPassword")
    print(firstname,lastname,email,password,confirmPassword)
    records.insert_one({"email":email,"password":password,"firstname":firstname,"lastname":lastname})
    return render_template('login.html')



if __name__=='__main__':
    app.secret_key='secretivekeyagain'
    app.run(debug=True)

