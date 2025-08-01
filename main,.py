
import random
def games():
    while True:
        user = int(input("Enter your number :"))
        print(f"You choose {user}")

        data = random.randint(1,101)
        print(f"The random number chosse by computer is {data}")

        if user == data :
            print("Yoou are winner")
        elif abs(user-data)<=20 :
            print("You are close but you lost")
        else:
            print("you are looser")

            user_s=input("Enter exit for ending this game  and press enter to continue")
            if user_s.lower() == 'exit':
                print("thanks for playing")
                break
            
games()


