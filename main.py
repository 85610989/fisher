from flask import  Flask



app=Flask(__name__)
app.config.from_object('config')

@app.route('/hello/')
def hello():
    return 'hello world'


app.run(debug=app.config['DEBUG'],host='0.0.0.0',port=81)