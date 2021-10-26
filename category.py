import logging

from client.shopify_client import ShopifyClient
from data.factories import CategoryFactory
from utils.constants import RequestTypes, ShopifyStoreAdmin

class CategoryMigration:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        logging.basicConfig(level = logging.INFO)

        self.client = ShopifyClient(
            api_password="YOUR_API_PASSWORD",
            shop_url="YOUR_SHOP_URL",
            endpoint=ShopifyStoreAdmin.COLLECTION_ENDPOINT.value
        )

    def generate_categories(self):
        category_data = CategoryFactory.create_batch(5)

        collections_shopify = []

        for category in category_data:
            collection_row = {
                "custom_collection" : {
                    "title": category.title,
                    "body_html": category.body_html,
                    "published": category.published,
                    "sort_order": category.sort_order,
                    "image": {"src": category.image }
                }
            }
            collections_shopify.append(collection_row)
        return collections_shopify
    
    def migrate(self):
        collections_shopify = self.generate_categories()
        for collect in collections_shopify:
            res = self.client.api_request(
                method=RequestTypes.POST.value,
                data=collect
            )
            self.log.info("Response %s", res)


categories_migration = CategoryMigration()
categories_migration.migrate()