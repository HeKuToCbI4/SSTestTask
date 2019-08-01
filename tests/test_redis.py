import redis

import config_data


class TestRedis:
    def test_connection(self):
        r_conn = redis.StrictRedis(host=config_data.vm_ip, port=config_data.redis_port, db=0, socket_connect_timeout=10)
        r_conn.ping()
