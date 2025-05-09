#in day 75 we are going do another excersize called clear the clutter in python.......using os module......
import os
files=os.listdir("clutteredfolder")
i=1

for file in files:
    if file.endswith(".png"):
     print(file)
    os.rename(f"clutteredfolder/{file}" , f"clutteredfolder/{i}.png")
    i=i+1
    