<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:3C3B3F,100:605C3C&height=250&section=header&text=DevSync%20Backend&fontSize=70&fontAlign=50&fontAlignY=35&animation=fadeIn&desc=Secure%20REST%20API%20with%20JWT%20&descAlign=50&descAlignY=60&descSize=20" alt="DevSync Backend Header" width="100%" />

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=F7F7F7&background=0D1117&center=true&vCenter=true&width=600&lines=Django+Rest+Framework+Powered+%F0%9F%9A%80;Secure+JWT+Authentication+%F0%9F%94%91;Email+OTP+Verification+%F0%9F%93%A7;Rate+Limiting+%26+Throttling+%E2%9F%B2;Robust+User+Management..." alt="Typing Animation" />
  </a>
</div>
  
  <br>

  <p align="center">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/Rest_Framework-A30000?style=for-the-badge&logo=django&logoColor=white" alt="DRF" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  </p>

</div>

---

## 📖 About The Project

**DevSync Backend** is a high-performance, secure authentication microservice designed as a foundational layer for scalable web and mobile applications. Engineered with **Django Rest Framework**, it provides a production-grade identity management system out of the box.

This project was architected to address common security pitfalls in modern development, enforcing strict standards for data protection, user verification, and API accessibility.

### 🔑 Key Features
*   **Stateless JWT Authentication:** Secure, scalable token-based access compatible with microservices.
*   **Cryptographic Security:** OTP generation using Python's `secrets` module for non-predictable tokens.
*   **Throttling & protection:** Built-in rate limiting to mitigate Brute-Force and DDoS attacks.
*   **Role-Based Access Control (RBAC):** Distinct permission scopes for Admins and Standard Users.
*   **Resilient Architecture:** Centralized error handling and standardized API responses.

<br>

## 🛠️ Tech Stack & Tools

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=django,python,sqlite,postman,vscode,git,github&perline=7" />
  </a>
</div>

<br>

## ⚡ Quick Start Guide

Follow these steps to get the server running on your local machine.

### 1. Clone & Install
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/DevSync-Backend.git

# Enter directory
cd DevSync-Backend

# Create Virtual Environment
python -m venv venv

# Activate Virtual Environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the root directory. Configure the following variables:

| Variable | Description | Required | Example |
| :--- | :--- | :---: | :--- |
| `DEBUG` | Toggle debug mode (False for Prod) | Yes | `True` |
| `SECRET_KEY` | Django security key | Yes | `django-insecure...` |
| `EMAIL_HOST_USER` | SMTP Email Address | Yes | `admin@example.com` |
| `EMAIL_HOST_PASSWORD` | SMTP App Password | Yes | `abcd 1234 efgh 5678` |

### 3. Ignite Server

```bash
# Apply database migrations
python manage.py migrate

# Run the local server
python manage.py runserver
```

## 📡 API Endpoints Documentation

| Method | Endpoint | Access | Functionality |
| --- | --- | --- | --- |
| **Auth & Registration** |  |  |  |
| `POST` | `/api/signup/` | 🔓 Public | Creates a new user (Inactive state), Sends OTP |
| `POST` | `/api/verify-otp/` | 🔓 Public | Verifies email via 6-digit OTP code |
| `POST` | `/api/login/` | 🔓 Public | Returns `Access` & `Refresh` tokens |
| **Token Management** |  |  |  |
| `POST` | `/api/token/refresh/` | 🔓 Public | Get new Access token using Refresh token |
| `POST` | `/api/logout/` | 🔐 Auth | Blacklists the refresh token |
| **User Management** |  |  |  |
| `GET` | `/api/profile/` | 🔐 Auth | Get current logged-in user details |
| `GET` | `/api/users/` | 👮 Admin | List all registered users (Admin only) |

> **Note:** Endpoints marked **🔐 Auth** require the header: `Authorization: Bearer <your_access_token>`

## 🚀 Roadmap

* ✅ **Secure Email/Password Registration**
* Custom user model with email-first authentication.


* ✅ **OTP Email Verification (SMTP)**
* Real-time 6-digit code validation using cryptographically secure `secrets` module.


* ✅ **JWT Authentication System**
* Full Access/Refresh token cycle with rotation and blacklisting.


* ✅ **Rate Limiting & Throttling**
* Brute-force protection on Login (5/min) and OTP (3/min) endpoints.


* 🚧 **Password Reset Flow** (Planned)
* Secure "Forgot Password" functionality via email.


* 🚧 **Account Deletion** (Planned)
* User-initiated account removal.



## 📂 Project Structure

```text
DevSync/
├── apps/
│   └── accounts/          # User Auth, Models, Views, Serializers
├── core/                  # Project Settings & URLs
├── .env                   # Secret Keys (Ignored by Git)
├── manage.py              # CLI Utility
└── requirements.txt       # Dependencies
```

<div align="center">

<h3>👤 Author</h3>

<p><b>Muhammad Zaid</b></p>

<p>
<a href="https://www.linkedin.com/in/muhammad-zaid-945b01337/" target="_blank">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"/>
</a>
<a href="https://github.com/mzaid-dev" target="_blank">
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Follow on GitHub"/>
</a>
<a href="https://mail.google.com/mail/?view=cm&fs=1&to=dev.mzaid@gmail.com" target="_blank">
<img src="https://img.shields.io/badge/Email_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Me"/>
</a>
</p>

<sub><i>Built with ❤️ for the Open Source Community</i></sub>

</div>
