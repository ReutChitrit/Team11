from flask import render_template, Blueprint



tips = Blueprint('tips', __name__, static_folder='static',
                 static_url_path='/pages/tips',
                 template_folder='templates')


@tips.route('/tips')
def tipsfunc():

    return render_template('tips.html')
