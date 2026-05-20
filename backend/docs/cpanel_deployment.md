# Shared cPanel Hosting Deployment Guide

This guide provides step-by-step instructions on how to deploy your production-ready Node.js, Express, and MySQL backend onto a standard **shared hosting server managed via cPanel**.

---

## Phase 1: Set Up the MySQL Database in cPanel

Since shared hosts don't allow raw command-line root database operations, you must use cPanel's interface tools.

### Step 1: Create the Database
1. Log into your **cPanel** dashboard.
2. Scroll to the **Databases** section and click on **MySQL® Database Wizard**.
3. **Enter Database Name**: E.g., `yourcpaneluser_beyondbridge_db`. Click **Next Step**.

### Step 2: Create the Database User
1. **Enter Username**: E.g., `yourcpaneluser_db_admin`.
2. **Generate Password**: Click the **Password Generator** to create a strong password. Save this password securely!
3. Click **Create User**.

### Step 3: Grant User Privileges
1. In the privileges screen, check **ALL PRIVILEGES** (this grants standard SELECT, INSERT, UPDATE, DELETE, and table schemas privileges).
2. Click **Make Changes** (or **Next Step**). Keep a note of the exact database name, username, and password!

### Step 4: Import the Database Schema
1. Go back to the main cPanel dashboard.
2. Under the **Databases** section, click on **phpMyAdmin**.
3. **Select your newly created database from the left-hand sidebar** (e.g., `yourcpaneluser_beyondbridge_db`).
   > [!IMPORTANT]
   > You **must** click on your database in the left sidebar first. The repository's schema file `backend/schema.sql` has its `CREATE DATABASE` and `USE` statements commented out to ensure compatibility with shared hosting security policies (which prevents the `#1044 Access Denied` error).
4. Click the **Import** tab at the top of the page.
5. Choose your `schema.sql` file (from `backend/schema.sql`) and click **Go** (or **Import**) at the bottom. The tables `users` and `otp_verifications` will be created instantly inside your database.

---

## Phase 2: Prepare Node.js Code for Upload

1. Open your project locally.
2. Delete the `node_modules` folder (this prevents uploading massive directories of operating-system-specific files, which will be re-installed directly on the cPanel server instead).
3. Zip the entire backend codebase (including `.env`, `.env.example`, `server.js`, and all the subdirectories: `config/`, `controllers/`, `models/`, `routes/`, `middleware/`, `utils/`). Name this file `backend.zip`.

---

## Phase 3: Setup Node.js Application in cPanel

cPanel uses a specialized **Node.js Selector** (usually powered by Phusion Passenger) to run JS applications in a sandbox.

### Step 1: Open the Node Selector
1. In cPanel, scroll down to the **Software** section and click on **Setup Node.js App**.
2. Click **Create Application**.

### Step 2: Configure the Selector
1. **Node.js Version**: Select the latest stable version (e.g., v18 or v20).
2. **Application Mode**: Change to **Production**.
3. **Application Root**: The folder name where you will upload your code (e.g., `beyondbridge_backend`).
4. **Application URL**: The domain/subdomain path where the APIs should reside (e.g., `api.yourdomain.com` or `yourdomain.com/api`).
5. **Application Startup File**: Enter `server.js`.
6. Click the **Create** button in the top right. This spins up the sandbox environment and generates an default starter `app.js` or startup configuration.

---

## Phase 4: Upload and Extract Node Code

1. Return to the main cPanel dashboard and open **File Manager**.
2. Navigate to the folder entered in **Application Root** (e.g., `beyondbridge_backend`).
3. Delete the default starter files if any were auto-generated.
4. Click **Upload**, choose your local `backend.zip` file, and upload it.
5. Select the uploaded `backend.zip` in File Manager, click **Extract**, and confirm.

---

## Phase 5: Configure Production Environments & Run

### Step 1: Write Production `.env`
1. Inside the root folder in File Manager, open and edit the `.env` file.
2. Fill in the parameters with your live cPanel credentials:
   ```env
   PORT=passenger  # Passenger (cPanel selector) maps port automatically!
   NODE_ENV=production

   # cPanel MySQL Configurations
   DB_HOST=localhost  # On cPanel, MySQL is almost always hosted locally!
   DB_PORT=3306
   DB_USER=yourcpaneluser_db_admin
   DB_PASS=your_strong_generated_password
   DB_NAME=yourcpaneluser_beyondbridge_db

   # JWT Configurations
   JWT_SECRET=generate_a_very_long_secure_secret_for_production_here
   JWT_LIFETIME=24h
   COOKIE_LIFETIME=1

   # SMTP Configurations (Recommended for sending real emails on cPanel)
   SMTP_HOST=mail.yourdomain.com  # Use your cPanel Webmail SMTP host!
   SMTP_PORT=465
   SMTP_USER=contact@yourdomain.com
   SMTP_PASS=your_email_password
   SMTP_FROM="Beyond Bridge Advisory <contact@yourdomain.com>"
   ```
3. Click **Save Changes**.

### Step 2: Install Node Packages
1. Go back to cPanel **Setup Node.js App** page.
2. Click **Edit** (pencil icon) on your application.
3. Scroll down and click the **Run npm install** button. This downloads and compiles all modules (including `bcryptjs` and `mysql2`) directly inside the host environment.
4. Once completed successfully, scroll to the top and click **Restart** to boot your live, production-ready backend!

---

## Troubleshooting Common cPanel Issues

* **Error: "502 Bad Gateway" or Phusion Passenger Error**:
  - This usually indicates a syntax error or crash on boot. Click the **Setup Node.js App** page, find the exact path of your application log file (typically under `stderr.log` or specified in the Node settings), and review it to identify missing variables or config typos.
* **Error: "Access denied for user '...'@'localhost'" inside `.env`**:
  - Double check your cPanel MySQL username and database name inside `.env`. On shared hosting, your database resources MUST be prefixed with your cPanel account username (e.g. `user_dbname` instead of just `dbname`).
* **Error: "#1044 - Access denied for user '...'@'localhost' to database 'beyondbridge_db'" during SQL Import**:
  - **Why this happens**: Shared hosting environments restrict database creation (`CREATE DATABASE`) and administration to the cPanel UI dashboard. They do not allow raw SQL queries to create databases or switch schemas via DDL commands (`CREATE DATABASE` / `USE`).
  - **Resolution**: Select your custom cPanel-created database in the left sidebar of phpMyAdmin first. Make sure your SQL import file has the `CREATE DATABASE` and `USE` statements commented out or removed (we have pre-commented them in `backend/schema.sql`).
* **Error: Mail not delivering**:
  - Ensure SMTP details match your cPanel email settings. Many shared hosts block standard SMTP ports (like `25` or `587`) for outbound emails to prevent spamming. Using **Port `465` (SSL)** is highly recommended.
