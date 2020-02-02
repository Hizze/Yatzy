import pygame, sys, os, random

assetsPath = os.path.dirname("C:/Users/knapp/Desktop/PythonProjects/Yatzy/Assets/")
size = width, height = 1200,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Yatzy")

background = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/background.png"))
rollBtn = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/roll.png"))
lockBtn = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/locked.png"))
notLockBtn = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/notlocked.png"))
nextBtn = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/next.png"))
scoreTable = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/scoreTable.png"))

rollDiceAnimation, gameState = 1, 1
amountOfRolls, firstPair, secondPair = 0, 0, 0
throwList, newThrowList = [], []
newThrow = False
calculated = False
lockClick1, lockClick2, lockClick3, lockClick4, lockClick5 = False, False, False, False, False
ones, twos, threes, fours, fives, sixes = 0,0,0,0,0,0
pair, twoPairs, threeOfAKind, fourOfAKind, smallStraight, largeStraight, fullHouse, chance, yatzy = 0,0,0,0,0,0,0,0,0
onesInList, twosInList, threesInList, foursInList, fivesInList, sixesInList = 0,0,0,0,0,0

def animateDice():
    global rollDiceAnimation
    rollDiceAnimation += 1
    pygame.display.update()
    drawScreen()
    
def drawScreen():
    global newThrow
    global throwList
    global newThrowList
    global throw1, throw2, throw3, throw4, throw5
    global lockClick1, lockClick2, lockClick3, lockClick4, lockClick5
    global die1, die2, die3, die4, die5
    global calculated
    global rollDiceAnimation

    screen.blit(background,(0,0))
    screen.blit(rollBtn,(200,350))
    screen.blit(nextBtn,(450,350))
    screen.blit(scoreTable,(800,50))
    
    if newThrow == True and rollDiceAnimation <= 10:
        diceFrame = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/diceFrame%d.png" % rollDiceAnimation))
        screen.blit(diceFrame,(0,50))
        pygame.time.delay(100)
        animateDice()
    else:
        rollDiceAnimation = 1
    if amountOfRolls == 1 or 2 or 3:
        if newThrow == True:
            if lockClick1 == False:
                throw1 = random.randint(1,6)
            if lockClick2 == False:
                throw2 = random.randint(1,6)
            if lockClick3 == False:
                throw3 = random.randint(1,6)
            if lockClick4 == False:
                throw4 = random.randint(1,6)
            if lockClick5 == False:
                throw5 = random.randint(1,6)
            throwList = [throw1,throw2,throw3,throw4,throw5]
            newThrow = False
        else:
            for throw in throwList:
                die1 = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/die%d.png" % throw1))
                screen.blit(die1,(50,50))
                die2 = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/die%d.png" % throw2))
                screen.blit(die2,(200,50))
                die3 = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/die%d.png" % throw3))
                screen.blit(die3,(350,50))
                die4 = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/die%d.png" % throw4))
                screen.blit(die4,(500,50))
                die5 = pygame.image.load(os.path.join(os.path.dirname(assetsPath), "Assets/die%d.png" % throw5))
                screen.blit(die5,(650,50))
                pairText = myFont.render("Pair: " + str(pair), False, (0, 0, 0))
                twoPairsText = myFont.render("Two pairs: " + str(twoPairs), False, (0, 0, 0))
                threeOfAKindText = myFont.render("Three of a kind: " + str(threeOfAKind), False, (0, 0, 0))
                fourOfAKindText = myFont.render("Four of a kind: " + str(fourOfAKind), False, (0, 0, 0))
                smallStraightText = myFont.render("Small straight: " + str(smallStraight), False, (0, 0, 0))
                largeStraightText = myFont.render("Large straight: " + str(largeStraight), False, (0, 0, 0))
                fullHouseText = myFont.render("Full house: " + str(fullHouse), False, (0, 0, 0))
                chanceText = myFont.render("Chance: " + str(chance), False, (0, 0, 0))
                yatzyText = myFont.render("Yatzy: " + str(yatzy), False, (0, 0, 0))
                rollsLeftText = myFont.render("Throws left: " + str(3 - amountOfRolls), False, (0, 0, 0))
                
                screen.blit(pairText,(0,20))
                screen.blit(twoPairsText,(0,40))
                screen.blit(threeOfAKindText,(0,60))
                screen.blit(fourOfAKindText,(0,80))
                screen.blit(smallStraightText,(0,100))
                screen.blit(largeStraightText,(0,120))
                screen.blit(fullHouseText,(0,140))
                screen.blit(chanceText,(0,160))
                screen.blit(yatzyText,(0,180))
                screen.blit(rollsLeftText,(0,250))
                calculated = False
                if calculated == False and throwList != newThrowList:
                    newThrowList = throwList
                    calculated = True
                    calculateThrow()

    if lockClick1 == True:
        screen.blit(lockBtn,(50,200))
    elif lockClick1 == False and amountOfRolls > 0:
        screen.blit(notLockBtn,(50,200))
    if lockClick2 == True:
        screen.blit(lockBtn,(200,200))
    elif lockClick2 == False and amountOfRolls > 0:
        screen.blit(notLockBtn,(200,200))
    if lockClick3 == True:
        screen.blit(lockBtn,(350,200))
    elif lockClick3 == False and amountOfRolls > 0:
        screen.blit(notLockBtn,(350,200))
    if lockClick4 == True:
        screen.blit(lockBtn,(500,200))
    elif lockClick4 == False and amountOfRolls > 0:
        screen.blit(notLockBtn,(500,200))
    if lockClick5 == True:
        screen.blit(lockBtn,(650,200))
    elif lockClick5 == False and amountOfRolls > 0:
        screen.blit(notLockBtn,(650,200))

        
    pygame.display.update()  
    
