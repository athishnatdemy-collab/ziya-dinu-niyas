# Ziya & Dinu - Nikah Invitation (Django + Nginx)

An interactive digital Nikah invitation website built with Django, Nginx, and Gunicorn.

- **Domain**: `ziya-dinu.vandmark.com`
- **Bride Invitation URL**: `http://ziya-dinu.vandmark.com/` (or `http://ziya-dinu.vandmark.com/ziya`)
- **Groom Invitation URL**: `http://ziya-dinu.vandmark.com/dinu`
- **Reception (4 PM - 7 PM) URL**: `https://ziya-dinu.vandmark.com/reception-4-7` (or `receptoin-4-7`, `reception`)
- **Reception (7 PM - 10 PM) URL**: `https://ziya-dinu.vandmark.com/reception-7-10` (or `receptoin-7-10`)
- **Server Path**: `/var/www/ziya-dinu.vandmark.com`

---

## Project Structure

```text
├── core/                   # Django project configuration (settings, urls, wsgi)
├── invitation/             # Main Django app
├── templates/              # HTML templates (index.html for bride, dinu.html for groom, reception.html for 4-7 PM, reception_7_10.html for 7-10 PM)
├── static/                 # Static assets (img/, song.mp3, reception/img/, reception/audio/)
├── nginx/                  # Nginx server configuration
├── systemd/                # Gunicorn systemd service
├── manage.py               # Django CLI utility
└── requirements.txt        # Python dependencies
```

---

## Server Deployment Instructions (Ubuntu)

Run these commands on your Ubuntu server (`ubuntu@ip-172-31-7-216`):

### 1. Clone the Repository
```bash
cd /var/www
sudo git clone https://github.com/athishnatdemy-collab/ziya-dinu-niyas.git ziya-dinu.vandmark.com
sudo chown -R ubuntu:www-data /var/www/ziya-dinu.vandmark.com
cd /var/www/ziya-dinu.vandmark.com
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Collect Static Files & Migrate Database
```bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate
```

### 4. Configure Gunicorn Systemd Service
```bash
sudo cp systemd/gunicorn_ziya_dinu.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start gunicorn_ziya_dinu
sudo systemctl enable gunicorn_ziya_dinu
sudo systemctl status gunicorn_ziya_dinu
```

### 5. Configure Nginx
```bash
sudo cp nginx/ziya-dinu.vandmark.com.conf /etc/nginx/sites-available/ziya-dinu.vandmark.com
sudo ln -s /etc/nginx/sites-available/ziya-dinu.vandmark.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 6. (Optional) Enable Free HTTPS / SSL with Certbot
```bash
sudo certbot --nginx -d ziya-dinu.vandmark.com
```
