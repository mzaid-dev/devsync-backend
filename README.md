# Nexus Chat Backend API Guide & Security Analysis

## 🔒 Security Analysis (Is this "Google Level" Security?)

**Verdict: NO.** Currently, this project is configured for **Development Mode**, not Production. It is **highly insecure** if deployed as-is.

### 🚨 Critical Security Issues (Must Fix for Production):

1.  **Hardcoded Secrets**: The `SECRET_KEY` is visible in `settings.py`. In a real "Google-level" app, this must be stored in environment variables and never committed to code.
2.  **Debug Mode**: `DEBUG = True` is dangerous for production. It leaks technical details (stack traces) to attackers.
3.  **Exposed Credentials**: Email host password and user are hardcoded in `settings.py`. This is a major security breach.
4.  **Weak Database**: SQLite is file-based and not suitable for high-concurrency or secure production environments.
5.  **Missing Security Headers**: No SSL/TLS configuration (`SECURE_SSL_REDIRECT`, etc.), default generic settings.
6.  **CORS**: Not configured (Cross-Origin Resource Sharing), which may block frontend apps.

**To make this secure:**
*   Use `.env` files (python-dotenv) for all secrets.
*   Set `DEBUG = False`.
*   Use a production-grade database (PostgreSQL).
*   Implement Rate Limiting (Throttling).
*   Enable SSL/HTTPS.

---

## 🚀 How to Run the Project

1.  **Activate Virtual Environment**:
    ```bash
    source venv/bin/activate
    ```

2.  **Run Migrations** (Initialize Database):
    ```bash
    python manage.py migrate
    ```

3.  **Start Server**:
    ```bash
    python manage.py runserver
    ```
    The server will run at `http://127.0.0.1:8000/`.

---

## 📬 Postman Testing Guide

Open Postman and create a new collection called "Nexus Chat".

### 1. Signup (Create Account)
*   **Method**: `POST`
*   **URL**: `http://127.0.0.1:8000/api/accounts/signup/`
*   **Body** (Select **raw** -> **JSON**):
    ```json
    {
        "username": "testuser",
        "email": "your_email@example.com",
        "password": "strongpassword123"
    }
    ```
*   **Response**: Returns user details. **Check your email** (or console if email fails) for the OTP.

### 2. Verify OTP (Activate Account)
*   **Method**: `POST`
*   **URL**: `http://127.0.0.1:8000/api/accounts/verify-otp/`
*   **Body** (JSON):
    ```json
    {
        "email": "your_email@example.com",
        "otp": "123456"  
    }
    ```
    *(Replace "123456" with the actual OTP you received)*

### 3. Login
*   **Method**: `POST`
*   **URL**: `http://127.0.0.1:8000/api/accounts/login/`
*   **Body** (JSON):
    ```json
    {
        "email": "your_email@example.com",
        "password": "strongpassword123"
    }
    ```
*   **Response**: You will receive an `access` token and a `refresh` token.
    *   **COPY the Access Token** for the next steps.

### 4. Get Profile (Protected Route)
*   **Method**: `GET`
*   **URL**: `http://127.0.0.1:8000/api/accounts/profile/`
*   **Authorization** (Tab):
    *   Type: **Bearer Token**
    *   Token: `PASTE_YOUR_ACCESS_TOKEN_HERE`
*   **Response**: Returns your profile info (email, username, role).

### 5. Refresh Token (Get New Access Token)
*   **Method**: `POST`
*   **URL**: `http://127.0.0.1:8000/api/accounts/token/refresh/`
*   **Body** (JSON):
    ```json
    {
        "refresh": "PASTE_YOUR_REFRESH_TOKEN_HERE"
    }
    ```

### 6. Logout
*   **Method**: `POST`
*   **URL**: `http://127.0.0.1:8000/api/accounts/logout/`
*   **Authorization**: Bearer Token (Access Token)
*   **Body** (JSON):
    ```json
    {
        "refresh": "PASTE_YOUR_REFRESH_TOKEN_HERE"
    }
    ```
# devsync-backend
