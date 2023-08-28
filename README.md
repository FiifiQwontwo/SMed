# SMed
## Prerequisites
```bash
python 3.9

```


# Installation

```bash
$ git clone https://github.com/FiifiQwontwo/SMed.git
```

Then 
```bash
$ cd Foldername
```
create a virtual environment to install dependencies

```bash
python -m venv venv
./venv/Scripts/activate

```
Then install the dependencies:
```bash
(venv) $ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies: create a MySQL database, and comment out the sqlite code, and I also disable the .env file  then makemigrations and then migrate

```bash
(venv)$ cd project
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```
and navigate to http://localhost:8000/swagger/ to read the API documentation 

## Tech Stack 

    Python - Language Used
    Django - The web framework used
    SQLite & MYSQL - Database used(used MYSQL for development and used SQLite for Demo
    you can request for the data 
    


## Contributing
- [@Michael Ahwireng](https://www.github.com/FiifiQwontwo)
- 

## License

[MIT](https://choosealicense.com/licenses/mit/) This project is licensed under the MIT License - see the LICENSE.md file for details

