
import cv2



def preprocessing(img):
    img_ = cv2.imread(img)  # to make the image be binary color (black&white)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    img_ = cv2.resize(img_, (900, 950))
    img_result = cv2.adaptiveThreshold(img_, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # use adaptive_Threshold library
                                            cv2.THRESH_BINARY, 17, 5)

    return img_result
