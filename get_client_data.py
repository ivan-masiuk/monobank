import requests

from base import BaseMonobankApiHelper


class MonobankClient(BaseMonobankApiHelper):
    def __init__(self, path_to_public_key: str, path_to_private_key: str):
        super().__init__(path_to_public_key, path_to_private_key, "/personal/client-info")

    def get_client_info(self, token: str):
        headers = self.base_auth_headers
        headers["X-Token"] = token

        response = requests.request(
            "GET",
            "https://api.monobank.ua/personal/client-info",
            json=self.base_auth_payload,
            headers=self.base_auth_headers,
        )
        return response
