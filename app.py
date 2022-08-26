from flask import Flask,render_template
app=Flask(__name__,template_folder='templates')
@app.route('/Adarsh')
def showAdarsh():
    return render_template('adarsh.html')
app.run(debug=True)
