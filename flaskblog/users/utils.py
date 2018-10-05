#!/usr/bin/env python

from __future__ import print_function
import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = os.urandom(8).encode('hex')
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # resize image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender=os.environ.get('EMAIL_USER'), recipients=[user.email])
    msg.body = '''To Reset your password, visit the following link:
{0}

If you did not make this request then simply ignore this email and no changes will be made
'''.format(url_for('users.reset_token', token=token, _external=True))
    mail.send(msg)

