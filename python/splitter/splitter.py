from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# Replace the filename below.
required_video_file = "filename.mp4"

times = ["0-30", "30-60", "60-90", "90-120", "120-150", "150-180"]

print("TIMES :", times)

for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  ffmpeg_extract_subclip(required_video_file,
                         starttime, endtime,
                         targetname="{}_{}.mp4".format(required_video_file, times.index(time)+1))
