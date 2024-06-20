import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

image_raw = imread("labimage.jpg")
print(image_raw.shape)
plt.imshow(image_raw, cmap='grey')
plt.show()

image_sum = image_raw.sum(axis=2)
print(image_sum.shape)
image_bw = image_sum/image_sum.max()
print(image_bw.max())
plt.imshow(image_bw, cmap='grey')
plt.show()

pca = PCA()
pca.fit(image_bw)

cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
print(cumulative_variance)

num_components = np.argmax(cumulative_variance >= 0.95) + 1
print(num_components)

plt.plot(cumulative_variance, color='pink')
plt.xlabel('Principal components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance explained by the components')
plt.axhline(y=0.95, color='green')
plt.axvline(x=num_components, color='yellow')
plt.show()


pca = PCA(n_components=num_components)
image_transformed = pca.fit_transform(image_bw)
image_reconstructed = pca.inverse_transform(image_transformed)


plt.imshow(image_reconstructed, cmap='gray')
plt.title(f'{num_components} components')
plt.show()

def reconstruct_image(image, num_components):
    pca = PCA(n_components=num_components)
    image_transformed = pca.fit_transform(image)
    image_reconstructed = pca.inverse_transform(image_transformed)
    return image_reconstructed

components_list = [1, 2, 3, 4, 5, 10, 15, 20, 30]
fig, axes = plt.subplots(3, 3, figsize=(7, 7))

for axes, num_components in zip(axes.flatten(), components_list):
    image_reconstructed = reconstruct_image(image_bw, num_components)
    axes.imshow(image_reconstructed, cmap='gray')
    axes.set_title(f'{num_components} components')
    axes.axis(False)

plt.show()