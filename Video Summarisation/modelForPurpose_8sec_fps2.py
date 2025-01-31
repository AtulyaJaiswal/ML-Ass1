import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load video and extract frames
video_path = './video.mp4'
cap = cv2.VideoCapture(video_path)
frames = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(cv2.resize(frame, (256, 256)))  # Resize for efficiency

cap.release()

# Convert frames to feature vectors
frame_vectors = np.array([f.flatten() for f in frames])

# Apply PCA for dimensionality reduction
pca = PCA(0.95)  # Retain 95% variance
reduced_features = pca.fit_transform(frame_vectors)

# Number of clusters based on desired duration
desired_duration = 8  # Desired video duration in seconds
fps = 2  # Frames per second for the summarized video
n_clusters = min(len(frames), desired_duration * fps)  # Ensure enough clusters for duration

# Cluster frames
kmeans = KMeans(n_clusters=n_clusters, random_state=80)
labels = kmeans.fit_predict(reduced_features)

# Select keyframes (closest to cluster centers, ensuring even distribution)
keyframes = []
used_indices = set()

for cluster in range(kmeans.n_clusters):
    cluster_indices = np.where(labels == cluster)[0]
    centroid = kmeans.cluster_centers_[cluster]
    closest_idx = cluster_indices[np.argmin(np.linalg.norm(reduced_features[cluster_indices] - centroid, axis=1))]

    # Avoid selecting duplicate frames
    if closest_idx not in used_indices:
        keyframes.append(frames[closest_idx])
        used_indices.add(closest_idx)

# Ensure keyframes are sorted in temporal order
keyframes = [frames[idx] for idx in sorted(used_indices)]

# Adjust FPS to match keyframes and duration
adjusted_fps = max(1, len(keyframes) // desired_duration)

# Parameters for the output video
output_video_path = 'summarized_video.mp4'
frame_size = (256, 256)

# Initialize VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter(output_video_path, fourcc, adjusted_fps, frame_size)

# Write keyframes to the output video
for keyframe in keyframes:
    out.write(keyframe)

out.release()
print(f"Summarized video saved as {output_video_path} with duration ~{len(keyframes) / adjusted_fps:.2f} seconds")
