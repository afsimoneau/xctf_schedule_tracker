rm db.sqlite3

python3 manage.py migrate --run-syncdb

python3 manage.py loaddata fixtures/reset.json
