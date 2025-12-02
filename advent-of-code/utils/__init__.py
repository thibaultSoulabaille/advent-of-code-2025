def split_string_by_block(input_str: str, block_len: int) -> list[str]:
    return [input_str[i : i + block_len] for i in range(0, len(input_str), block_len)]
