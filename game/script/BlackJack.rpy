init: 
    $ CardsList = [
        "2 Swords", "2 Clubs", "2 Diamonds", "2 Hearts",
        "3 Swords", "3 Clubs", "3 Diamonds", "3 Hearts",
        "4 Swords", "4 Clubs", "4 Diamonds", "4 Hearts",
        "5 Swords", "5 Clubs", "5 Diamonds", "5 Hearts",
        "6 Swords", "6 Clubs", "6 Diamonds", "6 Hearts",
        "7 Swords", "7 Clubs", "7 Diamonds", "7 Hearts",
        "8 Swords", "8 Clubs", "8 Diamonds", "8 Hearts",
        "9 Swords", "9 Clubs", "9 Diamonds", "9 Hearts",
        "10 Swords", "10 Clubs", "10 Diamonds", "10 Hearts",
        "J Swords", "J Clubs", "J Diamonds", "J Hearts",
        "Q Swords", "Q Clubs", "Q Diamonds", "Q Hearts",
        "K Swords", "K Clubs", "K Diamonds", "K Hearts",
        "A Swords", "A Clubs", "A Diamonds", "A Hearts",
    ]

    $ CardsDealt = []

    $ PlayerHand = []
    $ PlayerValue = 0
    $ PlayerHandStr = ""

    $ DealerHand = []
    $ DealerValue = 0
    $ DealerHandStr = ""

    $ Rnd_Card = -1

label Start_BlackJack:
    screen black

    $ CardsDealt = []

    $ PlayerHand = []
    $ PlayerValue = 0
    $ PlayerHandStr = ""

    $ DealerHand = []
    $ DealerValue = 0
    $ DealerHandStr = ""
    $ Rnd_Card = -1

    ## Dealer Gets 2 Cards Player Gets 2 Cards
    ## I interlaced to break RNG
    call GetCard
    $ DealerHand.append(CardsList[Rnd_Card])

    call GetCard
    $ PlayerHand.append(CardsList[Rnd_Card])

    call GetCard
    $ DealerHand.append(CardsList[Rnd_Card])
    
    call GetCard
    $ PlayerHand.append(CardsList[Rnd_Card])

    call CalcDealerHand
    call CalcPlayerHand

    call MenuPlayer

label MenuPlayer:

    while True:
        menu:
            "Your cards\n[PlayerHandStr]\nValue: [PlayerValue]"
            "Buy":
                call PlayerBuyCard
            "Stop":
                call DealerAI

label DealerAI:
    "Dealer Cards\n[DealerHandStr]\nValue: [DealerValue]"

    while DealerValue <= 16:
        call DealerBuyCard

    jump FinishGame

label DealerBuyCard:
    call GetCard
    $ DealerHand.append(CardsList[Rnd_Card])
    call CalcDealerHand

    "Dealer cards\n[DealerHandStr]\nValue: [DealerValue]"

    if DealerValue == 21:
        "Dealer BlackJack"
        jump MatchLost
        
    if DealerValue > 21:
        "Dealer Busted"
        jump MatchWon

    return
label PlayerBuyCard:
    call GetCard
    $ PlayerHand.append(CardsList[Rnd_Card])
    call CalcPlayerHand

    "Your cards\n[PlayerHandStr]\nValue: [PlayerValue]"

    if PlayerValue == 21:
        "Player BlackJack"
        jump MatchWon
    
    if PlayerValue > 21:
        "You Busted"
        jump MatchLost

    return

label CalcDealerHand:
    $ DealerHandStr = ""
    $ DealerValue = 0
    $ AceCount = 0
    $ i = 0

    while i < len(DealerHand):
        $ Card = DealerHand[i]
        $ DealerHandStr += Card + ", "
        $ i += 1

        if "2 " in Card:
            $ DealerValue += 2
        elif "3 " in Card:
            $ DealerValue += 3
        elif "4 " in Card:
            $ DealerValue += 4
        elif "5 " in Card:
            $ DealerValue += 5
        elif "6 " in Card:
            $ DealerValue += 6
        elif "7 " in Card:
            $ DealerValue += 7
        elif "8 " in Card:
            $ DealerValue += 8
        elif "9 " in Card:
            $ DealerValue += 9
        elif "10 " in Card or "J " in Card or "Q " in Card or "K " in Card:
            $ DealerValue += 10
        elif "A " in Card:
            $ DealerValue += 11
            $ AceCount += 1

    while DealerValue > 21 and AceCount > 0:
        $ DealerValue -= 10
        $ AceCount -= 1

    return

label CalcPlayerHand:
    $ PlayerHandStr = ""
    $ PlayerValue = 0
    $ AceCount = 0
    $ i = 0

    while i < len(PlayerHand):
        $ Card = PlayerHand[i]
        $ PlayerHandStr += Card + ", "
        $ i += 1

        if "2 " in Card:
            $ PlayerValue += 2
        elif "3 " in Card:
            $ PlayerValue += 3
        elif "4 " in Card:
            $ PlayerValue += 4
        elif "5 " in Card:
            $ PlayerValue += 5
        elif "6 " in Card:
            $ PlayerValue += 6
        elif "7 " in Card:
            $ PlayerValue += 7
        elif "8 " in Card:
            $ PlayerValue += 8
        elif "9 " in Card:
            $ PlayerValue += 9
        elif "10 " in Card or "J " in Card or "Q " in Card or "K " in Card:
            $ PlayerValue += 10
        elif "A " in Card:
            $ PlayerValue += 11
            $ AceCount += 1

    while PlayerValue > 21 and AceCount > 0:
        $ PlayerValue -= 10
        $ AceCount -= 1

    return

label GetCard:
    $ Rnd_Card = renpy.random.randint(0, len(CardsList) - 1)

    while Rnd_Card in CardsDealt:
        $ Rnd_Card = renpy.random.randint(0, len(CardsList) - 1)

    $ CardsDealt.append(Rnd_Card)

    return
    
label FinishGame:
    "Player: [PlayerValue]\nDealer: [DealerValue]"

    if DealerValue > PlayerValue:
        call MatchLost
    elif PlayerValue > DealerValue:
        call MatchWon
    else:
        call MatchDraw
    
label MatchDraw:
    "The match was a Draw"
    jump MenuEndGame

label MatchWon:
    "Congratulations You Won!"
    jump MenuEndGame

label MatchLost:
    "You lost, ggs"
    jump MenuEndGame

label MenuEndGame:
    menu:
        "Want to Play, again?"
        "Yes":
            call Start_BlackJack
        "No":
            $ MainMenu(confirm=False)()