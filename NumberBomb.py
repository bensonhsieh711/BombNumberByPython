from random import randint
print("數字爆爆王開始....")
isGameOver = False
minNum = 0
maxNum = 100
bombNumber = randint(minNum, maxNum)

while isGameOver == False:
    guessNumber = input(f"輸入{minNum}~{maxNum}內任一數字:")

    try:
        guessNumber = int(guessNumber)

        if guessNumber > maxNum or guessNumber < minNum:
            print("輸入數字範圍錯誤！")
        elif guessNumber == bombNumber:
            print(f"BOOM！爆爆數字為{bombNumber}！")
            isGameOver = True
        elif guessNumber == minNum and guessNumber != minNum + 1:
            minNum = minNum + 1
        elif guessNumber == maxNum and guessNumber != maxNum - 1:
            maxNum = maxNum - 1                
        elif guessNumber > minNum and guessNumber < bombNumber:
            minNum = guessNumber
        else:
            maxNum = guessNumber
    except:
        print("請輸入數字！")
