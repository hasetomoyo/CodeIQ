try:
    while True:
        N = int(input())
        result = 0
        i = 0
        # print("入力された数値：", N)

        # 入力された数値が0
        if N == 0:
            result = 0

        # 入力された数値が1
        if N == 1:
            result = 1

        # 2以上の数値
        a = 0
        b = 1
        if N > 1:
            for i in range(N-1):
                result = a + b
                a = b
                b = result
                # print("a:", a, "b:", b, "result:", result)

            # resultの結果が16以上の場合
            if result > 15:
                result = result % 16

        # print("回答：", result)
        print(result)

except EOFError:
    pass
