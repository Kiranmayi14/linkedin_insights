import redis

cache = redis.Redis(host="localhost", port=6379, db=0)

def get_cached_data(key):
    return cache.get(key)

def set_cached_data(key, value, ttl=300):
    cache.set(key, value, ex=ttl)