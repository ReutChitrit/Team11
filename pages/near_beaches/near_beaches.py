from flask import render_template, Blueprint, request, session
from pages.near_beaches.class_near_beaches import beaches_with_LG_and_SS, beaches_with_SS, beaches_with_LG, \
    beaches_by_city, display_all_beaches, fetch_func

near_beaches = Blueprint('near_beaches', __name__, static_folder='static',
                         static_url_path='/pages/near_beaches',
                         template_folder='templates')


@near_beaches.route('/near_beaches', methods=['GET'])
def nearbeachesfunc():
    session["all_beaches"] = False
    only_with_surf = request.args['supplies']
    only_with_guard = request.args['life_guard']

    if session.get('city') is not None:
        if only_with_surf == "כן" and only_with_guard == "כן":
            query = beaches_with_LG_and_SS(session['city'])
        elif only_with_surf == "כן":
            query = beaches_with_SS(session['city'])
        elif only_with_guard == "כן":
            query = beaches_with_LG(session['city'])
        else:
            query = beaches_by_city(session['city'])
        beaches = fetch_func(query)
        return render_template('near_beaches.html', beaches=beaches, guard=only_with_guard, surf=only_with_surf)

    return render_template('near_beaches.html')


@near_beaches.route('/all_beaches', methods=['GET'])
def all_beaches_func():
    session["all_beaches"] = True
    query = display_all_beaches()
    all_beaches = fetch_func(query)
    return render_template('near_beaches.html', beaches=all_beaches)
