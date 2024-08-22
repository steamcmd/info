from main import app, logger
import config
import redis
import logging
import os


def connect():
    """
    Parse redis config and connect.
    """

    try:
        rds = redis.Redis(host=config.redis_host, port=config.redis_port)

    except Exception as error:
        logging.error("Failed to connect to Redis with error: " + error)
        return False

    return rds


def read(key):
    """
    Read specified key from Redis.
    """

    rds = connect()
    data = rds.get(key)

    if not data:
        return False
    data = data.decode("UTF-8")

    return data


def write(key, data):
    """
    Write specified key to Redis.
    """

    rds = connect()
    rds.set(key, data)

    return True
