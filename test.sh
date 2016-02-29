clear
coverage run -m unittest discover -s testing/ -t .
coverage report -m --omit=venv/*,**__init__.py,testing/test_endtoend.py,testing/TwitchIrc.py
