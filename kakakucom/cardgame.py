import sys

try:
    while True:
        Total_point_of_opponent = int(input())

        card_pattern = []
        for line in range(sys.stdin):
            card_pattern.append(line)

        print(Total_point_of_opponent)
        print(card_pattern)

except EOFError:
    pass
