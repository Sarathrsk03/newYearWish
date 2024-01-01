from flask import Flask, render_template
import csv 



app = Flask(__name__)

def checkFriendName(friendName):
   with open("static/friends.csv", "r") as fr:
        reader = csv.reader(fr, delimiter=";")
        content = [row for row in reader if row]  # Exclude empty rows
        for name, message in content[1:]:  # Skip the header row
            if name == friendName:
                return message
        return "Cheers to new beginnings and fresh starts! May the New Year bring you exciting opportunities, and may you make the most of each moment."

    

@app.route('/<friend_name>')
def index(friend_name):
    messageForFriend = checkFriendName(friend_name)
    friendname = friend_name[0].upper() + friend_name[1:]
    message=messageForFriend
    # Use the friend_name from the URL, default to "Friend" if not provided
    return render_template('wish.html', friend_name=friendname, message=message)

@app.route('/junior/<friend_name>')
def junior(friend_name):
    messageForFriend = checkFriendName("junior")
    friendname = friend_name[0].upper() + friend_name[1:]
    message=messageForFriend
    # Use the friend_name from the URL, default to "Friend" if not provided
    return render_template('wish.html', friend_name=friendname, message=message)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()