def calculateThrow():
    global ones, twos, threes, fours, fives, sixes
    global pair, twoPairs, threeOfAKind, fourOfAKind, smallStraight, largeStraight, fullHouse, chance, yatzy
    global onesInList, twosInList, threesInList, foursInList, fivesInList, sixesInList
    firstPair, secondPair = 0,0
    pair, twoPairs, threeOfAKind, fourOfAKind, smallStraight, largeStraight, fullHouse, chance, yatzy = 0,0,0,0,0,0,0,0,0
    onesInList, twosInList, threesInList, foursInList, fivesInList, sixesInList = 0,0,0,0,0,0
    onesInList = newThrowList.count(1)
    twosInList = newThrowList.count(2)
    threesInList = newThrowList.count(3)
    foursInList = newThrowList.count(4)
    fivesInList = newThrowList.count(5)
    sixesInList = newThrowList.count(6)
    
    #Pair
    if sixesInList >= 2:
        pair = 12
    elif fivesInList >= 2:
        pair = 10
    elif foursInList >= 2:
        pair = 8
    elif threesInList >= 2:
        pair = 6
    elif twosInList >= 2:
        pair = 4
    elif onesInList >= 2:
        pair = 2
        
    #Two pairs
    if firstPair == 0:
        if sixesInList >= 2:
            firstPair = 12
        elif fivesInList >= 2:
            firstPair = 10
        elif foursInList >= 2:
            firstPair = 8
        elif threesInList >= 2:
            firstPair = 6
        elif twosInList >= 2:
            firstPair = 4
        elif onesInList >= 2:
            firstPair = 2
    if secondPair == 0:
        if sixesInList >= 2 and firstPair != 12:
            secondPair = 12
        elif fivesInList >= 2 and firstPair != 10:
            secondPair = 10
        elif foursInList >= 2 and firstPair != 8:
            secondPair = 8
        elif threesInList >= 2 and firstPair != 6:
            secondPair = 6
        elif twosInList >= 2 and firstPair != 4:
            secondPair = 4
        elif onesInList >= 2 and firstPair != 2:
            secondPair = 2
    twoPairs = firstPair + secondPair
    
    #Three of a kind
    if sixesInList >= 3:
        threeOfAKind = 18
    elif fivesInList >= 3:
        threeOfAKind = 15
    elif foursInList >= 3:
        threeOfAKind = 12
    elif threesInList >= 3:
        threeOfAKind = 9
    elif twosInList >= 3:
        threeOfAKind = 6
    elif onesInList >= 3:
        threeOfAKind = 3
        
    #Four of a kind
    if sixesInList >= 4:
        fourOfAKind = 24 
    elif fivesInList >= 4:
        fourOfAKind = 20
    elif foursInList >= 4:
        fourOfAKind = 16 
    elif threesInList >= 4:
        fourOfAKind = 12
    elif twosInList >= 4:
        fourOfAKind = 8
    elif onesInList >= 4:
        fourOfAKind = 4

    #Small straight
    if onesInList == 1 and twosInList == 1 and threesInList == 1 and foursInList == 1 and fivesInList == 1 and sixesInList == 0:
        smallStraight = 15

    #Large straight
    if onesInList == 0 and twosInList == 1 and threesInList == 1 and foursInList == 1 and fivesInList == 1 and sixesInList == 1:
        largeStraight = 20
        
    #Full house
    if onesInList == 3 or twosInList == 3 or threesInList == 3 or foursInList == 3 or fivesInList == 3 or sixesInList == 3:
        if onesInList == 2 or twosInList == 2 or threesInList == 2 or foursInList == 2 or fivesInList == 2 or sixesInList == 2:
            for eyes in newThrowList:
                fullHouse += eyes

    #Chance
    for eyes in newThrowList:
        chance += eyes
    
    #Yatzy
    if onesInList == 5 or twosInList == 5 or threesInList == 5 or foursInList == 5 or fivesInList == 5 or sixesInList == 5:
        yatzy = 50
        
    if pair > 0: print("Pair:", pair)
    if firstPair > 0 and secondPair > 0: print("Two pairs:", (firstPair + secondPair))
    if threeOfAKind > 0: print("Four of a kind:", threeOfAKind)
    if fourOfAKind > 0: print("Four of a kind:", fourOfAKind)
    if smallStraight > 0: print("Small straight:", smallStraight)
    if largeStraight > 0: print("Large straight:", largeStraight)
    if fullHouse > 0: print("Full house:", fullHouse)
    if chance > 0: print("Chance:", chance)
    if yatzy > 0: print("Yatzy:", yatzy)
    
