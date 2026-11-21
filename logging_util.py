"""日志工具模块。"""
import logging


def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def log_execution_time(logger, operation_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = (time.time() - start) * 1000
            logger.info(f"{operation_name} took {elapsed:.2f}ms")
            return result
        return wrapper
    return decorator
