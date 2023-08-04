
from flask import Flask,render_template,request
import ibm_db

app=Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;USERNAME=gbr27924;PASSWORD=ZqEWVYOYyt88NRns;SECURITY=ssl;SSLSERVICECERTIFICATE=DigiCertGlobalRootCA.crt;PORT=32733;",'','')
print(ibm_db.active(conn))


@app.route("/")
def index():
     return render_template("index.html")


@app.route("/contact")
def contact():
     return render_template("contact.html")


@app.route("/login",methods=["GET","POST"])
def login():
     if request.method=="POST":
          uname=request.form['username']
          pword=request.form['password']
          print(uname,pword)
          sql='SELECT * FROM REGISTER_FDP WHERE USERNAME=?'
          stmt=ibm_db.prepare(conn,sql)
          ibm_db.bind_param(stmt,1,uname)
         # ibm_db.bind(stmt,2,pword)
          ibm_db.execute(stmt)
          out=ibm_db.fetch_assoc(stmt)
          print(out)
     return render_template("login.html")


if __name__=="__main__":
    app.run(debug=True)