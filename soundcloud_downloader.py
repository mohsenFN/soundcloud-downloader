import requests
from bs4 import BeautifulSoup
import secrets
from os import remove

# Use a Session object to make requests.
session = requests.Session()

# Set the save directory to the current directory.
save_dir = "./songs"

# Set the URL for soundcloud.
url = "https://www.klickaud.co/download.php"

# Get the SoundCloud link from the user.
link = str(input("Enter SoundCloud Link > "))


def get_download_link(url, data):
    """
    Retrieve the download link from the response HTML.

    :param url: str - The URL for the request.
    :param data: dict - The POST data to send in the request.
    :return: str - The download link.
    """
    response = session.post(url, data=data)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    download_link = soup.find('div', {'id': 'dlMP3'})['onclick'].split("'")[1]
    return download_link


def download_file(url, directory, file_name):
    """
    Download the file at the provided URL to the directory with the provided file name.
    
    :param url: str - The URL of the file to download.
    :param directory: str - The directory where the file will be saved.
    :param file_name: str - The name of the file to save.
    :return: None
    """
    response = session.get(url)
    if response.ok:
        with open(f"{directory}/{file_name}.mp3", 'wb') as f:
            f.write(response.content)
        print(f"MP3 saved to ./songs/{file_name}.mp3.")
    else:
        print("Error !")


# POST data.
data = {
    "value": link,
    secrets.token_hex(12): secrets.token_hex(12)
}

# Get the download link.
download_link = get_download_link(url, data)

# Download the file.
save_name = str(input("mp3 file name > "))
download_file(download_link, save_dir, save_name)




# By Mohsen Core :)
