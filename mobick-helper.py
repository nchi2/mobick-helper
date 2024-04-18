import itertools
from bitcoin import *

# 잘못된 자리의 인덱스와 프라이빗 키의 나머지 부분
wrong_indices = [0,1,2]  # 실제 인덱스로 교체 필요
partial_private_key = 'cdyf4daJyA1FRQYcBrUWPuU3SwiUvPCimnyCSD3h6pfu27LKHQts'  # 예시 키, 실제 값으로 대체 필요

# 가능한 모든 Base58 문자
base58_characters = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# 잘못된 각 자리에 대해 모든 가능한 Base58 문자를 대입
for combo in itertools.product(base58_characters, repeat=len(wrong_indices)):
    # 잘못된 자리에 문자 채우기
    test_key = list(partial_private_key)
    for idx, char in zip(wrong_indices, combo):
        test_key[idx] = char
    
    # 리스트를 문자열로 변환
    test_key_str = ''.join(test_key)
    
    # 프라이빗 키의 유효성 검사
    if is_privkey(test_key_str):
        print(f"Valid private key found: {test_key_str}")
        break  # 유효한 키를 찾으면 루프 종료
else:
    print("No valid private key found.")  # 유효한 키를 찾지 못한 경우
