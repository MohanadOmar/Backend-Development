import os
import shutil

FROM_PATH = r"C:\Users\Mohanad\Downloads"
TO_PATH = r"C:\Users\Mohanad"

IMAGES_FORMATS = ['jpg', '.jpeg', '.png']
VIDEOS_FORMATS = ['.mp4', '.wav', '.mov']
APPLICATIONS_FORMATS = ['.exe']
DOCUMENTS_FORMATS = ['.doc', '.txt', '.pdf', '.docm', '.docx']

downloads_files = os.listdir(FROM_PATH)
for file in downloads_files:
    # Images Format
    if ".jpg" in file or ".jpeg" in file or ".png" in file:
        shutil.move(f"{FROM_PATH}\{file}", f"{TO_PATH}\Pictures\{file}")
        print(f"{file} Moved")

    # Videos Format
    elif ".mp4" in file or ".wav" in file or ".mov" in file:
        shutil.move(f"{FROM_PATH}\{file}", f"{TO_PATH}\Videos\{file}")
        print(f"{file} Moved")

    # Applications Format
    elif ".exe" in file:
        shutil.move(f"{FROM_PATH}\{file}", f"{TO_PATH}\Apps\{file}")
        print(f"{file} Moved")

    # Documents Format
    elif ".doc" in file or ".txt" in file or ".pdf" in file or ".docm" in file or ".docx" in file:
        if ".pdf" in file:
            shutil.move(f"{FROM_PATH}\{file}", f"{TO_PATH}\Documents\PDF\{file}")
        shutil.move(f"{FROM_PATH}\{file}", f"{TO_PATH}\Documents\DOC\{file}")
        print(f"{file} Moved")

    # Others
    else:
        print(f"{file} Saved as Others")
