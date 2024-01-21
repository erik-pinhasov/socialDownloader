set -o errexit

curl -o /dev/null https://www.facebook.com/
curl -o /dev/null https://www.youtube.com/
curl -o /dev/null https://www.twitter.com/
curl -o /dev/null https://www.snapchat.com/
curl -o /dev/null https://www.instagram.com/p/C0wlbk6o1DI/
wget https://www.instagram.com/p/C0wlbk6o1DI/
curl -o /dev/null https://www.linkedin.com/


pip install --upgrade pip
pip install -r requirements.txt

cp innertube.py ~/project/src/.venv/lib/python3.11/site-packages/pytube/innertube.py
cp instaloadercontext.py ~/project/src/.venv/lib/python3.11/site-packages/instaloader/main.py
cp main.py ~/project/src/.venv/lib/python3.11/site-packages/instaloader/main.py


python manage.py collectstatic --no-input
python manage.py migrate
