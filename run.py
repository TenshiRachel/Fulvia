from Scripts import app, db
import datetime
from Scripts.models import Breakfast, Lunch, Dinner

#Check if logged in
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args,**kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized, Please log in','danger')
#             return redirect(url_for('login'))
#     return wrap
if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.debug = True
    app.run(port='80')

