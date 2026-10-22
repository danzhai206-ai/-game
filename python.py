import random
while True:
 answer = random.randint(1, 100)
 count = 0
 while True:
   guess=int(input("数字を入力してください(1-100)："))
  
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
   
   

            
            
            
          