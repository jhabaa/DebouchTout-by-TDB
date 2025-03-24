from flask import Flask, render_template, request, redirect, url_for, flash, Request
from dotenv import load_dotenv
import mysql.connector
import json as json
import os 


app = Flask(__name__)
load_env = load_dotenv()
#MysQL Config
config = {
            'user':os.getenv("MYSQL_USER"),
            'password':os.getenv("MYSQL_PSSWRD"),
            'host':os.getenv("MYSQL_HOST"),
            'database':os.getenv("MYSQL_DB"),
            'raise_on_warnings':True
        }
cnx = mysql.connector.connect(**config)

def get_from_database(table:str, id:str = None, ordered8by:str=None ):
    cnx.reconnect()
    cur = cnx.cursor(dictionary=True) # prettier with dict
    query = f"SELECT * FROM {config['database']}.{table} {"where id = " + id if id  else ""} {ordered8by if ordered8by else ""};"
    cur.execute(query)
    output = cur.fetchall()
    return output

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    art = get_from_database(table="article", ordered8by="order by date desc")[:3]
    serv = get_from_database(table="service")
    return render_template('index.html', articles=art, services = serv)

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=get_from_database(table="article"))

@app.route('/about')
def about():
    serv = get_from_database(table="service")
    return render_template('about.html', services = serv)

@app.route('/about/<id>')
def about_service(id):
    s = get_from_database(table="service", id=id)
    serv = get_from_database(table="service")
    return render_template('about_service.html', services = serv, service = s)

@app.route('/article/<id>')
def article(id):
    cnx.reconnect()
    arg=[2]
    cur = cnx.cursor(dictionary=True)
    cur.callproc('readed', arg)
    cur.close()
    art = get_from_database(table="article", id=id)
    return render_template('article.html', article=art[-1] if len(art) > 0 else None)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
