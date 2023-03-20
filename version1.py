from flask import Flask, render_template, url_for, request, flash , redirect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/uploads", methods=['POST','GET'])
def uploads():
    if request.method == 'POST':
        name = request.form['nm']
        number = request.form['num']
        text_file = open('TEXT/text.txt', "a+")
        text_file.write(f"Name: {name}    | Number: {number} \n")
        text_file.close()
        return '<h1> Form Submitted </h1>'
    return redirect(url_for('home'))

@app.route("/retrieve", methods=['POST','GET'])
def retrieve():
    if request.method == 'POST':
        file = request.form['fl']
        with open("TEXT/text.txt" , "r") as f:
            contents= f.read()
            #flash message
            #flash(f'The message is:  {contents}')
        return render_template('test.html',contents=contents)



if __name__ == "__main__":
    app.run(debug=True)

