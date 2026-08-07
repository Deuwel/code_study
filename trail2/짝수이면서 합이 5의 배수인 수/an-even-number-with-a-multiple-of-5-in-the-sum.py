n = int(input())

def is_answer_number(k):
    kSum = sum(list(map(int, str(k))))
    if kSum % 5 == 0 and n % 2 == 0:
        return True
    return False

print("Yes") if is_answer_number(n) else print("No")