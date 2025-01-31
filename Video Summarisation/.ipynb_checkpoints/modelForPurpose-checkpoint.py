import cv2

# Input and output file paths
input_file = 'umcp.mpg'  # Replace with your .mpg file
output_file = 'video.mp4'  # Desired output .mp4 file

# Open the input video
cap = cv2.VideoCapture(input_file)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Unable to open the input file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4

# Create the VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# Read frames from the input video and write to the output video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame to the output file
    out.write(frame)

# Release resources
cap.release()
out.release()

print(f"Conversion complete. Saved as {output_file}")