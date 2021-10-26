import factory
import factory.fuzzy

from data.entities import Category

class CategoryFactory(factory.Factory):

    class Meta:
        model = Category

    title = factory.Faker('name')
    body_html = factory.Faker('sentence')
    published = factory.fuzzy.FuzzyChoice([True, True, True, False])
    sort_order = "manual"
    image = factory.Faker('image_url')
