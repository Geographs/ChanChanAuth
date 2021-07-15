import json

import requests

from chanchanauth.types import LicenseGenerationResponse, HWIDKeyGenerationResponse


class Admin(object):
    def __init__(self, aid: str, apikey: str, username: str, password: str):
        self.aid = aid
        self.apikey = apikey
        self.username = username
        self.password = password

    def generate_license(self, license_type: str = "", license_length: str = "", user_type: str = ""):
        try:
            response = requests.get(
                url=f"https://api.ccauth.app/api/v3/getkey?key={self.apikey}",
                headers={
                    "data": {
                        "type": license_type,
                        "time": license_length
                    },
                    "userType": user_type,
                    "aid": self.aid,
                    "pass": self.password,
                    "user": self.username
                }
            )
        except Exception:
            return LicenseGenerationResponse(
                error=True,
                error_message="Failed to connect to authentication server."
            )

        try:
            resp_dict = response.json()

            if response.status_code == 200:
                return LicenseGenerationResponse(
                    license=resp_dict["key"],
                    success=eval(resp_dict["success"])
                )
            else:
                return LicenseGenerationResponse(
                    error=True,
                    error_message=resp_dict["reason"]
                )
        except json.JSONDecodeError:
            return LicenseGenerationResponse(
                error=True,
                error_message="Failed to parse response."
            )
        except Exception:
            return LicenseGenerationResponse(
                error=True,
                error_message="Server returned something unexpected."
            )

    def generate_hwidkey(self):
        try:
            response = requests.get(
                url=f"https://api.ccauth.app/api/v2/gethwidkey?key={self.apikey}",
                headers={
                    "discord": "",
                    "user": self.username,
                    "pass": self.password,
                    "aid": self.aid
                }
            )
        except Exception:
            return HWIDKeyGenerationResponse(
                error=True,
                error_message="Failed to connect to authentication server."
            )

        try:
            resp_dict = response.json()

            if response.status_code == 200:
                return HWIDKeyGenerationResponse(
                    key=resp_dict["key"],
                    success=eval(resp_dict["success"])
                )
            else:
                return HWIDKeyGenerationResponse(
                    error=True,
                    error_message=resp_dict["reason"]
                )
        except json.JSONDecodeError:
            return HWIDKeyGenerationResponse(
                error=True,
                error_message="Failed to parse response."
            )
        except Exception:
            return HWIDKeyGenerationResponse(
                error=True,
                error_message="Server returned something unexpected."
            )
