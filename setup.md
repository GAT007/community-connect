# Setup

## Prequisites

Clone the project from the https://gitlab.com/ka-moamoa/community-connect/-/tree/main

### Python environment

1. Create a new python virtual environment with python3 : python3 -m venv community
2. Activate the python environment : source community/bin/activate
3. CD into the root folder of the project and install all the packages in the directory: pip install -r requirements.txt

### Starting the python project on your local

1. cd to the backend folder
2. run python3 manage.py runserver
3. This will start the server at http://127.0.0.1:8000/. The project is still nascent so you may see migration pending
   errors, please ignore them for now.

#### Post app development instruction

1. python manage.py startapp <app-name> : To create new application

#### Must be run before every backend commit to ensure no migrations are pending

1. python3 manage.py makemigrations
2. python3 manage.py migrate

### Starting the react project on your local

1. cd to the frontend folder
2. run npm install - one time only or if any changes have been done to the package.json file
3. npm run build - to build the latest projects
4. npm run dev - to run the local server