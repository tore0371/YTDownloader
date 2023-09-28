from pytube import YouTube

import os
import time


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
    else:
        return path


def Download(links, downloadPath):
    print("Starting downloads")
    for link in links:
        print("URL --> " + link)
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download(output_path=downloadsPath)
        except:
            print("An error has occurred")
        print("Download is completed successfully")


file = open('urls.txt')
urlFiles = readFile(file)
downloadsPath = createDownloadsFolderIfNotExists()
Download(urlFiles, downloadsPath)