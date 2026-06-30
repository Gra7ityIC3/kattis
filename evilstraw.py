from collections import Counter

def min_swaps_to_palindrome(s):
    if sum(v % 2 for v in Counter(s).values()) > 1:
        return 'Impossible'

    s = list(s)
    swaps = 0

    left = 0
    right = len(s) - 1

    while left < right:
        # Find matching character for s[left], searching from the right
        k = right
        while k > left and s[k] != s[left]:
            k -= 1

        if k == left:
            # s[left] is the odd character; move it toward the middle
            s[k], s[k + 1] = s[k + 1], s[k]
            swaps += 1
        else:
            # Move matching character to the right side
            while k < right:
                s[k], s[k + 1] = s[k + 1], s[k]
                swaps += 1
                k += 1

            left += 1
            right -= 1

    return swaps


for _ in range(int(input())):
    print(min_swaps_to_palindrome(input()))