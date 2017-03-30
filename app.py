from flask import Flask, jsonify, request
from datetime import date
import time
from flask_sqlalchemy import SQLAlchemy
import psycopg2


test_select = """select * from users;"""
try:
	con = psycopg2.connect('dbname=test_backend user=michaelcesario')
except:
	print("Unable to connect")

cur = con.cursor()

try:
	cur.execute(test_select)
	data = cur.fetchall()
	for user in data:
		print(user)
except:
	print("Unable to select")

app = Flask(__name__) #global object for file

@app.route("/hello") #endpoint that clients reach via route
def hello(): #function that will run when client reaches endpoint
	return "Hello World!";

@app.route("/add_user", methods = ['POST'])
def add_user():
	dict = request.get_json() #save incoming json data from client into dictionary
	username = dict['username']
	email = dict['email']
	
	#try:
	#cur.executemany('INSERT INTO users(username,email) values (?,?)', [(username,email)]) #injection
	#conn.commit()
	#return jsonify(success=True)
		
	#except sqlite3.Error as er:
	#	print(er)
	#	return  jsonify(error = er)
	
	

if __name__ == "__main__": 
	app.run()
