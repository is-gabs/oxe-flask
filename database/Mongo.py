from pymongo import MongoClient, uri_parser
from api.utils.ENV import envs

mongo_url = uri_parser.parse_uri(envs.MONGO_URL)

client = MongoClient(host=envs.MONGO_URL)

db = client.get_database(mongo_url['database'])
