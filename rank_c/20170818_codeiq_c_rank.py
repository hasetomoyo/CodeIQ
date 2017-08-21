import itertools

try:
    while True:
        N = int(input())
        numbers = map(int, input().split())
        result = ''
        i = 0

        # 整数が2個の場合
        if N == 2:
            lists = list(numbers)
            sum_reg = lists[0] + lists[1]
            
            if sum_reg == 256:
                result = 'yes'

        # 組み合わせの計算
        else:
            lists = list(itertools.combinations(numbers, 2))
            # print(lists)

            # 配列1つ1つを足してみて、256になればyesを設定
            for string in range(len(lists)):
                sum_reg = lists[i][0] + lists[i][1]
                i = i + 1
                # print(sum_reg)

                if sum_reg == 256:
                    result = 'yes'
                    break

        # 結果出力
        # yseが格納されていなければnoを出力
        if result == 'yes':
            print('yes')
        else:
            print('no')

except EOFError:
    pass
