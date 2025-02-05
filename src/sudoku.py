import pandas, random

def make_board():
    board = []
    for row in range(1):
        nums = [1,2,3,4,5,6,7,8,9]
        for _ in range(9):
            num = random.choice(nums)
            nums.remove(num)
            board.append(num)


    print(board)

make_board()