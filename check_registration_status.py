import requests

from monobank.base import BaseMonobankApiHelper


class CheckRequestStatus(BaseMonobankApiHelper):
    def __init__(self, path_to_public_key: str, path_to_private_key: str):
        super().__init__(path_to_public_key, path_to_private_key, "/personal/auth/registration/status")

    def check(self):
        response = self._get_data_from_api()
        data, status_code = response.json(), response.status_code

        print(f"Status code: {status_code}\n")
        if status_code == 200:
            print(f"Your request is {data.get('status')}")
            print(f"Your keyId: {data.get('keyId')}\n")
        else:
            print("Smth went wrong")
            print(f"More data: {response.text}")

    def _get_data_from_api(self):
        return requests.request(
            "POST",
            "https://api.monobank.ua/personal/auth/registration/status",
            json=self.base_auth_payload,
            headers=self.base_auth_headers,
        )


if __name__ == "__main__":
    public_key_path = "../keys/pub.pem"
    private_key_path = "../keys/private.pem"

    CheckRequestStatus(public_key_path, private_key_path).check()
