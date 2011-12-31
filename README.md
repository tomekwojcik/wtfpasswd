What The Fuck Should I Use For Password?
=

Source code for http://whatthefuckshouldiuseforpassword.com/

Installation
-
1. `pip install -r requirements.txt`
1. `nosetests`

Serving via Werkzeug
-
1. `python run.py --help`
1. `python run.py [server_options]`

Serving via gunicorn
-
1. `pip install gunicorn`
1. `gunicorn pwdgen.app:app`

Serving via other WSGI servers
-
WSGI app is exported from `pwdgen.app:app`. If you installed the app in a virtual env be sure to make the environment aware of it.

API
-
The app provides API. See docs [here](https://gist.github.com/1517544).

Why?
-
For teh lulz.

License
-
MIT-style, see LICENSE.