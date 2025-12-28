\# SVD Image Compression



A Python implementation of image compression using Singular Value Decomposition (SVD) from scratch. This project demonstrates how SVD can be used to compress grayscale images by retaining only the most significant singular values.



\## What It Does



This program compresses grayscale images using SVD, a matrix factorization technique that decomposes an image matrix into three components: U, Σ (singular values), and V^T. By keeping only the top k singular values, we can reconstruct an approximation of the original image with reduced storage requirements.



The visualization shows:

\- Original image

\- Compressed versions at different compression levels (k=10, 20, 50, 100)

\- Compression ratio for each level

\- Singular value decay plot showing how rapidly the importance drops off



\## Features



\- \*\*Custom SVD implementation\*\*: Built from eigenvalue decomposition rather than using numpy's built-in SVD

\- \*\*Multiple compression levels\*\*: Compare different k values side-by-side

\- \*\*Compression ratio calculation\*\*: See exactly how much space you're saving

\- \*\*Singular value visualization\*\*: Understand which components contribute most to image quality



\## Requirements



```bash

pip install numpy pillow matplotlib

```



Or install from requirements.txt:

```bash

pip install -r requirements.txt

```



\## Usage



1\. Place your test image in the same directory as the script and name it `test.jpg` (or modify the filename in the code)



2\. Run the script:

```bash

python svd\_compression.py

```



3\. The program will display a 2x3 grid showing:

&nbsp;  - Top left: Original image

&nbsp;  - Top middle through bottom middle: Compressed versions with k=10, 20, 50, 100

&nbsp;  - Bottom right: Singular value decay plot



\## How It Works



\*\*SVD Decomposition:\*\*

The image matrix A is decomposed as: A = U @ Σ @ V^T



Where:

\- U contains the left singular vectors (image patterns in row space)

\- Σ is a diagonal matrix of singular values (importance weights)

\- V^T contains the right singular vectors (image patterns in column space)



\*\*Compression:\*\*

By keeping only the top k singular values and their corresponding vectors, we get:

A\_compressed = U\_k @ Σ\_k @ V^T\_k



This reduces storage from m×n to (m×k + k + n×k) values.



\*\*Compression Ratio:\*\*

```

ratio = (m × n) / (m×k + k + n×k)

```

Higher ratio = more compression (but potentially lower quality)



\## Example Output



For a typical image, you'll see:

\- k=10: High compression (~30-40x ratio), somewhat blurry

\- k=20: Good compression (~15-20x ratio), recognizable details

\- k=50: Moderate compression (~6-8x ratio), good quality

\- k=100: Low compression (~3-4x ratio), nearly identical to original



\## Customization



\*\*Change compression levels:\*\*

```python

kVals = \[10, 20, 50, 100]  # Modify these values

```



\*\*Use a different image:\*\*

```python

img = Image.open('your\_image.jpg').convert('L')

```



\*\*Adjust numerical threshold:\*\*

```python

rank = np.sum(singularValue > 1e-10)  # Change 1e-10 for different noise tolerance

```



\## Notes



\- Only works with grayscale images (color images are converted automatically)

\- Larger k values = better quality but less compression

\- The singular value plot helps identify the "elbow point" for optimal compression

\- Custom SVD implementation is educational; for production use `np.linalg.svd()` for better performance



\## Project Structure



```

svd-image-compression/

├── svd\_compression.py

├── test.jpg              # Your test image goes here

├── README.md

└── requirements.txt

```



\## License



Free to use for educational and personal projects.



\## Author



Created as a learning project to understand SVD and its applications in image compression.

