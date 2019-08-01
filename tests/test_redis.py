import redis
from redis_provider import RedisStorageProvider
import config_data


class TestRedis:
    def test_connection(self):
        connection = redis.StrictRedis(host=config_data.vm_ip, port=config_data.redis_port, db=0,
                                           socket_connect_timeout=10)
        connection.ping()

class TestStorageProvider:
    provider: RedisStorageProvider.RedisStorageProvider
    @classmethod
    def setup_class(cls):
        cls.provider = RedisStorageProvider.RedisStorageProvider(config_data.vm_ip, config_data.redis_port, db=1)

    @classmethod
    def teardown_class(cls):
        cls.provider.clear_db()

    def test_subscription(self):
        import time
        filters = [b'set', b'expire']
        def callback(message):
            assert message['data'] in filters
        self.provider.subscribe_to_events()
        self.provider.register_callback(callback, filters)
        self.provider.add_message_with_expiration('woo', 'someusr', 'now', expiration=5)
        time.sleep(4)

