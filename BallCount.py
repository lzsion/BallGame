from Const import *
def guessY(ball):
    ballX = ball.getPosi()[0]
    ballY = ball.getPosi()[1]
    ballR = circleRadius
    veloX = ball.getSpeed()[0]
    veloY = ball.getSpeed()[1]
    if veloX > 0 and veloY > 0:
        tick = (screenX - boardX - ballX - ballR) / veloX
        detaY = veloY * tick - (screenY - ballR - ballY)
        if detaY <= 0:
            guessY = ballY + veloY * tick
        elif (detaY // (screenY - 2 * ballR)) % 2 == 0:
            guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
        elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
            guessY = ballR + detaY % (screenY - 2 * ballR)
        return [1,guessY,tick]
    elif veloX > 0 and veloY < 0:
        tick = (screenX - boardX - ballX - ballR) / veloX
        detaY = (-veloY) * tick - (ballY - ballR)
        if detaY < 0:
            guessY = ballY - (-veloY) * tick
        elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
            guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
        elif (detaY // screenY) % 2 == 0:
            guessY = ballR + detaY % (screenY - 2 * ballR)
        return [1,guessY,tick]
    elif veloX < 0 and veloY > 0:
        tick = (ballX - boardX - ballR) / (-veloX)
        detaY = veloY * tick - (screenY - ballR - ballY)
        if detaY <= 0:
            guessY = ballY + veloY * tick
        elif (detaY // (screenY - 2 * ballR)) % 2 == 0:
            guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
        elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
            guessY = ballR + detaY % (screenY - 2 * ballR)
        return [0,guessY,tick]
    elif veloX < 0 and veloY < 0:
        tick = (ballX - boardX - ballR) / (-veloX)
        detaY = (-veloY) * tick - (ballY - ballR)
        if detaY < 0:
            guessY = ballY - (-veloY) * tick
        elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
            guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
        elif (detaY // screenY) % 2 == 0:
            guessY = ballR + detaY % (screenY - 2 * ballR)
        return [0,guessY,tick]


