from flask import Flask,  render_template 
app = Flask(__name__)



@app.route('/')
def checker_board():
    
    return render_template("index.html", times=num_of_hellos, list=student_info, height=height)


if __name__=="__main__": 
        app.run(debug=True)