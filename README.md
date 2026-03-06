# 🚀 Flask SaaS Dashboard

A modern **Flask Admin Dashboard** with authentication, analytics charts, and project management UI.

This project demonstrates a **production-ready Flask deployment architecture** using:

- Flask
- Gunicorn
- Nginx
- SQLite
- TailwindCSS
- Chart.js

---

# 📌 Features

- 🔐 User Login System
- 📊 Analytics Dashboard
- 📁 Projects Page
- 📈 Interactive Charts
- 🎨 Modern UI (Tailwind CSS)
- ⚡ Gunicorn Production Server
- 🌐 Nginx Reverse Proxy

---

# 🏗️ Architecture

Client → Nginx → Gunicorn → Flask → SQLite

---

# 📁 Project Structure

flask-saas-dashboard
│
├── app.py
├── database
│   └── users.db
│
├── templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── analytics.html
│   └── projects.html
│
├── static
│   ├── css
│   │   └── style.css
│   │
│   └── js
│       └── chart.js
│
└── README.md

---

# ⚙️ Installation

Clone the repository
```bash
git clone https://github.com/yourusername/flask-saas-dashboard.git
```
cd flask-saas-dashboard

Create virtual environment

python3 -m venv venv

source venv/bin/activate

Install dependencies

pip install flask flask-login gunicorn

---

# 🗄️ Setup Database

Run database initialization script

python database/init_db.py

Default credentials

username: admin

password: admin

---

# ▶️ Run Application

Development mode

python app.py

Production mode

gunicorn --workers 3 --bind 127.0.0.1:8000 app:app

Open in browser

http://127.0.0.1:8000

---

# 🚀 Nginx Deployment

Install Nginx

sudo apt install nginx

Create configuration

sudo nano /etc/nginx/sites-available/flaskapp

Example configuration

server {

    listen 80;

    server_name _;

    location / {

        proxy_pass http://127.0.0.1:8000;

        proxy_set_header Host $host;

        proxy_set_header X-Real-IP $remote_addr;

    }

}

Enable configuration

sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled

Restart nginx

sudo systemctl restart nginx

---

# 📊 Dashboard Pages

Dashboard → /dashboard

Analytics → /analytics

Projects → /projects

Logout → /logout

---

# 🔐 Authentication

Authentication is implemented using **Flask-Login**.

Only authenticated users can access dashboard pages.

---

# 🧑‍💻 Tech Stack

Python  
Flask  
Flask-Login  
SQLite  
TailwindCSS  
Chart.js  
Gunicorn  
Nginx  

---

# 🔮 Future Improvements

- User registration
- Password hashing
- REST API
- PostgreSQL database
- Docker deployment
- Kubernetes deployment

---

# 👨‍💻 Author

Shubham Tayde

YouTube Channel: Tech Tadka With Shubham

---

# ⭐ Support

If you like this project, please star the repository.
