from flask import Flask, redirect , render_template,url_for,request
import cx_Oracle
import datetime
x = datetime.datetime.now()
con = cx_Oracle.connect('system/1234@localhost:1521')
cursor = con.cursor()
cursor.execute('SELECT CAST(ID AS VARCHAR2(4)) , TYPE , PRICE,PRICE-PRICE*REDUCTION,REDUCTION FROM PRODUCTS') 
tab = []
tab2 = []
liked_tab = []
for row in cursor:
    tab.append(row)

app = Flask(__name__)
app.config['SECRET_KEY']='QFVKEBR392RIR2NF2DL'
items = []
@app.route('/')
def default():
    return redirect('/home')

cursor1 = con.cursor()
cursor1.execute('SELECT EMAIL, PASSWORD FROM CLIENT')
for row in cursor1:
    tab2.append(row)


@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]        
        result = (email,password)
        if result not in tab2:
            cursor2 = con.cursor()
            sql = f"INSERT INTO CLIENT(EMAIL,PASSWORD) VALUES('{email}','{password}')"
            cursor2.execute(sql)
            con.commit()
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html',products = tab)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/card')
def card():
    return render_template('card.html',items=items)

@app.route('/liked')
def liked():
    return render_template('liked.html',products=liked_tab)

@app.route('/add/<int:id>')
def add(id):
    global x
    x = datetime.datetime.now()
    c = x.strftime("%A")
    items.append(tab[id-1])
    return redirect(url_for('products'))

@app.route('/liked/<int:id>')
def add_liked(id):
    if tab[id-1] not in liked_tab:
        liked_tab.append(tab[id-1])
    return redirect(url_for('products'))
                    
@app.route('/cancel/<int:id>')
def cancel(id):
    items.remove(tab[id-1])
    return redirect(url_for('card'))

if __name__=="__main__":
    app.run(debug=True)