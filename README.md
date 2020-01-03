# Setting up Iron-Django and the OWASP application

This is a forked repository from sketchybinary's iron-django project, a Django project containing examples of "best-practices" when building an application using Django REST framework. This forked version contains the OWASP application which demonstrates live examples of web-app vulnerabilities found in OWASP's Top 10. 

## Setup

1. Install the latest version of Python 3 from your distro repository
    ```
    sudo apt-get install python3
    ```

1. Clone this project
    ```
    git clone git@github.com:AMPER54ND/iron-django.git
    ```

1. Create your python virtual-environment
    ```
    cd brewwolf
    python3 -m venv venv
    source venv/bin/activate
    ```
    
1. Source your python virtual-environment    
    ```
    source venv/bin/activate
    ```

1. Update pip and install requirements
    ```
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

1. Collect the static files within the brewwolf project
    ```
    python manage.py collectstatic
    ```

1. Start the Server using the "manage.py" found within the brewwolf project
    ```
    python manage.py runserver
    ```
