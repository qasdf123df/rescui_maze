import cv2
import numpy as np
def send_red_signal():
    pass
def send_green_signal():
    pass
def send_yellow_signal():
    pass
def treck_red(image, lower_red, upper_red):
    red_mask = cv2.inRange(image, lower_red, upper_red)
    red = cv2.bitwise_and(image, image, mask=red_mask)
    red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('red', red)
    for contur1 in contours:
        if cv2.contourArea(contur1) > 100:
            print(cv2.contourArea(contur1), 'red')
            cv2.drawContours(image, contours, -1, (255, 255, 0), 1)
            cv2.imshow('contour', image)
            send_red_signal()
            return None
    return None

def treck_green(image, lower_green, upper_green):
    green_mask = cv2.inRange(image, lower_green, upper_green)
    green = cv2.bitwise_and(image, image, mask=green_mask)
    green = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('green', green)
    for contur1 in contours:
        if cv2.contourArea(contur1) > 100:
            print(cv2.contourArea(contur1), 'green')
            cv2.drawContours(image, contours, -1, (255, 255, 0), 1)
            cv2.imshow('contour', image)
            send_green_signal()
            return None
    return None

def treck_yellow(image, lower_yellow, upper_yellow):
    yellow_mask = cv2.inRange(image, lower_yellow, upper_yellow)
    yellow = cv2.bitwise_and(image, image, mask=yellow_mask)
    yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('yellow', yellow)
    for contur1 in contours:
        if cv2.contourArea(contur1) > 100:
            print(cv2.contourArea(contur1), 'yellow')
            cv2.drawContours(image, contours, -1, (255, 255, 0), 1)
            cv2.imshow('contour', image)
            send_yellow_signal()
            return None
    return None


image = cv2.imread('red.jpg')
cv2.imshow('st', image)

lower_red = np.array([0, 0, 150])
upper_red = np.array([50, 50, 255])

lower_green = np.array([0, 150, 0])
upper_green = np.array([100, 255, 50])

lower_yellow = np.array([0, 200, 200])
upper_yellow = np.array([60, 255, 255])



treck_red(image, lower_red, upper_red)

treck_green(image, lower_green, upper_green)

treck_yellow(image, lower_yellow, upper_yellow)

cv2.waitKey(0)
