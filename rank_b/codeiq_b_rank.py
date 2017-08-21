try:
    while True:
        N,M = map(int, input().split())
        all_count = 0

        for i in range(0,N+1):
            count = 0
            tmp_num = format(i,'b')
            # print(tmp_num)

            stmp_num = list(map(str, tmp_num))

            for j in range(len(stmp_num)):
                if stmp_num[j] == '1':
                    count = count + 1

            # print('1の数:', count)

            if count == M:
                all_count = all_count + 1

        # print('1の数が一致したもの:', all_count)
        print(all_count)

except EOFError:
    pass
