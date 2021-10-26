import json
import requests

from utils.constants import RequestTypes, ShopifyDefaults

class ShopifyClient:

    def __init__(self, api_password: str, shop_url: str, endpoint: str):
        self.api_password = api_password
        self.shop_url = shop_url
        self.endpoint = endpoint
        self.headers = {
            "Accept": 'application/json',
            "Content-Type": 'application/json'
        }
    
    def api_request(self, *args, **kwargs):
        self.headers.update({
          "X-Shopify-Access-Token": self.api_password
        })

        context = {
            "method": kwargs.get("method"),
            "url": f"{self.shop_url.rstrip('/')}{self.endpoint}",
            "timeout": 60,
            "headers": self.headers
        }

        if kwargs.get("method") == "POST":
            context["data"] = json.dumps(kwargs.get("data"))
        
        return requests.request(**context).json()