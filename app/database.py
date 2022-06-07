"""
Подключение к Mongo DB.
"""

from abc import abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from app import logger

logger = logger.getChild('api.database')


class DatabaseManager(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @property
    def faq(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str, database: str, collection_name: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None
    faq: AsyncIOMotorCollection = None
    user: AsyncIOMotorCollection = None

    async def connect_to_database(self, path: str, database: str, collections_name: list):
        self.client = AsyncIOMotorClient(path, maxPoolSize=10, minPoolSize=10)
        logger.info("Connected to MongoDB.")
        self.db = self.client[database]
        faq_, _ = collections_name
        self.faq = self.db[faq_]
        logger.info(f"MongoDB set db=[{database}], collections=[{collections_name}].")

    async def close_database_connection(self):
        logger.info("Closing connection with MongoDB.")
        self.client.close()
        logger.info("Closed connection with MongoDB.")


db = MongoManager()


async def get_database() -> DatabaseManager:
    return db
