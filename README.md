# Admin panel in Django
Админ панель для генерации Word документов

git clone https://github.com/Liofan/admin_panel.git

cd admin_panel

python3 -m venv env

source /env/bin/activate

pip install -r requirements.txt

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser
