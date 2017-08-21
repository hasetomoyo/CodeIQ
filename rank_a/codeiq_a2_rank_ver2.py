import sys

try:
    while True:
        N = int(input())
        nyuryoku_lines = []
        # for line in sys.stdin:
        for i in range(N):
            nyuryoku_lines.append(input())
        # print(nyuryoku_lines)

        # 0,1の値を格納
        fib = []
        fib.append(0)
        fib.append(1)

        # 2以降の数字を計算して格納
        a = 0
        b = 1
        for i in range(100):
            result = a + b
            a = b
            b = result

            # resultの結果が16以上の場合
            if result > 15:
                result = result % 16

            fib.append(result)

        # 回答を取り出す
        #　for i in range(10000000):
        #     N = int(input())
        #     print(fib[N])
        for i in range(len(nyuryoku_lines)):
            tmp = int(nyuryoku_lines[i])
            print(fib[tmp])

except EOFError:
    pass
