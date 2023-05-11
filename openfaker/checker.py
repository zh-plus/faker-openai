def total_num_check(result, num):
    if result['total_num'] != num:
        raise ValueError(f"Expected {num} addresses, but got {result['num']} addresses.")
