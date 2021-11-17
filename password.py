import random
l1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # small case characters
l2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Capital case characters
l3 = ['1','2','3','4','5','6','7','8','9','0'] # Numbers
l4 = ['&','$','@'] # special Characters
l5 = [] # password
passwordlist =[]

def main():
    # print(len(l1))
    i = 0
    while(i<8):
        randnum1 = random.randint(0,len(l1)-1)
        l5.append(l1[randnum1])
        i+=1
        randnum2 = random.randint(0,len(l2)-1)
        l5.append(l2[randnum2])
        i+=1
        randnum3 = random.randint(0,len(l3)-1)
        l5.append(l3[randnum3])
        i+=1
        randnum4 = random.randint(0,len(l4)-1)
        l5.append(l4[randnum4])
        i+=1

    # randomizing placing of characters
    listindex=0
    while(listindex<8):
        indexnum = random.randint(0,len(l5)-1)
        passwordlist.insert(listindex,l5[indexnum])
        listindex +=1
        l5.pop(indexnum)
    # print(passwordlist)

    password = ''.join(passwordlist)
    print(f'Your password is : {password}')
    # Clearing the list
    for i in range(0,len(passwordlist)):    
        passwordlist.pop(0)
        # print(l5)

# Save generated password
    with open('Generated Password.txt','a') as f:
        f.write(f'{str(password)}\n')

Generate = 'y'
while Generate == 'y':
    Generate = input('Do you want to generate a new password (y/n): ')
    if Generate == 'y':
        main()
    elif Generate == 'n':
        exit()
    else:
        print('Invalid input')
        print('please enter a valid input')
        Generate = input('Do you want to generate a new password (y/n): ') # stop the program from exiting due to invalid input
