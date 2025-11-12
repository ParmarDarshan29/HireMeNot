# 🚀 HireMeNot Deployment Guide

This guide helps you deploy HireMeNot to production.

## Prerequisites

- Git account
- Domain name (optional)
- Server or hosting platform account

## Deployment Options

### Option 1: Heroku (Easiest)

#### 1. Install Heroku CLI
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

#### 2. Login to Heroku
```bash
heroku login
```

#### 3. Create Heroku App
```bash
heroku create your-app-name
```

#### 4. Add Buildpack
```bash
heroku buildpacks:set heroku/python
```

#### 5. Create Procfile
Create `Procfile` in project root:
```
web: gunicorn hiremenot.wsgi --log-file -
```

#### 6. Update requirements.txt
Add these lines:
```
gunicorn>=20.1.0
whitenoise>=6.5.0
dj-database-url>=2.1.0
psycopg2-binary>=2.9.9
```

#### 7. Update settings.py
Add at the top:
```python
import dj_database_url
```

Update middleware:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]
```

Update database:
```python
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

Update static files:
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Update allowed hosts:
```python
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']
```

#### 8. Set Environment Variables
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set USE_LOCAL_AI=false
heroku config:set OPENROUTER_API_KEY="your-api-key"
```

#### 9. Deploy
```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

#### 10. Run Migrations
```bash
heroku run python manage.py migrate
```

#### 11. Create Superuser
```bash
heroku run python manage.py createsuperuser
```

---

### Option 2: Railway (Modern & Simple)

#### 1. Install Railway CLI
```bash
npm i -g @railway/cli
```

#### 2. Login & Initialize
```bash
railway login
railway init
```

#### 3. Add Environment Variables
In Railway dashboard, add:
- `SECRET_KEY`
- `DEBUG=False`
- `OPENROUTER_API_KEY`
- `USE_LOCAL_AI=false`

#### 4. Create railway.toml
```toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "python manage.py migrate && gunicorn hiremenot.wsgi"
healthcheckPath = "/"
```

#### 5. Deploy
```bash
railway up
```

---

### Option 3: DigitalOcean App Platform

#### 1. Prepare App Spec
Create `.do/app.yaml`:
```yaml
name: hiremenot
services:
  - name: web
    github:
      repo: your-username/HireMeNot
      branch: main
    build_command: pip install -r requirements.txt
    run_command: gunicorn hiremenot.wsgi
    envs:
      - key: SECRET_KEY
        value: ${SECRET_KEY}
      - key: DEBUG
        value: "False"
      - key: OPENROUTER_API_KEY
        value: ${OPENROUTER_API_KEY}
    http_port: 8000
```

#### 2. Deploy via Dashboard
- Connect GitHub repository
- Configure environment variables
- Deploy!

---

### Option 4: VPS (Ubuntu) - Advanced

#### 1. Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python & dependencies
sudo apt install python3 python3-pip python3-venv nginx -y

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y
```

#### 2. Create Database
```bash
sudo -u postgres psql
CREATE DATABASE hiremenot;
CREATE USER hiremenotuser WITH PASSWORD 'your_password';
ALTER ROLE hiremenotuser SET client_encoding TO 'utf8';
ALTER ROLE hiremenotuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE hiremenotuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE hiremenot TO hiremenotuser;
\q
```

#### 3. Clone & Setup Project
```bash
cd /var/www
git clone https://github.com/your-username/HireMeNot.git
cd HireMeNot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

#### 4. Configure Django
Edit `.env`:
```
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://hiremenotuser:your_password@localhost/hiremenot
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

#### 5. Collect Static Files
```bash
python manage.py collectstatic --noinput
python manage.py migrate
```

#### 6. Create Gunicorn Service
Create `/etc/systemd/system/hiremenot.service`:
```ini
[Unit]
Description=HireMeNot Django App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/HireMeNot
Environment="PATH=/var/www/HireMeNot/venv/bin"
ExecStart=/var/www/HireMeNot/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 hiremenot.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start hiremenot
sudo systemctl enable hiremenot
```

#### 7. Configure Nginx
Create `/etc/nginx/sites-available/hiremenot`:
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/HireMeNot;
    }
    
    location /media/ {
        root /var/www/HireMeNot;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/hiremenot /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### 8. Setup SSL (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

---

## Post-Deployment Checklist

### Security
- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Enable HTTPS/SSL
- [ ] Use environment variables for secrets
- [ ] Set up firewall rules
- [ ] Regular security updates

### Performance
- [ ] Enable static file compression
- [ ] Use CDN for static files
- [ ] Set up database connection pooling
- [ ] Configure caching (Redis)
- [ ] Enable gzip compression
- [ ] Monitor server resources

### Monitoring
- [ ] Set up error logging (Sentry)
- [ ] Configure uptime monitoring
- [ ] Set up analytics
- [ ] Monitor API usage
- [ ] Database backups

### Testing
- [ ] Test all features work in production
- [ ] Test file uploads
- [ ] Test API integrations
- [ ] Test on mobile devices
- [ ] Check page load times

## Environment Variables for Production

```bash
# Required
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# Database (if using PostgreSQL)
DATABASE_URL=postgres://user:password@localhost/dbname

# AI API
USE_LOCAL_AI=false
OPENROUTER_API_KEY=your-openrouter-key
OPENROUTER_MODEL=meta-llama/llama-3.2-3b-instruct:free

# Optional
GIPHY_API_KEY=your-giphy-key
SITE_URL=https://your-domain.com
```

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Connection Issues
- Check database credentials
- Verify database is running
- Check firewall rules

### 502 Bad Gateway
- Check Gunicorn is running
- Verify socket/port configuration
- Check Nginx error logs

### API Rate Limits
- Upgrade API plan
- Implement caching
- Add rate limiting

## Cost Estimates

### Heroku
- Free tier: $0 (limited hours)
- Hobby: $7/month
- Production: $25+/month

### Railway
- Hobby: $5/month
- Pro: $20/month

### DigitalOcean
- Basic Droplet: $5/month
- App Platform: $5/month

### VPS
- Basic: $5-10/month
- Database: +$15/month (managed)
- Domain: $10-15/year

## Support

For deployment issues:
1. Check service-specific documentation
2. Review error logs
3. Open GitHub issue
4. Contact hosting support

---

Good luck with your deployment! 🚀🔥
