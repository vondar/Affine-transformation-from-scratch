# Affine Transformation
## Logic 
1. We get coordinates of each pixels of the image.
2. We multiply them with respective matrix,as required![](https://i.imgur.com/Tznn91A.png)
3. Then, we observe respective transformation
![](https://i.imgur.com/EQ9NQTL.png)
## Step By Step program run through
1. The program will what ask type of transformation, do you want, give the required response
2. If you choose rotation then,it will ask the angle the to rotate ,if you choose translation, it will ask the distances in x and y direction,if you choose custom then, you will fill all 6 required matrix elements.
3. The result will be shown
## Math
1. The matrices are multiplied like this
![](https://i.imgur.com/ePYvi0E.png)
## Notes
* There can be non - integral coordinates after the multiplication,so either we can convert them to ,integers or your interpolation techniques.
* Using interpolation , should be preferred , but, since, I had no knowledge of interpolation , therefore , I simply converted them to integers.
