from datetime import timedelta
from flask import Flask

from pages.contact_us.contact_us import contact_us
from pages.find_a_beach.find_a_beach import find_a_beach
from pages.near_beaches.near_beaches import near_beaches
from pages.save_beach.save_beach import save_beach
from pages.surfing_clubs.surfing_clubs import surfing_clubs
from pages.tips.tips import tips

app = Flask(__name__)
app.register_blueprint(tips)
app.register_blueprint(surfing_clubs)
app.register_blueprint(save_beach)
app.register_blueprint(near_beaches)
app.register_blueprint(find_a_beach)
app.register_blueprint(contact_us)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=0.5)

if __name__ == '__main__':
    app.run(debug=True)
