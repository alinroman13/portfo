from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("./index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)  

def write_to_file(data):
     with open('database.txt', 'a') as f: 
        email=data["email"]
        message=data["message"]
        subject=data["subject"]
        f.write(f"From:{email}\n Message:{message}\n Subject{subject}\n\n ")

def write_to_csv(data):
     with open('database.csv', 'a') as f2: 
        email=data["email"]
        message=data["message"]
        subject=data["subject"]
        csv_writer=csv.writer(f2, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)     
        csv_writer.writerow([email,message,subject])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
       try: 
           data= request.form.to_dict()
           write_to_csv(data)
           return redirect("thankyou.html")
       except:"did not save to database"     
    else:
        return "something went wrong"