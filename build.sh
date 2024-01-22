set -o errexit

curl -o /dev/null https://www.facebook.com/
curl -o /dev/null https://www.youtube.com/
curl -o /dev/null https://www.twitter.com/
curl -o /dev/null https://www.snapchat.com/

curl -o /dev/null https://www.instagram.com/
curl -o /dev/null https://instagram.ftlv6-1.fna.fbcdn.net/v/t66.30100-16/48823640_3535080280075598_3824682799276920101_n.mp4?_nc_ht=instagram.ftlv6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=i0U5jDUZfLQAX_fsLfZ&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfBF1larOur1YaxbB4ZC89EznIQLzuSYKFr3iEam-v7sgw&oe=65AF9227&_nc_sid=2999b8
curl -o /dev/null https://scontent.cdninstagram.com/v/t66.30100-16/48823640_3535080280075598_3824682799276920101_n.mp4?_nc_ht=instagram.ftlv6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=i0U5jDUZfLQAX_fsLfZ&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfBF1larOur1YaxbB4ZC89EznIQLzuSYKFr3iEam-v7sgw&oe=65AF9227&_nc_sid=2999b8
curl -o /dev/null https://www.linkedin.com/

export DEBUG=False

export SECRET_KEY='f9jc!0isofztwhdcap$l_cyq#1o9z^5n1j*b&d_5^k4k)=r!10' >> ~/.bashrc

sudo python3 pip install
sudo pip install --upgrade pip
sudo pip install -r requirements.txt

cp innertube.py root/socialDownloader/venv/lib/python3.8/site-packages/pytube/innertube.py
cp instaloadercontext.py root/socialDownloader/venv/lib/python3.8/site-packages/instaloader/instaloadercontext.py

python3 manage.py collectstatic --no-input
python3 manage.py migrate

sudo chmod +x build.sh
