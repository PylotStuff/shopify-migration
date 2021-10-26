from dataclasses import dataclass

@dataclass
class Category:
    title: str
    body_html: str
    published: bool
    sort_order: str
    image: str