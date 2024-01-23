
sudo pip install --upgrade pip

pip install -r requirements.txt
pip install werkzeug

python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
