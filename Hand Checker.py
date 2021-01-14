#This program will ask you to compile a five card hand.
#It will then tell you what that hand is in poker.

def handchecker(hand):    

    suits = hand[0][1]+hand[1][1]+hand[2][1]+hand[3][1]+hand[4][1] #check suits of cards
    
    value = hand[0][0]+hand[1][0]+hand[2][0]+hand[3][0]+hand[4][0] #check values
    
    intvalue=[]
    full=0
    of=0
    pair=0
    highcard=0
    highcard1=0
    highcard2=0
    highcard3=0
    highcard4=0
    highpair=0
    highlist=[]
    lowpair=0
    trips=0
    handvalue=0 #not used in this program - can be used to expand to compare two hands and find winner


    for p in value:  #assigning values to face cards and ten
        if p=='J':
            intvalue=intvalue+[11]
            continue
        if p=='T':
            intvalue=intvalue+[10]
            continue
        if p =='Q':
            intvalue=intvalue+[12]
            continue
        if p=='K':
            intvalue=intvalue+[13]
            continue
        if p=='A':
            intvalue=intvalue+[14]
            continue
        else:
            intvalue=intvalue+[int(p)]
            
    intvalue.sort() #put the numbers in order to easier read  

    #Royal Flush

    if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] and ''.join(sorted(value))=='AJKQT':
        
        handvalue=10
        rf=[10]   

        return'Holy Cow! You got a royal flush!'

        
        
    #Straight Flush

    if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] and intvalue[0]+1==intvalue[1] and intvalue[1]+1==intvalue[2] and intvalue[2]+1==intvalue[3] and intvalue[3]+1==intvalue[4]:
        
        handvalue=9        
        highcard=intvalue[4]

        sf=[handvalue,highcard]

        return 'You got a straight flush!'

    if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] and intvalue[0]==2 and intvalue[1]==3 and intvalue[2]==4 and intvalue[3]==5 and intvalue[4]==14:
        #print('Straight Flush. Very nice.')
        handvalue=9
        highcard=5

        sf=[handvalue,highcard]

        return 'You got a straight flush!'

    #Four of a Kind

    for a in range(1,15):

        if intvalue.count(a)==4:
            
            for a in range(1,15):

                if intvalue.count(a)==1:

                    highcard=a
                    handvalue=8

                    fk=[handvalue,highcard]

                    return 'Four of a kind! Sick!'

    #Full House
                
    for a in range(1,15):

        if intvalue.count(a)==3:

            for b in range(1,15):

                if a==b:
                    continue

                elif intvalue.count(b)==2:                    

                    full=a
                    of=b
                    handvalue=7
                    
                    fh=[handvalue,full,of]
                    
                    return 'Full House! Holy moly!'

    #Flush
                    
    if suits[0]==suits[1]==suits[2]==suits[3]==suits[4]:        
        
        highcard=intvalue[4]
        handvalue=6
        
        flush=[handvalue,highcard]
        
        return 'Flush is a great hand!'

    #Straight

    if intvalue[0]+1==intvalue[1] and intvalue[1]+1==intvalue[2] and intvalue[2]+1==intvalue[3] and intvalue[3]+1==intvalue[4]:
       
        highcard=intvalue[4]
        handvalue=5

        straight=[handvalue,highcard]
        
        return 'Nice straight!'

    if intvalue[0]==2 and intvalue[1]==3 and intvalue[2]==4 and intvalue[3]==5 and intvalue[4]==14:
        
        highcard=5
        handvalue=5

        straight=[handvalue,highcard]
        
        return 'Woah... the low straight.'

    #Three of a Kind

    for a in range(1,15):

        if intvalue.count(a)==3:            

            for p in range(1,15):

                if p==a:
                    continue

                else:
                    if p in intvalue and p>highcard:
                        highcard=p
                        trips=a

            
            handvalue=4

            three=[handvalue,trips]

            return 'You have three-of-a-kind. Solid.'

    #Two Pair

    for a in range(1,15):

        if intvalue.count(a)==2:

            for b in range(1,15):

                if b==a:
                    continue

                if intvalue.count(b)==2:                    

                    lowpair=a
                    highpair=b

                    for g in intvalue:

                        if g==a or g==b:
                            continue
                        else:
                            highcard=g                            
                            handvalue=3

                            two=[handvalue,highpair,lowpair,highcard]
                            
                            return 'Two pairs!'

    #One Pair

    for a in range(1,15):

        if intvalue.count(a)==2:

            #print('One pair. Better than nothing.')

            for f in intvalue:

                if f==a:
                    continue

                else:
                    highlist=highlist+[f]

            highcard=highlist[2]
            highcard1=highlist[1]
            highcard2=highlist[0]
            pair=a
            handvalue=2            

            one=[handvalue,pair,highcard,highcard1,highcard2]
            
            return 'One pair is better than nothing.'

    #Highcard

    highcard=intvalue[4]
    highcard1=intvalue[3]
    highcard2=intvalue[2]
    highcard3=intvalue[1]
    highcard4=intvalue[0]
    handvalue=1    

    hc=[handvalue,highcard,highcard1,highcard2,highcard3,highcard4]

    if highcard<10:
    
        return 'Bad luck! You have ' + str(highcard) + ' high.'

    if highcard==10:

        return 'Bad luck! You have 10 high.'

    if highcard==11:

        return 'Bad luck! You have Jack high.'

    if highcard==12:

        return 'Bad luck! You have Queen high.'

    if highcard==13:

        return 'Bad luck! King high.'

    if highcard==14:

        return 'You only have Ace high.'

