# Repository Name
Project for proproject

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- UBUNTU 22.04.5
- Python 3.x
- Git (to clone repositories or install dependencies from GitHub)

## Installation

Follow the steps below to development test and run this project:

**1. Install Environment**

Second, we will create an environment for the proproducts project.

```bash
sudo apt install language-pack-id
sudo dpkg-reconfigure locales

sudo apt install -y python3 python3-pip python3-venv
python3 -m pip install --user pipenv
sudo -H pip3 install virtualenv

python3.10 -m venv envproproducts
```

**2. Clone Repository**

Third, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/herbew/proproducts.git
```

**3. Install Service**

To install the service, the first thing to do is to ensure that all the required libraries are properly installed according to the Ubuntu 22.04.5 OS.

```bash
sudo apt install dos2unix -y 
dos2unix proproducts/utilities/install_os_dependencies.sh 
dos2unix proproducts/utilities/install_python_dependencies.sh

sudo chmod a+x proproducts/utilities/install_os_dependencies.sh
sudo chmod a+x proproducts/utilities/install_python_dependencies.sh

sudo ./proproducts/utilities/install_os_dependencies.sh install
```
Then, install the application libraries.

```bash
source envproproducts/bin/activate
cd proproducts
./utilities/install_python_dependencies.sh
```

**4. Setup Service**

Running the setup, according to django framework rules

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

python3 manage.py loaddata users/fixtures/0002_users.json
```

**5. Test Service**

To ensure everything is running well, testing must be carried out.

```bash
python manage.py test  --verbosity=2

```









