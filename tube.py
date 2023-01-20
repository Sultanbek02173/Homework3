from pytube import YouTube
import shutil

# url = input("Введите сылку: ")
# yt = YouTube(url)
# print("Начинает скачивать")
# yt.streams.filter(progressive = True, file_extension = "mp4").order_by('resolution').desc().first().download()

path = "audio"

shutil.rmtree(path)
print("/home/school/math/final удалена.")