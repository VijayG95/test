def check_self_divisible(num):

    org_num = num
    sum = 0
    while num > 0:
        sum = sum + (num % 10)
        num = num // 10
    print(org_num,sum)
    if org_num % sum == 0:
        return True
    else:
        return False

a = check_self_divisible(1729)
print(a)