# Setting up Iron-Django

## Start Steps

1. Install the latest version of Python 3 from your Distro Repository
    ```
    sudo apt-get install python3
    ```

1. Clone this project
    ```
    git clone git@git.sp.darkwolf.io:will/brewwolf-python.git
    ```

1. Go into the project and create the virtual-environment
    ```
    cd brewwolf-python
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Update pip and install requirements
    ```
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

1. Start the notebook
    ```
    jupyter notebook
    ```
