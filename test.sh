clear
coverage run -m unittest discover -s testing/ -t .
#coverage report --omit=venv/*,**__init__.py,src/test_endtoend.py,testing/TwitchIrc.py
