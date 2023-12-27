# Django API Usage

### 1. clone the repo https://github.com/oderofrancis/Django-API-Usage.git and navigate to the cloned app

  `` git clone https://github.com/oderofrancis/Django-API-Usage.git``
  
  open with VS Code 
  
  ` cd Django-API-Usage && code .`

### 2. Create virtualenv and activate your environment

  `` virtualenv env `` 
  `` . env/bin/activate``

### 3. Make migrations and create superuser
    run `python manage.py migrate`
  
    for super user
  
    `` python manage.py createsuperuser``
  
    fill the fields.
### 4. Run runserver and navigate to http://127.0.0.1:8000/admin to fill in some companies and advocate 

  `` python manage.py runserver``

### 5. Test if you can access you APIs

     Navigate to API folder under parent folder and run `get.ipynb` file 
