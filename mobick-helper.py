import itertools
from bitcoin import *

def find_valid_private_key(base_key, max_index, indices):
    base58_characters = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    # 주어진 인덱스에 대해 모든 가능한 Base58 문자를 대입
    for combo in itertools.product(base58_characters, repeat=len(indices)):
        test_key = list(base_key)
        for idx, char in zip(indices, combo):
            test_key[idx] = char
        test_key_str = ''.join(test_key)
        if is_privkey(test_key_str):
            print(f"Valid private key found: {test_key_str}")
            return True  # 유효한 키를 찾으면 True 반환
    return False  # 유효한 키를 찾지 못하면 False 반환

# 초기 설정
partial_private_key = '프라이빗키'
initial_indices = [1, 2, 3]
max_index = len(partial_private_key) - 1

# 초기 인덱스 세트에서 시작
if not find_valid_private_key(partial_private_key, max_index, initial_indices):
    # 초기 세트가 실패하면 다른 조합 시도
    for i in range(max(initial_indices) + 1, max_index + 1):
        new_indices = initial_indices[:-1] + [i]
        if find_valid_private_key(partial_private_key, max_index, new_indices):
            break
    else:
        print("No valid private key found after trying all combinations.")
