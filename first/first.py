import cv2 as cv
#print(cv.__version__)

def loading_display_saving():
    img = cv.imread('11.jpg', cv.IMREAD_GRAYSCALE)
    print('height:'+str(img.shape[0]))
    print('width:'+str(img.shape[1]))
    #cv.imshow('11', img)
    #cv.waitKey(0)
    #cv.imwrite('graySerj.jpg', img)

loading_display_saving()



