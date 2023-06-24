# YouTube Playlist Video Information Scraper

This Python script allows you to retrieve information about videos in a YouTube playlist and store it in a CSV file. It uses the `pytube` library to interact with the YouTube API and extract video details.

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies by running the following command:

   ```shell
   pip install pytube

# Usage
1.Open the script file (youtube_project.py)

2.Modify the playlist variable in the script to include the URL of the YouTube playlist you want to scrape.

3.Adjust the start and end arguments in the get_playlist function to specify the range of videos you want to retrieve.

4.Save the changes to the script.

5.Run the script using Python:
```shell
python youtube_project.py
```
6.Once the script completes, it will generate a CSV file named info.csv in the same directory. The file will contain information about the videos in the specified range, including their title, URL, number, publish date, length, and views Contributing
