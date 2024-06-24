print('starting in 3 seconds and loading data ...')
import time as t  ##import module
t.sleep(3)  #sleep(STOP)

name = input('Enter Name' + '\n') ##take input
age  = input("Enter Age" + '\n')  ##take age input
date = input('Enter Date Of Next Apointment' + '\n')
time = input('Enter time For Next AppointMent On Date of ' + date + '\n')


print('Updating List Please Wait...')

t.sleep(5)

f = open("data_list2.txt" , 'a')##File Name

f.write( "name is " + name +' '+ " and age is " + age + ' and date of appointment is ' + date + '  ' + ' on time of ' + time +  '\n') ##Update List

f.close()                      ## CLOSE LIST

f = open("data_list2.txt", "r") #open list for faster load time

inp = input('Do You Want To See List??') ##OPTION

if inp == 'yes':  #StateMent True Or False
    print(f.read()) ##if true
else:
    print('ok')## if false.
quit

f = open ("data_list.txt2" , 'r')
if (f.read()) == 'khushal':
    print("Found")
    t.sleep(2)
   
else:
    print("not found")
## ----------------------------------------------END---------------------------------------------##









