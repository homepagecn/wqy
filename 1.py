# 基本流程

# 1. 顺序
def t1():
    print("  *  ")
    print(" *** ")
    print("*****")

# 2. 循环
def t2(rows=5):
    # i 代表当前行数
    for i in range(0, rows):  # [0, 1, 2, 3, 4]
        str = ""
        # [0, 1, 2, 3] #[0, 1, 2] # [0, 1] # [0]
        for j in range(0, rows - i - 1):
            str = str + " "
        for j in range(0, i * 2 + 1):
            str = str + "*"
        for j in range(0, rows - i - 1):
            str = str + " "
        print(str)


# 3. 判断
def t3(rows=5):
    # i 代表当前行数
    for i in range(0, rows):  # [0, 1, 2, 3, 4]
        str = ""
        # [0, 1, 2, 3] #[0, 1, 2] # [0, 1] # [0]
        for j in range(0, rows - i - 1):
            str = str + " "
        for j in range(0, i * 2 + 1):
            if i % 2 == 0:
                str = str + "\033[0;31m*\033[0m"
            else:
                str = str + "*"
        for j in range(0, rows - i - 1):
            str = str + " "
        print(str)


t3(100)
