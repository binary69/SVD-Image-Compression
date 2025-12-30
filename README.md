# SVD Image Compression

A Python implementation of image compression using Singular Value Decomposition (SVD) built from scratch. This project demonstrates how linear algebra techniques can be applied to compress grayscale images while maintaining visual quality.

## Table of Contents

- [About](#about)
- [How It Works](#how-it-works)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Customization](#customization)
- [Technical Details](#technical-details)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## About

This program compresses grayscale images using Singular Value Decomposition (SVD), a matrix factorization technique that decomposes an image matrix into three components: **U**, **Σ** (singular values), and **V^T**. By retaining only the most significant singular values, we can reconstruct an approximation of the original image with significantly reduced storage requirements.

The visualization includes:
- Original image
- Compressed versions at different compression levels (k=10, 20, 50, 100)
- Compression ratio for each level
- Singular value decay plot showing the importance distribution

## How It Works

### SVD Decomposition

The image matrix **A** is decomposed as:

```
A = U @ Σ @ V^T
```

Where:
- **U** contains the left singular vectors (image patterns in row space)
- **Σ** is a diagonal matrix of singular values (importance weights)
- **V^T** contains the right singular vectors (image patterns in column space)

### Compression

By keeping only the top **k** singular values and their corresponding vectors:

```
A_compressed = U_k @ Σ_k @ V^T_k
```

This reduces storage from `m × n` to `(m × k + k + n × k)` values.

### Compression Ratio

```
ratio = (m × n) / (m × k + k + n × k)
```

Higher ratio = more compression (but potentially lower quality)

## Features

- **Custom SVD implementation**: Built from eigenvalue decomposition rather than using NumPy's built-in SVD
- **Multiple compression levels**: Compare different k values side-by-side
- **Compression ratio calculation**: See exactly how much space you're saving
- **Singular value visualization**: Understand which components contribute most to image quality
- **Educational code**: Well-commented implementation for learning purposes

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/svd-image-compression.git
cd svd-image-compression
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install numpy pillow matplotlib
```

## Usage

1. Place your test image in the `Images` folder and name it `test.jpg` (or modify the path in the script)

2. Run the script:
```bash
python svd_compression.py
```

3. The program will display a 2×3 grid showing:
   - **Top left**: Original image
   - **Top middle through bottom middle**: Compressed versions with k=10, 20, 50, 100
   - **Bottom right**: Singular value decay plot

## Example Output

For a typical image, you'll observe:

| k Value | Compression Ratio | Quality Description |
|---------|------------------|---------------------|
| k=10    | ~30-40×          | High compression, somewhat blurry |
| k=20    | ~15-20×          | Good compression, recognizable details |
| k=50    | ~6-8×            | Moderate compression, good quality |
| k=100   | ~3-4×            | Low compression, nearly identical to original |

The singular value plot helps identify the "elbow point" where additional components provide diminishing returns.

## Customization

### Change Compression Levels

```python
kVals = [10, 20, 50, 100]  # Modify these values as needed
```

### Use a Different Image

```python
img = Image.open('Images/your_image.jpg').convert('L')
```

### Adjust Numerical Threshold

```python
rank = np.sum(singularValue > 1e-10)  # Change 1e-10 for different noise tolerance
```

### Modify Plot Layout

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # Adjust grid size and figure dimensions
```

## Technical Details

### Why SVD for Image Compression?

SVD is optimal for:
- Finding the best low-rank approximation of a matrix (Eckart-Young theorem)
- Separating signal from noise
- Understanding the intrinsic dimensionality of data

### Limitations

- **Grayscale only**: Color images are converted automatically (extend to RGB by applying SVD to each channel)
- **Computational cost**: Custom implementation is O(n³); production use should leverage optimized libraries
- **Not lossy like JPEG**: Different compression paradigm; better for understanding linear algebra than practical use

### Performance Notes

The custom SVD implementation is educational. For production use:
```python
U, s, Vt = np.linalg.svd(image_matrix, full_matrices=False)
```

## Project Structure

```
svd-image-compression/
├── svd_compression.py    # Main script
├── Images/               # Image folder
│   └── test.jpg          # Your test image
├── README.md             # This file
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore file
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Enhancement

- Extend to RGB images (apply SVD to each color channel)
- Add interactive slider to adjust k value in real-time
- Compare with other compression techniques (DCT, wavelets)
- Implement progressive loading (send low-k first, then refine)
- Add PSNR/SSIM quality metrics

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created as a learning project to understand SVD and its applications in image compression and dimensionality reduction.

**Connect with me:**
- GitHub: [@binary69](https://github.com/binary69)
- LinkedIn: [Reema Hanim Hanass](linkedin.com/in/reema-hanim-h-6b8971312)

---

⭐ If you found this project helpful, please consider giving it a star!

## Acknowledgments

- Inspired by the mathematical elegance of linear algebra
- Built as part of learning numerical methods and matrix decomposition
- Thanks to the NumPy and Matplotlib communities for excellent documentation
