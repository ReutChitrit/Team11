from flask import render_template, Blueprint

save_beach = Blueprint('save_beach', __name__, static_folder='static',
                       static_url_path='/pages/save_beach',
                       template_folder='templates')


@save_beach.route('/save_beach')
def savebeachfunc():
    return render_template('save_beach.html')
