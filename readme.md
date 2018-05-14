1. For at komme i gang skal man først lave et projekt. Det gør man sådan her:

django-admin startproject treasure_hunt  
cd treasure_hunt  

2. Følgende laver et virtuelt miljø  
virtualenv virtualenv/bin/activate  
3. Og så kan vi lige installere alle pakkerne:  
pip install -r requirements.txt  

4. Og til sidst lave mappen card med et par filer
python manage.py startapp card  

5. Vi skal have lavet en database - det kan vi gøre med følgende kommando. Den gør også lidt mere for dig.  
python manage.py migrate

6. Hvis man ændrer i modeller skal man lave en migration (og bagefter applie den).  
Det gør man med følgende kommando  
python manage.py makemigrations  
Herefter skal man køre kommandoen fra før  
python manage.py migrate  

7. Man kan lave en bruger med  
python manage.py createsuperuser

8.
Man kan køre app'en med  
python manage.py runserver

9. 
Derefter kan man besøge admin på http://127.0.0.1:8000/admin/
