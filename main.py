# 1. 輸入 2 個整數
try:
    num1 = int(input("請輸入第一個整數: "))
    num2 = int(input("請輸入第二個整數: "))

    # 確保由小到大處理
    start = min(num1, num2)
    end = max(num1, num2)

    multiples = []
    total_sum = 0

    # 2. 計算 2 個整數之間所有 17 的倍數
    for i in range(start, end + 1):
        if i % 17 == 0:
            multiples.append(i)
            total_sum += i

    # 3. 輸出結果
    print(f"由小到大所有 17 的倍數為: {multiples}")
    print(f"總和 (Sum) = {total_sum}")

except ValueError:
    print("錯誤：請確保輸入的是整數。")
