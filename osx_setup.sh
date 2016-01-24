brew install mysql
mysql.server start
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'root'@'localhost';"
mysql -uroot -e "CREATE DATABASE IF NOT EXISTS twitch"
mysql -uroot twitch < schema.sql
cp src/config/config_example.py src/config/config.py
cp globals_example.py globals.py
