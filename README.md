# bug-free-octo-dollop

### This is a python package 'django-polls', I have created.
to install this on your project, do:

**Steps:**
1. Clone this repository: hit in your terminal: `git clone git@github.com:dbijaya/bug-free-octo-dollop.git` .
1. Copy the folder named 'django-polls' and then paste outside of your current project directory.
1. and hit command: `python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz` .
  1. use Vertual environment (optional, but recommended)
  1. you may haven't installed [setuptools](https://pypi.org/project/setuptools/3.8.1/#:~:text=The%20recommended%20way%20to%20install,in%20your%20Python%20Scripts%20subdirectory.), if not do install: `pip install setuptools`
 1. don't forget to specify app name **'polls'** in your project settings.py file as:
 ```py
 INSTALLED_APPS = [
    ...
    'polls',
]
```
1. also, specify url in 'urls.py' as:
```py
from django.urls import path, include
urlpatterns = [path('polls/', include('polls.urls'),)]
```
1. now run, ` python manage.py runserver`
1. locate url: ` http://localhost:8000/polls/ `

**with Luck, it should work :)**
