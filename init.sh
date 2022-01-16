/usr/bin/python3 -m pip install --upgrade pip   #upgrade pip
pip3 install pipenv #Install pipenv for managing virtual enviroments
mkdir django
cd django
pipenv install django
pipenv --venv   # --> will show the path to the venv like the below line
cd /home/halim/.local/share/virtualenvs/<env dir name>  # /bin/python
cd ~/python-practice/django
pipenv shell    #To enter the virtual env under the django dir
django-admin startproject <proj name> .
python manage.py runserver <port num>   #port by default is 8000
python manage.py startapp playground