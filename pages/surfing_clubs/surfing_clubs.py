from flask import render_template, Blueprint

surfing_clubs = Blueprint('surfing_clubs', __name__, static_folder='static',
                          static_url_path='/pages/surfing_clubs',
                          template_folder='templates')


@surfing_clubs.route('/surfing_clubs')
def surfingclubsfunc():
    return render_template('surfing_clubs.html')
