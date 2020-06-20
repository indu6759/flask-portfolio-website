from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    # print(url_for('static',filename='favicon.ico'))
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_contact(data):
    content=f"name={data['name']}#email={data['email']}#subject={data['subject']}#message={data['message']} \n"   
    file_reader=open("database.txt","a")
    file_reader.write(content)
    file_reader.close()

def write_contact_csv(data):
    with open('database.csv', newline='', mode='a') as file_reader2:
        name=data['name']
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(file_reader2,  delimiter=',' , quotechar='"' ,  quoting=csv.QUOTE_MINIMAL)  
        csv_writer.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])

def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_contact_csv(data)
            # print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong!!'
