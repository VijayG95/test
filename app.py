from flask import Flask, Blueprint
from flask import render_template, request
from flask_restful import Api
import cgi
import psycopg2

from flask_sqlalchemy import SQLAlchemy

from resorces.Hello import Hello
from resorces.Addition import Addition
from config import bonhappeteeData
from resorces.loginApi import Login
from temp import temp1


app = Flask(__name__)

a = {"column1":"column1 ka data","serialNo":123}
db_conn = None
db_conn = psycopg2.connect(database='bhtoday',user='bh',password='test')
cursor = db_conn.cursor()
columns = ", ".join(list(a.keys()))
values_template = ", ".join(["%s"] * len(list(a.keys())))


sql = "insert into %s (%s) values (%s)" % (
    'testtemp', columns, values_template)
print (sql)
values = tuple(a[key] for key in list(a.keys()))
print (values)
cursor.execute(sql,values)
#cursor.execute("select * from loginInfoTemp;")
#print(cursor.fetchall())
db_conn.commit()
cursor = None
db_conn.close()
db_conn = None

form = cgi.FieldStorage()
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

app.config.from_object("config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(db)
# Route
api.add_resource(Hello, '/Hello')
api.add_resource(Addition, '/Addition')
api.add_resource(Login, '/loginApi')
app.register_blueprint(api_bp, url_prefix='/api')

#db_session_factory = bonhappeteeData().Session
#print(db_session_factory)
#db_session = db_session_factory()
#conn = db.connect()
#g.session = db_session_factory()
#res = g.session.execute("select * LoginInfoTemp").fetchall()
#print(res)
import logger
log = logger.setup_applevel_logger(file_name = 'app_debug.log')
log.debug('Calling module function.')

@app.route("/")
def hello():
    prev = request.referrer
    print(prev)
    if prev == "/api/loginApi" :
        user = False
        print(user)
        return render_template("index.html",head = '<p>Hello Welcome to Flask </p><br><p>Invalid Username or Password </p>')
    else:
        user = True
        print(user)
        return render_template("index.html",head = '<p>Hello Welcome to Flask </p>')
    # return "Hi Vijay!!!"

@app.route("/admin", methods=["GET", "POST"])
def loginMessageAdmin():
    # return args
    name = request.form['username']
    args = request.args
    print(args)
    return name + "Logged in successfully!!!"


@app.route("/login", methods=["GET", "POST"])
def loginMessage():
    # return args
    name = request.form['username']
    args = request.args
    print(args)
    return name + "Logged in successfully!!!"


@app.route("/login/<username>", methods=["GET", "POST"])
def loginMessageURL(username):
    # return args
    # name = form.getvalue('username')
    args = request.args
    print(args)
    return username + "Logged in successfully!!!"
'''
@app.before_request
def _before_request():
    g.session  = db_session_factory()


@app.after_request
def after(response):
    try:
        g.session.commit()
        g.user_session.commit()
    except Exception as e:
        g.session.rollback()
        g.user_session.rollback()
    return response
'''

app.run(port=5001)
