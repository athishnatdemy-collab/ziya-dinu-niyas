#!/bin/bash
set -e

echo "========================================="
echo " Deploying ziya-dinu.vandmark.com"
echo "========================================="

PROJECT_DIR="/var/www/ziya-dinu.vandmark.com"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Error: Directory $PROJECT_DIR does not exist."
    echo "Please clone the repo into $PROJECT_DIR first."
    exit 1
fi

cd "$PROJECT_DIR"

# 1. Virtual environment setup
if [ ! -d "venv" ]; then
    echo "--> Creating virtual environment..."
    python3 -m venv venv
fi

echo "--> Installing / upgrading dependencies..."
./venv/bin/pip install --upgrade pip -q
./venv/bin/pip install -r requirements.txt -q

# 2. Django static & migrations
echo "--> Collecting static files..."
./venv/bin/python manage.py collectstatic --noinput

echo "--> Applying database migrations..."
./venv/bin/python manage.py migrate

# 3. Gunicorn systemd service
echo "--> Updating Gunicorn systemd service..."
sudo cp systemd/gunicorn_ziya_dinu.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable gunicorn_ziya_dinu
sudo systemctl restart gunicorn_ziya_dinu

# 4. Nginx configuration
echo "--> Configuring Nginx..."
sudo cp nginx/ziya-dinu.vandmark.com.conf /etc/nginx/sites-available/ziya-dinu.vandmark.com
if [ ! -f /etc/nginx/sites-enabled/ziya-dinu.vandmark.com ]; then
    sudo ln -s /etc/nginx/sites-available/ziya-dinu.vandmark.com /etc/nginx/sites-enabled/
fi

echo "--> Testing Nginx syntax..."
sudo nginx -t

echo "--> Reloading Nginx..."
sudo systemctl reload nginx

echo "========================================="
echo " Deployment Complete!"
echo " URL: http://ziya-dinu.vandmark.com"
echo "========================================="
