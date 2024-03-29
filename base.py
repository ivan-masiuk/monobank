import time
import base64
import hashlib
from datetime import datetime
from ecdsa import SigningKey


class BaseMonobankApiHelper:
    def __init__(self, path_to_public_key: str, path_to_private_key: str, url: str):
        self.url = url

        self.path_to_public_key = path_to_public_key
        self.path_to_private_key = path_to_private_key
        self._check_if_keys_exists()

        self.time_now = str(self.to_timestamp(datetime.now()))

        self.base_auth_headers = self.get_base_auth_headers()
        self.base_auth_payload = self.get_base_auth_payload()

    def _check_if_keys_exists(self):
        if not self.path_to_public_key or not self.path_to_private_key:
            raise Exception("Path to public or private key is not set!")

        try:
            with open(self.path_to_public_key, "rb") as pubkey_file:
                pubkey_file.read()
        except FileNotFoundError:
            raise Exception("Public key file not found!")

        try:
            with open(self.path_to_private_key, "rb") as privkey_file:
                privkey_file.read()
        except FileNotFoundError:
            raise Exception("Private key file not found!")

    @staticmethod
    def to_timestamp(dtime):
        """Converts datetime to utc timestamp"""
        return int(time.mktime(dtime.timetuple()))

    def get_base_auth_headers(self) -> dict:
        return {
            "X-Time": self.time_now,
            "X-Sign": self._get_x_sign(),
        }

    def get_base_auth_payload(self) -> dict:
        return {
            "pubkey": self._get_pubkey(),
        }

    def _get_pubkey(self):
        with open(self.path_to_public_key, "rb") as pubkey_file:
            return base64.b64encode(pubkey_file.read()).decode("utf-8")

    def _get_x_sign(self):
        data = (self.time_now + self.url).encode("utf-8")

        with open(self.path_to_private_key) as f:
            sk = SigningKey.from_pem(f.read(), hashfunc=hashlib.sha256)

        sign = sk.sign(data, hashfunc=hashlib.sha256)
        signB64 = base64.b64encode(sign).decode("utf-8")
        return signB64
