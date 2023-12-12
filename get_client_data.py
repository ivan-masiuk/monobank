import requests

from monobank.base import BaseMonobankApiHelper


class MonobankClient(BaseMonobankApiHelper):
    def get_client_info(self, token: str) -> dict:
        headers = self.base_auth_headers
        headers["X-Token"] = token

        response = requests.request(
            "GET",
            "https://api.monobank.ua/personal/client-info",
            json=self.base_auth_payload,
            headers=self.base_auth_headers,
        )
        self.print_data(response)
        return response.json()

    @staticmethod
    def print_data(response):
        data, status_code = response.json(), response.status_code

        print(f"Status code: {status_code}\n")
        print(f"Data:\n{response.text}")


if __name__ == "__main__":
    MonobankClient(
        "../keys/pub.pem",
        "../keys/private.pem",
    ).get_client_info(
        "key",
    )
