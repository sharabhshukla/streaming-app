from faststream import FastStream
from faststream.redis import RedisBroker
from loguru import logger

broker = RedisBroker(host="redis-svc", port=6379)
app = FastStream(broker=broker, logger=logger)


@broker.subscriber(channel="opt_app")
def print_sub_messages(msg: str):
    """

    :param msg:
    """
    logger.info(msg)
    return "done"
