import  os
from moviepy import VideoFileClip
from PIL import Image

video_path = "videoplayback.mp4"
clip = VideoFileClip(video_path)

output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

#extract frames

for i, frame in enumerate(clip.iter_frames(fps=10, dtype="uint8")):
    frame_path = os.path.join(output_folder, f"frame_{i:04d}.png")
    img = Image.fromarray(frame)
    img.save(frame_path)

print("frames done extracting!")
