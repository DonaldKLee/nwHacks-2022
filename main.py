import random, string, os
from flask import Flask, render_template, request, redirect, url_for
# from flask_socketio import SocketIO

import dns, pymongo

from datetime import datetime
from datetime import timedelta


mongodb_username = os.environ['mongodb_username']
mongodb_password = os.environ['mongodb_password']
client = pymongo.MongoClient("mongodb+srv://"+mongodb_username+":"+mongodb_password+"@cluster0.s7jm6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Database

app = Flask (
	__name__,
	template_folder = "templates", # HTML files folder
	static_folder = "staic" # Images and CSS files
)

# app.config['SECRET_KEY'] = random.choices(string.ascii_letters, k=4)) + "".join(random.choices(string.digits, k=4)
# socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		# Generates a room code for the user
		if request.form.get('create_room') == "Create a Room!":
			room_code_characters = []
			unshuffled_room_code = "".join(random.choices(string.ascii_letters, k=4)) + "".join(random.choices(string.digits, k=4))
			for character in unshuffled_room_code:
				room_code_characters.append(character)
			random.shuffle(room_code_characters)
			
			# The room code for joining other rooms
			room_code = "".join(room_code_characters)
			
			room_data = {
				"room_code": room_code,
				"users": [request.form["name"]],
				"time_end": None
			}

			db.rooms.insert_one(room_data)

			return redirect(url_for('room', room_code=room_code))

		elif request.form.get('room_code') == "Join a room!":

			room_code_submitted = request.form["room_code_submitted"]
			#name_submitted = request.form["name_submitted"]
			print(room_code_submitted)

			for room in db.rooms.find({'room_code': str(room_code_submitted)}):
				if len(room) > 0: # If that note has something
					foundroom = True
			
					if foundroom:
						#db.rooms.update_one({'room_code': str(room_code_submitted)}, {'$push': {'users': name_submitted}})
						return redirect(url_for('room', room_code=str(room_code_submitted)))
					
					else:
						return redirect(url_for, "/")
		

	return render_template("home.html")

@app.route('/room/<room_code>')
def room(room_code):
	# if request.method == "POST":
	# 	print("hello")
	# 	current_time = datetime.today()

	# 	n = 25
	# 	# Add 15 minutes to current time
	# 	end_time = current_time + timedelta(minutes=n)

	# 	print(end_time)


	foundroom = False

	for room in db.rooms.find({'room_code': str(room_code)}):
		if len(room) > 0: # If that note has something
			foundroom = True

	if foundroom:
		return render_template("room.html", room_data=room)
	
	else:
		return render_template('404.html')

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
		port = random.randint(2000, 9000),
		debug = True
	)



