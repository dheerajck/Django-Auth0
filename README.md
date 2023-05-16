# Setting up the project
## I - Clone this repo

```
git clone https://github.com/dheerajck/Django-Auth0.git
```

## II - Create a new Python virtual environment:
```
python -m venv venv
```

## III - Activate the virtual environment and install the project requirements:

```
source venv/bin/activate
pip install -r requirements.txt
```

## IV - Create a new .env file on the root directory based on .env.example and update the variables in the .env file

## V -  Perform the Django database migrations:
```
python manage.py migrate
```


## VI - Start the Django development server:
```
python manage.py runserver
```

Now open your web browser and navigate to http://localhost:8000/ to view the application.

That's it! You should now be able to run the Django server and start working on your project. Don't forget to update the .env file with your own environment variables before running the server.