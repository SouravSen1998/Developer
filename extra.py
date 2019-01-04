print('Rules of the game....\n 1)You have to choose a value between 1 to 50 \n '
      '2)You will get only 5 chances\n 3)You will get hint at every step')
my_num=40
answer='yes'
while answer == 'yes':
    for chose in range(1,6):
        if chose==5:
            print('Warning!! This is your last try')
        print("choose yoour gussing number: ")
        gussing_num=int(input())
        if gussing_num==my_num:
            print("you win")
            break
        elif gussing_num+10<my_num:
            print("too low")
        elif gussing_num-10>my_num:
            print('too high')
        elif gussing_num<my_num:
            print('you are about to get it, little higher')
        elif gussing_num>my_num:
            print('you are about to get it, little lower')
        else:
            print('Check what you entered is a number...')
    if gussing_num!=my_num:
        print("But,Sorry you lose the game!!")

    print("do you still want to play ?")
    answer=input("yes or no ?")
if answer=='no':
    print('thsnks for playing..')