import os
import shutil
def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        backslash = '\\'
        print(f"Le dossier {folder_path.split(backslash)[-1]} a été créé.")
    except OSError as e:
        print(f"Erreur lors de la création du dossier : {e}")

# Creation du dossier pricipal

folder_path = input("Entrez le chemin du dossier principal : ")
create_folder(folder_path)

exercise_folder =os.path.join(folder_path,"newFolder")
create_folder(exercise_folder)


folder_to_make = ["testVitesse","dataSample"]

for folder in folder_to_make:
    create_folder(os.path.join(exercise_folder,folder))

file_to_make_in_testVitesse = ["moi","gagnant"]

for file in file_to_make_in_testVitesse:
    output_location = os.path.join(exercise_folder,"testVitesse", file)
    with open(f"{output_location}.py", "w", encoding="utf-8") as output:
        pass

file_to_copy = ["generateurReponse","generateurTest","partialInput","template"]

for file in file_to_copy:
    output_location = os.path.join(exercise_folder,file)
    with open(f"{file}.py","r",encoding="utf-8")as input:
        with open(f"{output_location}.py","w",encoding="utf-8")as output:
            output.write(input.read())
