# library-system-crud

# Steps to run application

# Create a virtual environment

python -m venv env

# Activate the virtual environment

# For Windows:

.\env\Scripts\activate

# For macOS/Linux:

source env/bin/activate

# Install Dependencies

pip install -r requirements.txt

cd library_system

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
