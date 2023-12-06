from flask import Flask, redirect, render_template, url_for,request

app=Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome ...{} '.format(name)


@app.route('/')
def home():
    return render_template('login.html')



@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['nm']
        return redirect(url_for('success',name=username))
    else:
        username=request.args.get('nm')
        return redirect(url_for('success',name=username))

#http://localhost:6789/login2?nm=amitava
#http://localhost:6789/login2?nm=amitava&nm2=kolkata
#Query String
#?nm=amitava&nm2=kolkata

@app.route('/login2')
def onlyget():
    username=request.args.get('nm')
    addr=request.args.get('nm2')
    return "<h1>data returned by Get method for the user : {} and he stays in {}</h1>".format(username,addr)




if __name__=='__main__':
    app.run(debug=True)



