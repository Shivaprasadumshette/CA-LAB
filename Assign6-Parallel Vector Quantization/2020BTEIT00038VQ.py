from sklearn.utils import shuffle
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpi4py import MPI
st = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# noprocs = comm.Get_size()
print('My rank is ',rank)
image = plt.imread("tiger.jpg")
h, w, c = image.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)
num1 = w*h*c
if rank==0:
    plt.imshow(image)
    plt.axis('off')
    plt.show()
type(image)
w, h, d = image.shape
image_array = image.reshape(w*h, d)
image_array = image_array/255
array_sample = shuffle(image_array, random_state=1)[:2000]
array_sample.size
kmeans = KMeans(n_clusters=6, random_state=1)
kmeans.fit(array_sample)
varL = kmeans.predict(image_array)
print(kmeans.cluster_centers_)
e = kmeans.cluster_centers_
def createImage(c, varL, w, h, d):
    image = np.zeros((w, h, d))
    label_idx=0

    for i in range(w):
        for j in range(h):
            image[i][j] = c[varL[label_idx]]
            label_idx+=1
    image = plt.imread("tiger.jpg")
    h1, w1, c1 = image.shape
    print('width:  ', w1)
    print('height: ', h1)
    print('channel:', c1)
    num2 = w1*h1*c1
    print(float(num1//num2))
    return image
if rank==0:
    plt.figure(1)
    plt.axis('off')
    plt.title("original")
    plt.imshow(image)
    plt.show()
    plt.figure(2)
    plt.axis('off')
    plt.title("reduced")
    image = createImage(e,varL,w,h,d)
    print(image.size)
    plt.imshow(image)
    plt.show()

elapsed_time = time.time() - st
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
