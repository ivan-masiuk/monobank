Registration and Setup Guide for Monobank API
=============================================

This guide provides step-by-step instructions on how to register and configure your application with the Monobank API,
including the creation of SSL keys, virtual environment setup, and installation of dependencies.

## Useful Links:
* [Docs](https://api.monobank.ua/docs/)
* [Unofficial chat](https://t.me/monobankunofficial)

Prerequisites
-------------

* SSL (OpenSSL) must be installed on your operating system.

Installation and Configuration
------------------------------

### Step 0: Install Requirements

1. **Install SSL (OpenSSL) for your OS.**

2. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```
    
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### Step 1: Create Your Private and Public Keys for Monobank API

To interact with the Monobank API, you need to generate your private and public keys. Use the following command to
create them:

```bash
make create_keys
```

### Step 2: Register Your Keys and Request Access

After creating your keys, you need to register them with the Monobank API and request access. Execute the following
command:

```bash
python manage.py register
```

### Step 3: Check the Status of Your Request

You can check the status of your registration request by running:

```bash
python manage.py check_registration
```

After your request is approved, you will receive a message with the status of your request and the time it was approved.

# What You Can Do After Approval

### Set Webhook for User Account

To set up a webhook for user account notifications, use the command below:

```bash
python manage.py set_user_webhook
```

### Get User Account Information

To set up a webhook for user account notifications, use the command below:

```bash
python manage.py get_user_info
```

### More Methods you can find in the [official documentation](https://api.monobank.ua/docs/)

## Good Luck! 🚀


_PS: some useful helpers with mcc you can find in `mcc_helpers` directory_
