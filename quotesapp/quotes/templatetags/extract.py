from django import template
from bson.objectid import ObjectId
from ..utils import get_mongo_client

register = template.Library()

@register.filter(name='author')
def get_author(_id):
    db = get_mongo_client()
    author = db.authors.find_one({'_id': ObjectId(_id)})
    return author['fullname'] if author else 'Unknown Author'