web: gunicorn -w 2 wsgi:application --log-level 'debug' --timeout 120
release: python craft migrate --force