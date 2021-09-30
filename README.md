```
git clone https://github.com/Justblue0312/Find_Job.git
virtualenv venv
cd env/
cd Script/
./activate
cd .. (Do it two times)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
``
