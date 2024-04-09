# 예외 알려주기.
raise Exception
# 예외 원인 같이 알려주기.
raise Exception('the door is not open')

# 값 오류.
raise ValueError
age = 15
raise ValueError(f'Too Young {age=}')