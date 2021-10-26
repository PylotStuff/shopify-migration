from enum import Enum

class ShopifyDefaults(Enum):
    SHOPIFY_API_VERSION = "2021-10"
    SHOPIFY_API_HEADER = "X-Shopify-Access-Token"


class ShopifyStoreAdmin(Enum):
    COLLECTION_ENDPOINT = "/admin/api/2021-10/custom_collections.json"

class RequestTypes(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"