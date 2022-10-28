import os

print(os.path.join("./videos", "Suzume no Tojimari OST『Suzume』 [qal34e9v_pk].webm"))

print(os.listdir("./videos"))

# url = "https://www.youtube.com/watch?v=qal34e9v_pk"

# print(os.popen(f"cd ./videos; yt-dlp \"{url}\"; cd ..").read())
# # print(subprocess.run(f"cd ./videos ; yt-dlp \"{url}\" ; cd ..".split(" "), capture_output=True))
