from moviepy.editor import VideoFileClip

clip = VideoFileClip("/Users/ahmedalmaqbali/Desktop/Muaeen/gitProjects/projects/10 Second Countdown _ After Effects.mp4")
clip.write_gif("mygif.gif")