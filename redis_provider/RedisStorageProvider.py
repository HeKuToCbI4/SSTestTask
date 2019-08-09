import threading
import time

import redis

import config_data


class RedisStorageProvider:
    def __init__(self, host, port, db, **kwargs):
        self.r = redis.StrictRedis(host, port, db, **kwargs)
        self.r.execute_command('config set notify-keyspace-events KEA')
        self.pub_sub = None
        self.server_thread = None
        self.callbacks = []

    def add_message_with_expiration(self, message, user_identifier, time_posted, expiration=config_data.message_ttl):
        self.add_key_value_pair(f'{user_identifier}_{time_posted}', {'user': user_identifier,
                                                                     'time_posted': time_posted,
                                                                     'message': message}, expiration)

    def serve_subscribed_messages(self, pubsub):
        while True:
            message = pubsub.get_message()
            if message is not None:
                print(message)
                for callback, filters in self.callbacks:
                    if message['data'] in filters:
                        callback(message)
            else:
                time.sleep(0.025)

    def remove_key(self, key):
        self.r.delete(key)

    def add_key_value_pair(self, key, value, expiration=None):
        self.r.hmset(key, value)
        self.r.expire(key, expiration)

    def subscribe_to_events(self, channel: str = '__keyspace@0__:*'):
        if self.pub_sub is None:
            self.pub_sub = self.r.pubsub()
        self.pub_sub.psubscribe(channel)
        if self.server_thread is None:
            self.server_thread = threading.Thread(target=self.serve_subscribed_messages, args=(self.pub_sub,),
                                                  daemon=True)
            self.server_thread.start()

    def register_callback(self, callback, data_filters):
        self.callbacks.append((callback, data_filters))

    def disconnect(self):
        pass

    def clear_db(self):
        self.r.flushall()
