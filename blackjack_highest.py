def BlackjackHighest(strArr):
    total = 0
    
    cards = ["one","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]
    for i in range(0, 10):
        total += strArr.count(cards[i])*(i+1)
    for i in range(10, len(cards)):
        total += strArr.count(cards[i])*10
        
    has_ace = strArr.count("ace")>0
    ace_value = 0
    if(has_ace):
        if(total == 20):
            ace_value = 1
        elif(total+11 > 21):
            ace_value = 1
        else:
            ace_value = 11
        total += ace_value

    if(ace_value == 1):
        highest_card = "ace"
    for i in range(0, len(cards)):
        if(strArr.count(cards[i])):
            highest_card = cards[i]
    if(ace_value == 11):
        highest_card = "ace"

    if(total<21):
        state = "below"
    elif(total>21):
        state = "above"
    else:
        state = "blackjack"

    result = "%s %s"%(state, highest_card)

    if(0):
        print("ace_value = %d"%(ace_value))
        print("has_ace = %d"%(has_ace))
        print("total = %d"%(total))
        print("highest_card = %s"%(highest_card))
    return result

print BlackjackHighest(raw_input())
#print(BlackjackHighest(("queen","ace","ten")))
