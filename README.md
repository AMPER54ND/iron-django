# Setting up Iron-Django and the OWASP application

## Start Steps

1. Install the latest version of Python 3 from your distro repository
    ```
    sudo apt-get install python3
    ```

1. Clone this project
    ```
    git clone XXXXX
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
