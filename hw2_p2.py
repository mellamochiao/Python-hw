def is_perfect(number):
    divisor_sum = 1  # divisor_sum : 所有的因數相加，從1開始加
    divisor = 2      # 從2開始檢查是否可除
    while divisor * divisor <= number:  # 為了避免重複計算因數，只檢查比較小那側的因數
        if number % divisor == 0:       # 若可整除
            divisor_sum += divisor      # 除數為因數，加入divisor_sum  
            if divisor != number // divisor:        # 若可整除且兩個因數不同
                divisor_sum += number // divisor    # 把商也加入divisor_sum 
        divisor += 1
    return divisor_sum == number    # 當divisor_sum == number時就是答案

# Main program
try:
    n = int(input("Enter a number: "))
    if n < 2:
        print("Please enter a number greater than or equal to 2.")
    else:
        print("Perfect numbers : ")
        num = 2
        while num <= n:
            if is_perfect(num):
                print(num)
            num += 1
except ValueError:
    print("Please enter a valid integer.")
