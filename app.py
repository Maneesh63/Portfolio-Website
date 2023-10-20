from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '632765'
app.config['MYSQL_DB'] = 'folio'

app.secret_key='hello123s'

mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/light')
def light():
    return render_template('light.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name=request.form.get('name')
        iam=request.form.get('iam')

        if not name:
            error_message = "Name is required."
            return render_template('reg.html', error_message=error_message)
         
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO reg (name,iam) VALUES (%s, %s)',(name,iam))
        mysql.connection.commit()
        cur.close()

        success_message = "Registration successful."
        return render_template('home.html', success_message=success_message)
       
    return render_template('reg.html')




if __name__=='__main__':
    app.run(debug=True)