#Following region is used to score hands. Not necessary for this program
##play1wins=0
##play2wins=0
##                    
##for p in range(0,1000):
##
##    p1=handchecker(play1[p])
##
##    p2=handchecker(play2[p])
##
##    if p1[0]>p2[0]:
##
##        play1wins+=1
##
##    if p2[0]>p1[0]:
##
##        play2wins+=1
##
##
##
##    if p1[0]==p2[0]: #ties - need to find high cards
##
##        if p1[0]==9: #straight flush
##
##            if p1[1]>p2[1]:
##
##                play1wins+=1
##
##            else:
##
##                play2wins+=1
##
##        if p1[0]==8: #four of a kind
##
##            if p1[1]>p2[1]: #highcard
##
##                play1wins+=1
##
##            else:
##                play2wins+=1
##
##
##        if p1[0]==7: #fullhouse
##
##            if p1[1]>p2[1]:
##
##                play1wins+=1
##
##            else:
##                play2wins+=1
##
##        if p1[0]==6: #flush
##
##            if p1[1]>p2[1]:
##                play1wins+=1
##
##            else:
##                play2wins+=1
##
##        if p1[0]==5: #straight
##
##            if p1[1]>p2[1]:
##
##                play1wins+=1
##
##            else:
##                play2wins+=1
##
##        if p1[0]==4: #3ofakind
##
##            if p1[1]>p2[1]:
##                play1wins+=1
##
##            else:
##                play2wins+=1
##
##        if p1[0]==3: # Two Pair
##
##            if p1[1]>p2[1]:
##
##                play1wins+=1
##
##            if p2[1]>p1[1]:
##
##                play2wins+=1
##
##            if p1[1]==p2[1]: #Same high pair
##
##                if p1[2]>p2[2]:
##
##                    play1wins+=1
##
##                if p2[2]>p1[2]:
##
##                    play2wins+=1
##
##                if p1[2]==p2[2]: #Both pairs same
##
##                    if p1[3]>p2[3]:
##
##                        play1wins+=1
##
##                    else:
##                        play2wins+=1
##
##        
##                    
##        if p1[0]==2: #One pair
##
##            for x in range(1,5):
##
##                if p1[x]>p2[x]:
##                    play1wins+=1
##                    break
##                if p2[x]>p1[x]:
##                    play2wins+=1
##                    break
##
##        if p1[0]==1: #high card
##
##            for x in range(1,6):
##                if p1[x]>p2[x]:
##                    play1wins+=1
##                    break
##                if p2[x]>p1[x]:
##                    play2wins+=1
##                    break

def pokergame():   #This is the function that will check the hand               

    playerhand=[]       

    cards=['2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH']                 

    print('This is a poker hand evaluator. If you enter a set of five cards,\nthe program will tell you which Poker hand you have.\n')

    print('Enter your cards in this format: 9H would be 9 of hearts, 2C would be 2 of clubs.\n')

    print('For ten,jack,queen,king, or ace: ten=T, jack=J, queen=Q, king=K, ace=A\n')

    print('So ace of spades is AS and ten of diamonds is TD. Be sure to use capital letters.\n')

    print('Enter your first card.\n')

    bob=input()

    while bob not in cards:

        print('\nThat is not a valid card. Try again.\n')

        bob=input()

    playerhand=playerhand+[bob]

    print('\nSo far your hand is: ' + bob + '\n')

    print('Enter your second card.\n')

    bob=input()

    while bob not in cards or bob in playerhand:

        print('\nThat is not a valid card. Try again.\n')

        bob=input()

    playerhand=playerhand+[bob]

    print('\nSo far your hand is: ' + playerhand[0] + ' ' + playerhand[1] + '\n')

    print('Enter your third card.\n')

    bob=input()

    while bob not in cards or bob in playerhand:

        print('\nThat is not a valid card. Try again.\n')

        bob=input()

    playerhand=playerhand+[bob]

    print('\nSo far your hand is: ' + playerhand[0] + ' ' + playerhand[1] + ' ' + playerhand[2] + '\n')

    print('Enter your fourth card.\n')

    bob=input()

    while bob not in cards or bob in playerhand:

        print('\nThat is not a valid card. Try again.\n')

        bob=input()

    playerhand=playerhand+[bob]

    print('\nSo far your hand is: ' + playerhand[0] + ' ' + playerhand[1] + ' ' + playerhand[2] + ' ' + playerhand[3] + '\n')

    print('Enter your last card.\n')

    bob=input()

    while bob not in cards or bob in playerhand:

        print('\nThat is not a valid card. Try again.\n')

        bob=input()

    playerhand=playerhand+[bob]

    print('Your hand is: ' + playerhand[0] + ' ' + playerhand[1] + ' ' + playerhand[2] + ' ' + playerhand[3] + ' ' + playerhand[4] + '\n')

    print(handchecker(playerhand))

    print('\n')

    print('Do you want to try again? Y/N')

    global jerk
    
    jerk=input()

    while jerk!='Y' and jerk!= 'N':

        print('You have to type "Y" for yes and "N" for no.')

        jerk=input()

    if jerk=='N':

        print('OK. Thanks for using my program. Love, Timbo')

        return

    if jerk=='Y':

        return

    

    
jerk='Y'

while jerk=='Y': #This lets program run until user shuts down

    pokergame()


        




    

                    
