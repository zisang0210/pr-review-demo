"""工具函数模块。"""
import hashlib
import os


def hash_password(password: str) -> str:
    """对密码做 SHA256 哈希。"""
    return hashlib.sha256(password.encode()).hexdigest()


def generate_token() -> str:
    """生成随机 token。"""
    return os.urandom(32).hex()


def format_size(size_bytes: int) -> str:
    """格式化文件大小。"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def retry(times: int):
    """重试装饰器。"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:
                        raise
                    print(f"retry {i+1}/{times}: {e}")
        return wrapper
    return decorator
