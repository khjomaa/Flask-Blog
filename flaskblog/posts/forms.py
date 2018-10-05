#!/usr/bin/env python

from __future__ import print_function
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    new_submit = SubmitField('Post')
    update_submit = SubmitField('Update')

