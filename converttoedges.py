import cv2
for i in range(0, 5301):
    img = cv2.imread('./frames/frame'+str(i)+'.png')
    edges = cv2.Canny(img, 75, 100)
    cv2.imwrite("./processedframes/frame%d.png" % i, edges)
