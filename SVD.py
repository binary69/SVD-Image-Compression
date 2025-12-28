import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#creating a method for SVD even though we can use np.linalg.svd(A) to truly go into the topic
def SVD(A):
    m,n = A.shape
    eigenValues, V = np.linalg.eig(A.T @ A)  #calculating the eigenvalue and eigenvector of (A^T).A
    eigenValues = np.real(eigenValues) #to remove the imaginary values
    V = np.real(V)

    index = np.argsort(eigenValues)[::-1]
    eigenValues = eigenValues[index]#sorted by descending order of the values
    V = V[:, index]

    singularValue = np.sqrt(np.maximum(eigenValues,0))
    rank = np.sum(singularValue>1e-10) #towards removing numerical noise, and get the number of meaningful singularValues

    U = np.zeros((m,rank))
    for i in range (rank):#fill all the columns of U
        U[:, i] = (A @ V[:, i]) / singularValue[i] #A = U@Σ@V^T , A@V = U@Σ@V^T@V , A@V = U@Σ

    return U, singularValue[:rank], V[:,:rank].T

#method to compress the image
def compress(imageMatrix, k):
    U, singularValue , VT = SVD(imageMatrix)

    Uk = U[:,:k]#keep only first k columns 
    s = singularValue[:k]
    VTk = VT [:k,:]

    compressed = Uk@np.diag(s)@VTk

    return compressed, singularValue

def calculateRatio(imageMatrix, k):
    m,n = imageMatrix.shape
    return m*n /(m*k + k + n*k)

img = Image.open('Images/test.jpg').convert('L') #convert the values into gray scale
imageMatrix = np.array(img, dtype = float)/255.0 #gray scale values are taken into an array and normalized

fig,axes = plt.subplots(2,3)
axes = axes.flatten()

axes[0].imshow(imageMatrix, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off')

kVals = [10, 20 , 50 , 100] # different compression levels I'm trying 

for index,k in enumerate(kVals):
    compressed, singularValue = compress(imageMatrix , k) # get the compressed values in mathematical format
    outImage = np.clip(compressed *255, 0, 255).astype(np.uint8) #getting the numbers to 0-255 integer vals

    axes[index + 1].imshow(outImage, cmap='gray')
    axes[index + 1].set_title(f'k={k}\nRatio: {calculateRatio(imageMatrix, k)}')
    axes[index + 1].axis('off')

axes[5].plot(singularValue, color='#008080', linewidth=2)
axes[5].set_xlabel('Component Index')
axes[5].set_ylabel('Singular Value')
axes[5].set_title('Singular Value Decay')
axes[5].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()