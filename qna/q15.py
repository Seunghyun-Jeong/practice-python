def check(n):
    result = []
    for num in n:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10
