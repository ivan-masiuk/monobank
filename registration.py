import base64
import requests

from base import BaseMonobankApiHelper


class Registration(BaseMonobankApiHelper):
    def __init__(self, path_to_public_key: str, path_to_private_key: str):
        super().__init__(path_to_public_key, path_to_private_key, "/personal/auth/registration")

    @staticmethod
    def get_logo(logo_path: str):
        # check if file exists
        try:
            with open(logo_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except FileNotFoundError:
            raise Exception("File with your logo not found!")

    def register(
            self,
            project_name: str,
            short_description_project: str,
            contact_person_full_name: str,
            contact_person_phone_number: str,
            contact_person_email: str,
            logo_path: str,
    ):
        payload = self.get_base_auth_payload()
        payload.update(
            {
                "name": project_name,
                "description": short_description_project,
                "contactPerson": contact_person_full_name,
                "phone": contact_person_phone_number,
                "email": contact_person_email,
                "logo": self.get_logo(logo_path),
            }
        )

        response = requests.request(
            "POST",
            "https://api.monobank.ua/personal/auth/registration",
            json=payload,
            headers=self.base_auth_headers,
        )
        return response
