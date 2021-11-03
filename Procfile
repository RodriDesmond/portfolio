release: python manage.py migrate --run-syncdb
web gunicorn portfolio.wsgi:application --log-file -