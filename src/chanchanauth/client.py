import json
from uuid import uuid4

import requests
from cryptography.fernet import Fernet, InvalidToken

from chanchanauth.types import AuthenticationResponse, RegistrationResponse, HWIDResetResponse


class Client(object):
    def __init__(self, aid: str, apikey: str, secret: str = None):
        self.aid = aid
        self.apikey = apikey
        self.fernet = None if secret is None else Fernet(bytes(secret, "utf-8"))

    def authenticate(self, username: str, password: str, hwid: str):
        if self.fernet is None:
            raise ValueError("`secret` must not be none if you are authenticating.")

        try:
            response = requests.get(
                url=f"https://api.ccauth.app/api/v3/authenticate?key={self.apikey}",
                headers={
                    "aid": self.aid,
                    "data": self.fernet.encrypt(bytes(str({
                            "username": username,
                            "password": password,
                            "hwid": hwid,
                            "sessionID": str(uuid4())
                    }).replace("\'", "\""), "utf-8")).decode()
                }
            )
        except Exception:
            return AuthenticationResponse(
                error=True,
                error_message="Failed to connect to authentication server."
            )

        try:
            resp_dict = json.loads(self.fernet.decrypt(bytes(response.text, "utf-8")).decode())

            if response.status_code == 200:
                return AuthenticationResponse(
                    is_authenticated=eval(resp_dict["is_Authenticated"]),
                    session_id=resp_dict["session_ID"],
                    expired_license=eval(resp_dict["expired_license"]),
                    invalid_hwid=eval(resp_dict["invalid_hwid"]),
                    invalid_credentials=eval(resp_dict["invalid_credentials"]),
                    account_type=resp_dict["accountType"]
                )
            else:
                return AuthenticationResponse(
                    error=True,
                    error_message=resp_dict["type"]
                )
        except InvalidToken:
            resp_dict = response.json()
            return AuthenticationResponse(
                error=eval(resp_dict["error"]),
                error_message=resp_dict["type"]
            )
        except Exception:
            return AuthenticationResponse(
                error=True,
                error_message="Failed to parse response."
            )

    def register(self, username: str, password: str, hwid: str, discord: str, license: str):
        try:
            response = requests.get(
                url=f"https://api.ccauth.app/api/v2/register?key={self.apikey}",
                headers={
                    "aid": self.aid,
                    "discord": discord,
                    "regkey": license,
                    "hwid": hwid,
                    "pass": password,
                    "user": username
                }
            )
        except Exception:
            return RegistrationResponse(
                error=True,
                error_message="Failed to connect to authentication server."
            )

        try:
            resp_dict = response.json()

            if response.status_code == 200:
                return RegistrationResponse(
                    registration_enabled=eval(resp_dict["registration_enabled"]),
                    invalid_key=eval(resp_dict["invalid_key"]),
                    success=eval(resp_dict["success"]),
                    max_users=eval(resp_dict["max_users"])
                )
            else:
                return RegistrationResponse(
                    error=True,
                    error_message=resp_dict["type"]
                )
        except json.JSONDecodeError:
            return RegistrationResponse(
                error=True,
                error_message="Failed to parse response."
            )
        except Exception:
            return RegistrationResponse(
                error=True,
                error_message="Server returned something unexpected."
            )

    def hwid_reset(self, username: str, password: str, hwid: str, hwid_key: str):
        try:
            response = requests.get(
                url=f"https://api.ccauth.app/api/v3/reset?key={self.apikey}",
                headers={
                    "hwidresetkey": hwid_key,
                    "aid": self.aid,
                    "newhwid": hwid,
                    "user": username,
                    "pass": password
                }
            )
        except Exception:
            return HWIDResetResponse(
                error=True,
                error_message="Failed to connect to authentication server."
            )

        try:
            resp_dict = response.json()

            if response.status_code == 200:
                return HWIDResetResponse(
                    hwid_resets=eval(resp_dict["hwid_resets"]),
                    invalid_key=eval(resp_dict["invalid_key"]),
                    invalid_credentials=eval(resp_dict["invalid_credentials"]),
                    success=eval(resp_dict["success"]),
                    reset_today=eval(resp_dict["reset_today"])
                )
            else:
                return HWIDResetResponse(
                    error=True,
                    error_message=resp_dict["type"]
                )
        except json.JSONDecodeError:
            return RegistrationResponse(
                error=True,
                error_message="Failed to parse response."
            )
        except Exception:
            return HWIDResetResponse(
                error=True,
                error_message="Server returned something unexpected."
            )
