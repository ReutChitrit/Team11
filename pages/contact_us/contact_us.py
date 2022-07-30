from flask import render_template, Blueprint, redirect, url_for, request

from pages.contact_us.class_contact_us import all_comments_by_email, fetch_query, \
    update_comment_func, delete_comment_function, insert_comment_function

contact_us = Blueprint(
    'contact_us',
    __name__,
    static_folder='static',
    static_url_path='/contact_us',
    template_folder='templates')


@contact_us.route('/contact_us')
def contactusfunc():
    return render_template('contact_us.html', message=request.args.get('message'))


@contact_us.route('/search', methods=['POST'])
def searchfunc():
    if 'email' in request.form:
        email = request.form['email']
        query = all_comments_by_email(email)
        comments = fetch_query(query)
        if comments:
            return render_template('contact_us.html',
                                   comment_list=comments,
                                   )
        else:
            return render_template('contact_us.html', message='המשתמש לא נמצא.')

    return render_template('contact_us.html')


@contact_us.route('/insert_comment', methods=["POST"])
def insert_comment():
    email = request.form['email']
    frequency = request.form['usage']
    phone_number = request.form['PhoneNumber']
    text = request.form['additional']
    insert_comment_function(email, phone_number, frequency, text)
    return redirect(url_for('contact_us.contactusfunc', message="פרטי הודעתך נשמרו בהצלחה"))


@contact_us.route('/delete_comment', methods=['POST'])
def delete_comment():
    serial_number = request.form['serial_number']
    delete_comment_function(serial_number)
    return redirect(url_for('contact_us.contactusfunc', message="הודעתך נמחקה בהצלחה!"))


@contact_us.route('/update_comment', methods=['POST'])
def update_comment():
    frequency = request.form['usage']
    phone_number = request.form['PhoneNumber']
    text = request.form['additional']
    serial_number = int(request.form['serial_number'])
    query = update_comment_func(frequency, phone_number, text, serial_number)
    return render_template('contact_us.html', message="הודעתך עודכנה בהצלחה!")
