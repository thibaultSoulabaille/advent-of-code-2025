import time


def split_string_by_block(input_str: str, block_len: int) -> list[str]:
    return [input_str[i : i + block_len] for i in range(0, len(input_str), block_len)]


def check_time(func):
    def wrapper(*args, **kwargs):
        tic = time.time()
        res = func(*args, **kwargs)
        toc = time.time()
        print(f"{func.__name__} execution time: {toc - tic:.6f} sec")
        return res

    return wrapper
