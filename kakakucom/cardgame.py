import sys
import itertools

try:
    while True:
        # 対戦相手の合計点
        total_point_of_opponent = int(input())

        # 手元のカードの点数
        card_pattern = []
        while True:
            n = input()
            if n == '':
                break
            card_pattern.append(n)

        print('相手のカード合計:', total_point_of_opponent)
        print('手もとのカード:', card_pattern)
        print('手元のカード数', len(card_pattern))

        count = 0

        if len(card_pattern) == 1:
            if total_point_of_opponent < card_pattern[0]:
                count = count + 1
        else:
            card_combination = []
            for i in range(1, len(card_pattern)+1):
                # 組み合わせを計算
                # card_combination.extend(itertools.combinations(card_pattern, i))
                card_combination = list(itertools.combinations(card_pattern, i))
                print(card_combination)

            # for j in range(0, len(card_combination)):
            #     print(card_combination(j))








except EOFError:
    pass
