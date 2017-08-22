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
        print('手元のカード数:', len(card_pattern), '枚')

        number_of_victories = 0

        card_combination = []
        for i in range(1, len(card_pattern) + 1):
            card_combination = list(itertools.combinations(card_pattern, i))
            print(i, '個取り出した場合の組み合わせ:', card_combination)
            print(i, '個取り出した場合の組み合わせ数:', len(card_combination))

            # 1つ以上の組み合わせ
            if i == 1:
                for j in range(len(card_combination)):
                    tmp_num = int(card_combination[j][0])
                    print(j + 1, 'つめ：', tmp_num)

                    if tmp_num > total_point_of_opponent:
                        print('勝ち！')
                        number_of_victories = number_of_victories + 1
                    else:
                        print('負け！')

            # 2つ以上の組み合わせ
            else:
                print('2つ以上！')

                for count in range(len(card_combination)):
                    print('count:', count)
                    print(card_combination[count])

                    temp_score = 0
                    for x in range(i):
                        temp_score = temp_score + int(card_combination[count][x])
                        print(x,': temp_score', temp_score)

                    if temp_score > total_point_of_opponent:
                        number_of_victories = number_of_victories + 1

        print('勝利回数:', number_of_victories)

except EOFError:
    pass
