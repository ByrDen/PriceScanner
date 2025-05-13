from polyfactory.factories.pydantic_factory import ModelFactory

from app.models import Product


class ProductInputFactory(ModelFactory[Product]):
    ...