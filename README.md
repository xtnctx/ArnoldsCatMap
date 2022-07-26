# ArnoldsCatMap

Consider taking a square image, consisting of N-by-N pixels, where the coordinate of each pixel is represented by the ordered pair (X, Y). 
 
Arnold’s cat map induces a discrete-time dynamical system in which the evolution is given by iterations of the mapping Γ𝑐𝑎𝑡 ∶ 𝕋2 → 𝕋2 given the formula
```
Γ𝑐𝑎𝑡(𝑥,𝑦)→(2𝑥+𝑦, 𝑥+𝑦) 𝑚𝑜𝑑 1 where Γ𝑐𝑎𝑡 ([𝑋𝑛+1 𝑌𝑛+1])=[1 11 2][𝑋𝑛 𝑌𝑛](𝑚𝑜𝑑 1) 
```

## Connection between Arnold’s cat and Fibonacci’s rule 

Let the nth number of the Fibonacci sequence be defined by the recurrence relation 𝐹𝑛 = 𝐹𝑛−1 + 𝐹𝑛−2 with 𝐹0 =0, 𝐹1 =1. 
We can get the f irst Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
 
Hence, the matrix representation of 𝐹=[0 1 1 1]=[𝐹0 𝐹1 𝐹1 𝐹2] will generate the sequence 𝐹𝑛 =[𝐹𝑛−1 𝐹𝑛 𝐹𝑛 𝐹𝑛+1 ] 
 
Let’s say we iterate twice 𝐹2, then 𝐹 =[0 1 1 1][0 1 1 1]=[1 1 1 2] which is also equal to the largest eigenvalue of 𝐹. 

Back in 1774, Lagrange discovered repeating patterns in the Fibonacci sequence 𝑚𝑜𝑑 𝑁. The 𝑁𝑡ℎ  Pisano  period, written 𝜋(𝑁),  is  the number of times  the Fibonacci sequence, modulo 𝑁, repeats.  

For example, if we take the first 15 Fibonacci numbers 𝐹15 with 𝐹0 =0, 𝐹1 =1, we will get 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377
Then  we  take  the  remainder  using the  modular  arithmetic  of each  number  𝑘  in  the sequence by dividing it to the 𝑁. 

If 𝑁 =3, we will get 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2 

with a pattern of:

0, 1, 1, 2, 0, 2, 2, 1, &nbsp;  0, 1, 1, 2, 0, 2, 2 

As a result, we can see the 3rd Pisano period is 8.  
 

## Python implementation 
At first, we want to load the image and get its width and height 
```
img = Image.open(input_img) 
width, height = img.width, img.height 
```

In this program, user may  only take a square size of the image. If the condition does not meet this requirement, we can create a function that resizes it to square. 
 
 
 ```
def resize_img(self, img) -> Image: 
    min_size = min(img.size) 
    imageBoxSize = 200 # maximum width of image placeholder 
 
    # arnold's cat map must be square 
    if min_size >= imageBoxSize: 
        resized_im = img.resize((imageBoxSize,imageBoxSize)) 
    else: 
        resized_im = img.resize((min_size,min_size)) 
         
    return resized_im 
 ```
 

This simply explains to resize the image to the desired size if the image exceeds the value of the image placeholder’s otherwise, resize the image to its minimum  size of (width, height) to make a square image. 
 
Now to make the chaotic map, we can create a  new canvas and take the image we have as reference.  
canvas = Image.new(img.mode, (img.width, img.height)) 
 
Given by the formula for Arnold’s Cat Map, we can draw and apply the rule on each pixel of the image in the 𝑥 and  𝑦  coordinates of the canvas  and setting the 𝑁 equal to the width or height of the image. Thus, 

 
```
done = False 
while not done: 
    for x in range(canvas.width): 
        for y in range(canvas.height): 
            nx = (2 * x + y) % canvas.width 
            ny = (x + y) % canvas.height 
      canvas.putpixel((nx,canvas.height-ny-1), 
                      img.getpixel((x, canvas.height-y-1))) 
    self.iteration += 1 
    new_image = self.images_path + f'ACM-{namex}-{self.iteration}.png' 
    canvas.save(new_image) 
    img = Image.open(new_image) 
         
    if images_the_same(self.images_path + f'ACM-{namex}-0.png', new_image): 
        done = True 
 ```
 
 
 
This is  done by iterating infinitely until we get the same  image.  This is  done using the OpenCV module in python. 
 
 
```
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
 
    if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and  
        cv2.countNonZero(r) == 0): 
        return True 
    return False 
```


As we recall the imageBoxSize  is sets to 200 because the higher size of the image will result in  longer process of doing the  map.  Overall, the time  complexity  represented in Big O notation of this program is 𝑂(𝑛<sup>2</sup>)+𝑚 where 𝑛 represents the width and height of the image and 𝑚 is the iteration until the original image reappears.

<div align="center">
 <img src="https://user-images.githubusercontent.com/67821138/176149793-64a473ea-e9fc-48ba-bf43-9d1dde411128.gif" alt="simulation">
<div/>

