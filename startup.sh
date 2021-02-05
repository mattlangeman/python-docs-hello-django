echo "-- Migrate Django Data Models"
python manage.py migrate
echo "-- Collect Static Files"
python manage.py collectstatic --no-input
echo "-- Start gunicorn with uvicorn workers"
gunicorn --workers 8 --threads 4 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000  -k uvicorn.workers.UvicornWorker \
     --chdir=/home/site/wwwroot django_hello.asgi