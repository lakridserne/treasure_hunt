Denne Django App er lavet på følgende måde:

django-admin startproject treasure_hunt  
cd treasure_hunt  
virtualenv virtualenv/bin/activate  
python manage.py startapp card  

Denne kommando bruger man når man skal applie migrations (ifht. databasen)  
python manage.py migrate

Hvis man ændrer i modeller skal man lave en migration (og bagefter applie den).
Det gør man med følgende kommando  
python manage.py makemigrations

Man kan lave en bruger med  
python manage.py createsuperuser

Man kan køre app'en med  
python manage.py runserver

Derefter kan man besøge admin på http://127.0.0.1:8000/admin/
