import requests

code = "the-code-from-the-redirect"

token_response = requests.post(
    "https://oauth.battle.net/token",
    data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    },
    auth=(client_id, client_secret),
    timeout=10,
)

token_response.raise_for_status()
access_token = token_response.json()["access_token"]

profile_response = requests.get(
    "https://eu.api.blizzard.com/profile/user/wow",
    params={
        "namespace": "profile-eu",
        "locale": "en_GB",
        "access_token": access_token,
    },
    timeout=10,
)

profile_response.raise_for_status()
print(profile_response.json())