import sys

try:
    while True:
        fib = [0,1,1,2,3,5,8,13,5,2,7,9,0,9,9,2,11,13,8,5,13,2,15,1]

        # 入力に対応した数値を取り出す
        N = int(input())
        N = N % 24
        print(fib[N])

except EOFError:
    pass
