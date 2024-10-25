from moviepy.editor import ImageClip, concatenate_videoclips
import os
import re

# 이미지가 있는 폴더 경로 설정
folder_path = "pics"  # 여기에 이미지 폴더 경로를 입력하세요.

# 폴더 내 파일 리스트 가져오기 (JPG와 PNG 형식 모두 포함)
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png"))]

# 파일 이름에서 순서와 시간을 파싱하는 함수
def parse_filename(filename):
    match = re.match(r"(\d{2})-(\d+)\.(jpg|png)", filename)  # 형식: 01-30.jpg 또는 01-30.png
    if match:
        order = int(match.group(1))       # 2자리 순서
        duration = int(match.group(2))    # 지속 시간 (초)
        return order, duration
    return None, None

# 파일을 순서대로 정렬하고 클립 생성
clips = []
for image_file in sorted(image_files, key=lambda x: parse_filename(x)[0] or 0):
    order, duration = parse_filename(image_file)
    if duration:
        filepath = os.path.join(folder_path, image_file)
        clip = ImageClip(filepath).set_duration(duration)  # 이미지 클립 생성
        clips.append(clip)

# 모든 클립을 연결하여 하나의 영상으로 결합
if clips:
    final_clip = concatenate_videoclips(clips, method="compose")
    # 비디오로 저장할 때 FPS(프레임 수) 설정
    final_clip.write_videofile("output_video.mp4", codec="libx264", fps=24)
else:
    print("유효한 이미지 파일이 없습니다.")
