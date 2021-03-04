import cv2

import os



dict=dict()
def call():

    for i in os.listdir(r'D:\among us\rahat\app\pythonfiles\ImagesQuery'):
        if i.endswith('.png') or i.endswith('.jpg'):
            pointer='ImagesQuery/'+i
            img1 = cv2.imread(pointer, 0)

            img = cv2.imread(r'D:\among us\rahat\app\pythonfiles\ImagesTrain\camera.jpeg', 0)


            orb = cv2.ORB_create(nfeatures=5000)
            kp1, des1 = orb.detectAndCompute(img1, None)
            kp2, des2 = orb.detectAndCompute(img, None)

            bf = cv2.BFMatcher()

            matches = bf.knnMatch(des1, des2, k=2)

            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])

            dict[len(good)]=pointer

    l1=sorted(dict.keys())
    #print(dict)

    #img1=cv2.imread(dict[l1[-1]], 0)

    #matches=[l1[-1],l1[-2]]
    return (dict[l1[-1]].split('/')[-1][:-4].upper())
    #print(matches)
print(call())