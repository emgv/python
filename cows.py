import random

def char_count(pstr):
    occ= {}
    for c in pstr:
        if(c not in occ):
            occ[c]= pstr.count(c)
    return occ

def cows_and_bulls(num_str, answer):
    print(occurr)
    i=0
    cows_ct=0
    bulls_ct=0
    bulls= {}
    len_ans=len(answer)
    while(i < len_ans):
        n= num_str[i]
        if(n == answer[i]):
            cows_ct+=1
            if(n in bulls): bulls_ct-=1
        elif(n not in bulls and n in occurr):
            bulls[n]= 1
            bulls_ct+= occurr[n]

        i+=1

    print('Cows: ' + str(cows_ct) + ' Bulls:' + str(bulls_ct))

random.seed()
secret= str(int(random.random() * 9999))
occurr= char_count(secret)

while(True):
    guess= input('guess?\n(type "q" to exit, "s" to see the secret): ')
    if(guess == 'q'): break
    if(guess == 's'):
        print('secret:' + secret)
        continue
    if(guess == '-2'):
        print('secret[1]:' + str(int(secret[1])+2))
        continue
    cows_and_bulls(guess, secret)

            #7848 (answer)
            #8348

            #8 => cows => 0, bulls => 2
            #3 => cows => 0, bulls => 2
            #4 => cows => 1, bulls => 2
            #8 => cows => 2, bulls => 1