while gameState == 1:
    pygame.font.init()
    myFont = pygame.font.SysFont("arial", 15)
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameState = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if throwList:
                if die1.get_rect(topleft=(50,50)).collidepoint(pos):
                    if lockClick1 == False:
                        lockClick1 = True
                    elif lockClick1 == True:
                        lockClick1 = False
                if die2.get_rect(topleft=(200,50)).collidepoint(pos):
                    if lockClick2 == False:
                        lockClick2 = True
                    elif lockClick2 == True:
                        lockClick2 = False
                if die3.get_rect(topleft=(350,50)).collidepoint(pos):
                    if lockClick3 == False:
                        lockClick3 = True
                    elif lockClick3 == True:
                        lockClick3 = False
                if die4.get_rect(topleft=(500,50)).collidepoint(pos):
                    if lockClick4 == False:
                        lockClick4 = True
                    elif lockClick4 == True:
                        lockClick4 = False
                if die5.get_rect(topleft=(650,50)).collidepoint(pos):
                    if lockClick5 == False:
                        lockClick5 = True
                    elif lockClick5 == True:
                        lockClick5 = False
            if throwList:
                if nextBtn.get_rect(topleft=(450,350)).collidepoint(pos):
                    amountOfRolls = 0
                    lockClick1, lockClick2, lockClick3, lockClick4, lockClick5 = False, False, False, False, False
                    newThrow = False
                    throwList = []
            if rollBtn.get_rect(topleft=(200,350)).collidepoint(pos):
                if amountOfRolls == 0:
                    newThrow = True
                    amountOfRolls = 1
                elif amountOfRolls == 1:
                    newThrow = True
                    amountOfRolls = 2
                elif amountOfRolls == 2:
                    newThrow = True
                    amountOfRolls = 3
    if gameState == 1:                
        drawScreen()
