import cv2

def images_the_same(image1, image2):
    """
    :param image1: path of image1
    :param image2: path of image2
    :return: True if images are the same, False if images are not the same
    """
    im1 = cv2.imread(image1)
    im2 = cv2.imread(image2)

    if im1.shape != im2.shape:
        return False

    difference = cv2.subtract(im1, im2)
    b, g, r = cv2.split(difference)

    if(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 
        and cv2.countNonZero(r) == 0):
        return True
    return False



