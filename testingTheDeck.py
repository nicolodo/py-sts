
# Get deck 
# put cards in it
    # from the all possible cards list
# take a card out
# done

# using the arbritrary card number scheme
# thats 5 strikes a bash and 4 defends
deck = [1,1,1,1,1,2,3,3,3,3]
print(deck)


deck.append(4) # 4 in the arbitraryNum list isss... iron cleave
print(deck)

#making a quick test deck for the remove part
deck = [1,2,3,4,5,6,7,8,9]
print(deck)
# removing a card
# im removing the card at position 3
deckCardsBefore = deck[0:3]
deckCardsAfter = deck[3+1::]
deck = deckCardsBefore + deckCardsAfter
print(deck)

# ok I have a way of adding cards and removing them
# will have to add this to deck class


deck = [1,2,3,4,5,6,7,8,9]
# function is zero indexed
# it would be easier to read if it were 1 indexed but whatever
def removeCard(deck=list,card=int):
    print(deck)
    before = deck[0:card]
    if card < (len(deck) - 1):
        after = deck[card+1:]
    else:
        after = []
    deck = before + after
    print(deck)

print("test function")
removeCard(deck,0)
removeCard(deck,8)
removeCard(deck,3)
removeCard(deck,2)
