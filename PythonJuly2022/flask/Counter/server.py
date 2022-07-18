from flask import Flask, render_template  

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return render_template('index.html') 

# @app.route('/session/')
# def session():
#     return 'session'
# if 'key_name' in session:
#     print('key exists!')
# else:
#     print("key 'key_name' does NOT exist")
# session.clear()		# clears all keys
# session.pop('key_name')		# clears a specific key


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

