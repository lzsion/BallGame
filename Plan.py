from Const import *
def computerEvent(allBallLi,sideBoard):
    sideBallLi = []
    sideBoardTop = sideBoard.getPosi()[1]
    sideBoardBottom = sideBoardTop + boardY
    # minTick = screenY // boardVelo + 100
    # haveball = False
    for eachBall in allBallLi:
        guessedY = eachBall.getGuessedY()
        if guessedY[0] in computerPlayer:
            if sideBoardTop - guessedY[2] * boardVelo > guessedY[1]: 
                continue
            if sideBoardBottom + guessedY[2] * boardVelo < guessedY[1]:
                continue
            sideBallLi.append(eachBall)
            # if guessedY[2] < minTick:
            #     minTick = guessedY[2]
            #     minBall = eachBall
            #     haveBall = True
    # if len(sideBallLi) > 0:
    #     minGuessY = min(sideBallLi,key = lambda x : x[2])
    #     for eachGuess in sideBallLi:
