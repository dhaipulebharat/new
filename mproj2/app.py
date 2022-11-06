from flask import Flask,render_template,request,jsonify,request,redirect,url_for

from gram import get_response
from gram1 import resp,resp1

app=Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("base.html")
@app.route("/success/<string:msg>/<string:msg1>/<string:msg2>")
def success(msg,msg1,msg2):
    return render_template("result.html",output=msg,output1=msg1,output2=msg2)

@app.route("/predict",methods=["GET","POST"])
def predict():
    unchck_ms=""
    if request.method=="POST":
        message=request.form['msg']
        response= resp(message)
        response1= resp1(message)
    return redirect(url_for("success",msg=message,msg1=response,msg2=response1))

if __name__ == "__main__":
    app.run(debug=True)





""" text=request.get_json().get("message")
    # TODO:check if text is valid
    response= get_response(text)
    message={"answer":response}
    return jsonify(message) """