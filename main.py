import random, string
from flask import Flask, render_template, request

app = Flask (
	__name__,
	template_folder = "templates", # HTML files folder
	static_folder = "staic" # Images and CSS files
)

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
			
			"""
				Tasks:
					- Add room code to database
					- Redirect user to the room

			"""

		elif request.form.get('join_room') == "Join a room!":
			print("aaaja")
			"""
				Tasks:
					- If room code exists in database
						- take user to room page

					- 
			"""
		

	return render_template("home.html")

@app.route('/room')
def room():
	return render_template("room.html")


if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
		port = random.randint(2000, 9000),
		debug = True
	)



