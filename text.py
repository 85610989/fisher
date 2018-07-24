from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/index', methods=['GET'])
def index_form():
    return '''<h1 style="color:skyblue">hello智鹏</h1>
				<center>
					<div>
						<h2 style="color:orange"><em>等额本息还款测算<em></h2>
								<form action="/index" method="post">
								<p>贷款金额（元）  <input name="username"></p>
								<p>月利率（%）  <input name="rate" type="number"></p>
								<p><button type="submit">查看还款计划表</button></p>
								</form>
					</div>
				    <div>
						<h2 style="color:orange"><em>先息后本还款测算<em></h2>
								<form action="/index" method="post">
								<p>贷款金额（元）  <input name="username"></p>
								<p>月利率（%）  <input name="rate" type="number"></p>
								<p><button type="submit">查看还款计划表</button></p>
								</form>
					</div>
					<div>
						<h2 style="color:orange"><em>等额本金还款测算</em></h2>
						<form action="/index" method="post">
						<p>贷款金额（元）  <input name="username"></p>
						<p>月利率（%）  <input name="rate" type="number"></p>
						<p><button type="submit">查看还款计划表</button></p>
						</form>
					</div>
					<div>
						<h2 style="color:orange"><em>等本等息还款测算</em></h2>
							<form action="/index" method="post">
							<p>贷款金额（元）  <input name="username"></p>
							<p>月利率（%）  <input name="rate" type="number"></p>
							<p><button type="submit">查看还款计划表</button></p>
							</form>
					</div>
				  </ul>
				</center>
			
			'''
			
@app.route('/index', methods=['POST'])
def index():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h1>请输入数据</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81,debug=True)
	
