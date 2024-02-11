import sys
from check_registration_status import CheckRequestStatus
from get_client_data import MonobankClient
from registration import Registration
from webhook import MonobankWebHook

PUBLIC_KEY_PATH = "./keys/pub.pem"
PRIVATE_KEY_PATH = "./keys/private.pem"

def printf(*args):
    print()
    print("*"*10)
    for arg in args:
        print(arg)
    print("*"*10)
    print()

def register():
    # todo add validations
    project_name = input("Enter project name: ")
    short_description_project = input("Enter short description project: ")
    contact_person_full_name = input("Enter contact person full name: ")
    contact_person_phone_number = input("Enter contact person phone number (+380000000000): ")
    contact_person_email = input("Enter contact person email: ")
    logo_path = input("Enter path to logo: ")

    response = Registration(
          PUBLIC_KEY_PATH, PRIVATE_KEY_PATH
    ).register(
          project_name=project_name,
          short_description_project=short_description_project,
          contact_person_full_name=contact_person_full_name,
          contact_person_phone_number=contact_person_phone_number,
          contact_person_email=contact_person_email,
          logo_path=logo_path,
    )
    printf("Registration response:", response.json(), response.status_code)
    return response

def check_registration():
    response = CheckRequestStatus(PUBLIC_KEY_PATH, PRIVATE_KEY_PATH).check()
    printf("Check registration status", response.json(), response.status_code)

def get_user_data():
    token = input("Enter user token: ")
    response = MonobankClient(PUBLIC_KEY_PATH, PRIVATE_KEY_PATH).get_client_info(token)
    printf("Client info:", response.json(), response.status_code)


def set_user_webhook():
    token = input("Enter user token: ")
    webhook_url = input("Enter webhook url: ")
    response = MonobankWebHook(PUBLIC_KEY_PATH, PRIVATE_KEY_PATH).set_hook(webhook_url, token)
    printf("Set webhook:", response.json(), response.status_code)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'register':
            register()
        elif command == 'check_registration':
            check_registration()
        elif command == 'get_user_data':
            get_user_data()
        elif command == 'set_user_webhook':
            set_user_webhook()
        else:
            print(f"Unknown command {command}")
    else:
        print("No command provided")