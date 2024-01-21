set -o errexit

cp -f innertube.py ~/project/src/.venv/lib/python3.11/site-packages/pytube/innertube.py

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
