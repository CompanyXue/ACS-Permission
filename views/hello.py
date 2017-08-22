# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from database.config_setting import app

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            user = User(name=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return refirect(url_for('/index'))
    return render_template('index.html', form=form, name=session.get('name'),\
                           known=session.get('known',False))
 