# chess.com API -> https://www.chess.com/news/view/published-data-api
# The API has been used to download monthly archives for a user using a Python3 program.
# This program works as of 24/09/2018
# This code is written by Aditya Ranjan Samal, inspired by a query from Reddit.

import urllib
import urllib.request

username = "adityarnsamal"  # change the username as per your requirement
baseUrl = "https://api.chess.com/pub/player/" + \
    username + "/games/"  # fetches the base url of the user
archivesUrl = baseUrl + "archives"  # gets the archive url of the user

# read the archives url and store in a list
f = urllib.request.urlopen(archivesUrl)
archives = f.read().decode("utf-8")
archives = archives.replace("{\"archives\":[\"", "\",\"")
archivesList = archives.split("\",\"" + baseUrl)
archivesList[len(archivesList) -
             1] = archivesList[len(archivesList)-1].rstrip("\"]}")

# download all the archives
for i in range(len(archivesList)-1):
    url = baseUrl + archivesList[i+1] + "/pgn"
    filename = archivesList[i+1].replace("/", "-")
    urllib.request.urlretrieve(
        url, "/Users/adity/Downloads/chess/" + filename + ".pgn")  # change
    print(filename + ".pgn has been downloaded.")
print("All files have been downloaded.")
