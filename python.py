import random
import sys
level=input("難易度を選択してください")
if level=="1":
     max_number=20
elif level=="2":
     max_number=100
elif level=="3":
     max_number=500
else:
     print("無効な選択です。")
     sys.exit()

while True:
 answer = random.randint(1, max_number)
 count = 0
 while True:
   guess=int(input(f"数字を入力してください(1-{max_number})："))
  
   count+=1
   if guess<answer:
      print("もっと大きい！")
   elif guess>answer:
            print("もっと小さい！")
   else:
            print(f"正解です！試行回数は {count} 回です。")
            break
   if count==5:
            print("失敗です。GG")
            break
 again=input("continue?(y/n):")
 if again=="n":
    break
   
   

            
            
            
          