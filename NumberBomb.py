from random import randint
print("數字爆爆王開始....")
isGameOver = False
minNum = 0
maxNum = 100
bombNumber = randint(minNum, maxNum)

while isGameOver == False:
    if minNum == maxNum:
        print(f"沒得猜了！爆爆數字為{minNum}！")
    else:
        guessNumber = input(f"輸入{minNum}~{maxNum}內任一數字:")

        try:
            guessNumber = int(guessNumber)

            if guessNumber > maxNum or guessNumber < minNum:
                print(f"請輸入{minNum}~{maxNum}內任一數字！")
            elif guessNumber == bombNumber:
                print(f"BOOM！爆爆數字為{bombNumber}！")
                isGameOver = True         
            elif guessNumber >= minNum and guessNumber < bombNumber:
                minNum = guessNumber + 1
            else:
                maxNum = guessNumber - 1
        except:
            print("請輸入正確數字！")
