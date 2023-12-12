## Registration
0. Install requirements:

* install SSL

after run:
```bash
pip install -r requirements.txt
```


1. Firstly create your private and public keys for monobank API. You can use the following commands
 
To create public key for monobank API, you need to use the following command:
```bash
make create_public_key
```

To create private key for monobank API, you need to use the following command:
```bash
make create_private_key
```

2. Registrate your keys and request access via:
```bash
python monobank/register.py
```

3. To check status of your request, you can use the following command:
```bash
python monobank/check_registration_status.py
```
