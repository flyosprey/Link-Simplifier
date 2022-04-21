import json
import requests


API_SECRET_KEY = "sk_oygUozuP70uqnEIf"


def simplify_url(original_url) -> str:
    api_url = "https://api.short.io/links"
    payload = {
        "domain": "3g3h.short.gy",
        "originalURL": original_url,
        "allowDuplicates": False,
        "cloaking": False,
        "redirectType": 302
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": API_SECRET_KEY
    }
    response = requests.request("POST", api_url, json=payload, headers=headers)
    json_data = json.loads(response.text)
    simplified_url = json_data["shortURL"]
    return simplified_url
