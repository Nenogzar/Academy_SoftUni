from collections import deque

rows, cols = map(int, input().split())
word = list(input())
word_queue = deque(word)



for row in range(rows):
    while len(word_queue) < cols:
        word_queue.extend(word)

    if row % 2 == 0:
        print(*[word_queue.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_queue.popleft() for _ in range(cols)][::-1], sep="")