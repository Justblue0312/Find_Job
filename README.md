git clone https://github.com/Justblue0312/Find_Job.git

virtualenv venv

cd env/

cd Script/

./activate

Do cd command two times
cd .. 

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

python manage.py createsuperuser

python manage.py runserver
