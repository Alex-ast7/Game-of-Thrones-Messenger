import time
result = 1000
while result > 0:
    print(f'{result} - 7 = {eval(f"{result} - 7")}')
    result = result - 7
    time.sleep(0.03)