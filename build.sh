
sudo pip install --upgrade pip

sudo pip install -r requirements.txt
sudo pip install werkzeug

python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
