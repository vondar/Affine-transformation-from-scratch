import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('g.jpeg',0)
print('enter r for rotation')
print('enter s for shear')
print('enter t for translation')
print('enter c for custom' )
f=np.zeros(6)
#print(img)
key=0
rows,cols= img.shape
a=input()
if(a=='r'):
    t=float(input('enter theta '))
    t=t/180
    rot=np.float32([[np.cos(t),-np.sin(t),0],[np.sin(t),np.cos(t),0],[0,0,1]])
elif(a=='s'):
    rot=np.float32([[1,0.5,0],[0,0.5,0],[0,0,1]])
elif(a=='t'):
    x=int(input('enter movement in x '))
    y=int(input('enter movement in y '))
    rot=np.float32([[1,0,0],[0,1,0],[0,0,1]])
    key = 1
elif(a=='c'):
    for i in range(6):
        f[i]=input()
    rot=np.float32([[f[0],f[1],f[2]],[f[3],f[4],f[5]],[0,0,1]])

else:
    print('please enter only r,t,s')


#pts1 = np.float32([[50,50],[200,50],[50,200]])
#pts2 = np.float32([[10,100],[200,50],[100,250]])
#M = cv2.getAffineTransform(pts1,pts2)
#print(M)
#res=cv2.warpAffine(img,M,(cols,rows))

def arr(array,x,y):
    return array[x,y]
res=np.zeros_like(img)
rest=np.zeros_like(img)
for i in range(0,rows):
 for j in range(0,cols):
     b=np.float32([i,j,1])
     a=np.matmul(b,rot)
     #print(a[0],a[1])
     if(a[0]<rows and a[1]<cols and a[0]>0 and a[1]>0):
         res[int(a[0]),int(a[1])]=arr(img,i,j)
if key == 1:
    for i in range(rows-x):
        for j in range(cols-y):
            rest[i+x,j+y]=res[i,j]


#res.astype('uint8')
#print(res)
cv2.imshow('img',img)
if key == 1:
    cv2.imshow('rest',rest)
else:
    cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
