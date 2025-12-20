from flask import Flask, render_template ,request, redirect,flash,get_flashed_messages
import sqlite3

def db():
    c=sqlite3.connect("players.db")
    cur=c.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS players(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT)
                ''')
    c.commit()
    c.close()
db()

app=Flask(__name__)
app.secret_key='supersecretkey123newkey456'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username= request.form['username']
        password=request.form['password']
        c=sqlite3.connect('players.db')
        cur=c.cursor()
        cur.execute('SELECT * FROM players WHERE username=? AND password=?',(username,password))
        user=cur.fetchone()
        c.close()
        if user:
            flash('login successful!','success')
            return redirect('/loading')
        else:
            flash("Wrong username or password",'error')
            return render_template('login.html', title='login', last_username=username)
    return render_template('login.html' ,title='login',last_username='')

@app.route('/signup', methods=['GET',"post"])
def signup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        c=sqlite3.connect('players.db')
        cur=c.cursor()
        cur.execute('SELECT * FROM players WHERE username=? OR email=?',(username,email))
        existing=cur.fetchone()
        if existing:
            flash('Username or email already exsists','error')
            c.close()
            return render_template('signup.html',title='signup')
        
        cur.execute('INSERT INTO players(username,email,password) VALUES(?,?,?)',(username,email,password))
        c.commit()
        c.close()
        flash('signup successfull! please login','success')
        return redirect('/login')
    return render_template('signup.html', title='signup')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)