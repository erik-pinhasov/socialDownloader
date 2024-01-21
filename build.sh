set -o errexit

curl -o /dev/null https://www.facebook.com/
curl -o /dev/null https://www.youtube.com/
curl -o /dev/null https://www.twitter.com/
curl -o /dev/null https://www.snapchat.com/
curl -o /dev/null https://www.instagram.com/
curl -o /dev/null https://www.linkedin.com/


pip install --upgrade pip
pip install -r requirements.txt

cp innertube.py ~/project/src/.venv/lib/python3.11/site-packages/pytube/innertube.py

python manage.py collectstatic --no-input
python manage.py migrate
