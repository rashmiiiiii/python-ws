def is_prime(nums):
    if nums<2:
        return False
    else:
        for i in range(2, nums // 2 + 1):
            if nums % i == 0:
                return False
        return True        

nums = [i for i in range(1,201)]
lst =list(filter( is_prime,nums)) 
print(lst)