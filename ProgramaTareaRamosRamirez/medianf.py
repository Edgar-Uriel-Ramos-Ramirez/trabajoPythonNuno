
import cv2
import numpy as np


class Filter_Median3x3():
    def __init__(self, image):
        self.image = image
        self.height, self.width = image.shape
        self.copy = image.copy()
        self.K = 4
        self.Presult = 0
        
    def median_filter(self):    

        P = np.array([0] * (2*self.K+1))
        print(P)
        for v in range(1, self.height-2):
            for u in range(1, self.width-2):
                k = 0
                #Fill the pixel Vector P for filler position (u,v)
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        P[k] = self.copy[v+i] [u+j]
                        k += 1
                #Sort the pixel vector P
                P.sort()
                #Calculate the median value of the pixel vector P
                self.Presult = P[self.K]
                #Assign the median value to the pixel (u,v)
                self.image[v,u] = self.Presult
        return self.image
                
        

    


def main():
    image = cv2.imread("my_new_picture.jpg", 0)
    image = cv2.resize(image, None, fx= 0.4, fy = 0.4, interpolation = cv2.INTER_CUBIC)

    cv2.imshow("Original", image)
    filter = Filter_Median3x3(image)
    image_filter = filter.median_filter()   
    cv2.imshow("Filtered", image_filter)

    cv2.waitKey()
    pass 

if __name__ == "__main__":
    main()
