
export DEBUG=False

pip install --upgrade pip
pip install -r requirements.txt

cp innertube.py ~/project/src/.venv/lib/python3.8/site-packages/pytube/innertube.py

python3 manage.py collectstatic --no-input
python3 manage.py migrate
