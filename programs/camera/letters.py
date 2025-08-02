import cv2

def threshold_image_opencv(input_img, threshold):
    _, thresholded = cv2.threshold(input_img, threshold, 255, cv2.THRESH_BINARY)
    return thresholded

frame = cv2.imread('english_alphabet_4(1).png')

gray_alfabet = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# gray_alfabet = cv2.medianBlur(gray_alfabet, 21)
gray_alfabet = threshold_image_opencv(gray_alfabet, 50)
contours_img1, _ = cv2.findContours(gray_alfabet, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(frame, contours_img1, -1, (255, 255, 0), 3)
cv2.imshow('gray_alfabet', gray_alfabet)
cv2.imshow("qwe", frame)

template = cv2.imread('/home/evgeniy/Downloads/S20.jpg')

gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray, 7)
gray = threshold_image_opencv(gray, 50)
cv2.imshow('gray', gray)
contours_img2, _ = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(template, contours_img2, 0, (0, 150, 0), 3)
print(template.shape)
lisd = []
print(len(contours_img2))
# for i, contour1 in enumerate(contours_img1):
#     for j, contour2 in enumerate(contours_img2):
#         lisd.append(cv2.matchShapes(contour1, contour2, cv2.CONTOURS_MATCH_I1, 0.0))
for i in contours_img1:
    lisd.append(cv2.matchShapes(i, contours_img2[0], cv2.CONTOURS_MATCH_I1, 0.0))

for i in contours_img1:
    if cv2.matchShapes(i, contours_img2[0], cv2.CONTOURS_MATCH_I1, 0.0) == min(lisd):
        print(cv2.matchShapes(i, contours_img2[0], cv2.CONTOURS_MATCH_I1, 0.0))
        cv2.drawContours(frame, i, -1, (0, 150, 0), 3)

print(lisd)
print(min(lisd))
print(max(lisd))


cv2.imshow('template', template)
cv2.imshow('frame' , frame)
cv2.waitKey(0)
# cap.release()
cv2.destroyAllWindows()
