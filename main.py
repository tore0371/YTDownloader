import os
import time
from pytube import YouTube 


dirPath = os.path.dirname(os.path.abspath(__file__))

def readFile(file):
    print('Reading file')
    urlFiles = file.readlines()
    # print(urlFiles)
    return urlFiles


def createDownloadsFolderIfNotExists():
    print('Creating folder')
    path = os.path.join(dirPath, "Downloads")
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            return path
        except OSError as exc:
            raise


def download(urlFiles, downloadsPath):
    print("Starting downloads")
    for url in urlFiles:
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            print(f"Descargando: {yt.title}")
            video_stream.download(downloadsPath)
            print("Descarga completada.")
            time.sleep(5)
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(5)


def main():
    file = open('urls.txt')
    urlFiles = readFile(file)
    downloadsPath = createDownloadsFolderIfNotExists()
    download(urlFiles, downloadsPath)


    
    


main()