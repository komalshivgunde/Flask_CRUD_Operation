from flask import Flask, render_template,request,redirect
import pymysql

#create object of Flask class
app=Flask('__name__')
'''
@app.route('/')
def index():
    return "Hello from About page"

@app.route('/contact')
def contact_us():
    return "Hello from Contact page"
    '''
@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="select * from task"
        cu.execute(q)
        data=cu.fetchall()
        return render_template('dashboard.html',d=data)
    except Exception as e:
        return "Error"+e
    

@app.route('/create')
def create_data():
    return render_template('create.html')

@app.route('/store',methods=['POST'])
def store():
    
    x=request.form['ctitle']
    y=request.form['cdetail']
    z=request.form['cdate']
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="insert into task(title,detail,date) values('{}','{}','{}')".format(x,y,z)
        cu.execute(q)
        db.commit()
        return redirect('/')
    except Exception as e:
        return "Error"+e

         
    #return x+","+y+","+z
    
    #return "Data is stored"
@app.route('/delete/<rid>')
def delete(rid):
    db=pymysql.connect(host="localhost",user="root",password="",database="todo")
    cu=db.cursor()
    q="delete from task where id='{}'".format(rid)
    cu.execute(q)
    db.commit()
    return redirect('/')

@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="select * from task where id='{}'".format(rid)
        cu.execute(q)
        data=cu.fetchone()
        return render_template('edit_form.html',d=data)
    except Exception as e:
        return "Error"+e
    #return "record deleted successfully"
    #return "id to be deleted is"+rid

@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    ut=request.form['ctitle']
    udet=request.form['cdetail']
    ud=request.form['cdate']
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="update task SET title='{}',detail='{}',date='{}' where id='{}'".format(ut,udet,ud,rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
    except Exception as e:
        return "Error"+e

app.run(debug=True)