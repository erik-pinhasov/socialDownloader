set -o errexit

curl -o /dev/null https://www.facebook.com/
curl -o /dev/null https://www.youtube.com/
curl -o /dev/null https://www.twitter.com/
curl -o /dev/null https://www.snapchat.com/

curl -o /dev/null https://www.instagram.com/
curl -o /dev/null https://instagram.ftlv6-1.fna.fbcdn.net/v/t66.30100-16/48823640_3535080280075598_3824682799276920101_n.mp4?_nc_ht=instagram.ftlv6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=i0U5jDUZfLQAX_fsLfZ&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfBF1larOur1YaxbB4ZC89EznIQLzuSYKFr3iEam-v7sgw&oe=65AF9227&_nc_sid=2999b8
curl -o /dev/null https://scontent.cdninstagram.com/v/t66.30100-16/48823640_3535080280075598_3824682799276920101_n.mp4?_nc_ht=instagram.ftlv6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=i0U5jDUZfLQAX_fsLfZ&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfBF1larOur1YaxbB4ZC89EznIQLzuSYKFr3iEam-v7sgw&oe=65AF9227&_nc_sid=2999b8
curl -o /dev/null https://www.linkedin.com/


pip install --upgrade pip
pip install -r requirements.txt

cp innertube.py ~/socialDownloader/venv/lib/python3.8/site-packages/pytube/innertube.py
cp instaloadercontext.py ~/socialDownloader/venv/lib/python3.8/site-packages/instaloader/instaloadercontext.py

python manage.py collectstatic --no-input
python manage.py migrate

cp innertube.py /.venv/lib/python3.8/site-packages/pytube/innertube.py
