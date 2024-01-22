set -o errexit



export SECRET_KEY='f9jc!0isofztwhdcap$l_cyq#1o9z^5n1j*b&d_5^k4k)=r!10'

sudo pip install -r requirements.txt


python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate
