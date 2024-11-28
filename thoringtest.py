words = {input().lower() for _ in range(int(input()))}
for word in input().split():
    if word.lower() not in words:
        print('Thore has left the chat')
        break
else:
    print('Hi, how do I look today?')