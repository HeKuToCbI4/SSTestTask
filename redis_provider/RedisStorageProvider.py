import redis

import config_data


class RedisStorageProvider:
    def __init__(self, host, port, db, **kwargs):
        self.r = redis.StrictRedis(host, port, db, **kwargs)

    def add_message_with_expiration(self, message, user_identifier, time_posted, expiration=config_data.message_ttl):
        self.r.setex(f'{user_identifier}_{time_posted}', expiration, {'user': user_identifier,
                                                                      'time_posted': time_posted,
                                                                      'message': message})
