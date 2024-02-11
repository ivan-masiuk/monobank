import requests

from base import BaseMonobankApiHelper


class MonobankWebHook(BaseMonobankApiHelper):
    """
    Use this for setting up a webhook for a user.
    """
    def set_hook(self, web_hook_url, x_sign):
        payload = self.get_base_auth_payload()
        payload["webHookUrl"] = web_hook_url

        headers = self.base_auth_headers
        headers["X-Token"] = x_sign

        return requests.request(
            "POST",
            "https://api.monobank.ua/personal/webhook",
            json=payload,
            headers=headers,
        )
