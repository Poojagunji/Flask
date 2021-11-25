from flask import Flask , render_template,url_for,request,session,redirect
import pymongo
import bcrypt

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://pooja:Pooja2000@cluster0.krtlz.mongodb.net/detaisl?retryWrites=true&w=majority")
db = client.get_database('total_records')
records = db.register
# url mongodb+srv://pooja:Pooja2000@cluster0.krtlz.mongodb.net/detaisl?retryWrites=true&w=majority
# app.config['MONGO_DBNAME']='detaisl'
# app.config['MONGO_URI']='mongodb+srv://pooja:Pooja2000@cluster0.krtlz.mongodb.net/detaisl?retryWrites=true&w=majority'
# mongo=PyMongo(app)

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
        return "data found"
    else:
        return "not found"
    # users = mongo.db.users
    # login_user = users.find_one({'name' : request.form['username']})

    # if login_user:
    #     if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
    #         session['username'] = request.form['username']
    #         return redirect(url_for('index'))
    # return 'Invalid username or password combination'
    return ""


@app.route('/register',methods=["GET","POST"])
def register():
    firstname=request.form.get("firstname")
    lastname=request.form.get("lastname")
    email=request.form.get("email")
    password=request.form.get("password")
    confirmPassword=request.form.get("confirmPassword")
    print(firstname,lastname,email,password,confirmPassword)

    records.insert_one({"email":email,"password":password,"firstname":firstname,"lastname":lastname})

    
    # if (validateEmail(email) and  password_check(password) and check_phonenumber(phonenumber)):
    #     register.insert_one({"email":email,"phone_no":phonenumber,"user_name":username,"password":password})
    #     # print(username,password,phonenumber,email)
    #     return render_template("login.html")
    # else:
    #     return render_template("error.html")

    return render_template('login.html')



if __name__=='__main__':
    app.secret_key='secretivekeyagain'
    app.run(debug=True)

