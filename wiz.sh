#script cannot be ran directly, must be ran using source

#echo "activating virtual environment 'myvenv' "

#source .venv/bin/activate

#echo "myvenv activated"
#echo "starting postgres server..."

#pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start

#echo "starting nginx web server..." 
#nginx
#echo "starting gunicorn application server.."
python manage.py runserver --settings=mysite.settings.development
#use only in a development environmemt 
#gunicorn  mysite.wsgi:application --reload 
#gunicorn --certfile=cert.pem --keyfile=key.pem --workers=4 mysite.wsgi:application
#echo "shutting down postgres server..."

#pg_ctl -D $PREFIX/var/lib/postgresql -l logfile stop

#echo "shutting down nginx web server..."
#nginx -s stop

#echo "deactivating virtual env myvenv ..."

#deactivate
#echo "done !"
