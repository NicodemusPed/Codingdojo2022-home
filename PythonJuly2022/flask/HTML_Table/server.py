from flask import Flask,  render_template 
app = Flask(__name__)



@app.route('/')
def index():
    
    return render_template( "index.html" )

@app.route( '/success' )
def success():
    return "Success"

@app.route( '/<x><int:x>' )
def hello( x,x ):
    return render_template( "lists.html", x=x, x=x)

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


    return render_template("lists.html", users = user_info)



if __name__=="__main__": 
        app.run(debug=True)