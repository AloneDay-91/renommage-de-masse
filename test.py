import os

folder = r'C:\Users\elelo\OneDrive\Documents\Cours Terminale\SIN\PYTHON\renommage de masse\images\\'
count = 1

for file_name in os.listdir(folder):
    source = folder + file_name

    destination = folder + "image_" + str(count) + ".png"
    os.renames(source, destination)
    count += 1
print('Nouveaux Noms :')
res = os.listdir(folder)
print(res)