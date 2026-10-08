from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY="dev-only-change-me"
DEBUG=True
ALLOWED_HOSTS=[]
INSTALLED_APPS=["django.contrib.contenttypes","django.contrib.staticfiles","operaciones"]
MIDDLEWARE=[]
ROOT_URLCONF="cambio.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[BASE_DIR/"templates"],"APP_DIRS":True,"OPTIONS":{"context_processors":[]}}]
WSGI_APPLICATION="cambio.wsgi.application"
DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
LANGUAGE_CODE="es"
STATIC_URL="static/"
STATICFILES_DIRS=[BASE_DIR/"static"]
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"