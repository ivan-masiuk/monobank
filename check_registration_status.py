import requests

from base import BaseMonobankApiHelper


class CheckRequestStatus(BaseMonobankApiHelper):
    def __init__(self, path_to_public_key: str, path_to_private_key: str):
        super().__init__(path_to_public_key, path_to_private_key, "/personal/auth/registration/status")

    def check(self):
        return self._get_data_from_api()

    def _get_data_from_api(self):
        return requests.request(
            "POST",
            "https://api.monobank.ua/personal/auth/registration/status",
            json=self.base_auth_payload,
            headers=self.base_auth_headers,
        )
