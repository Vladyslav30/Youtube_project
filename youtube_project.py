# Import necessary modules from pytube library
from pytube import Playlist, YouTube

# Function to retrieve information about videos in a playlist within a given range
def get_playlist(playlists, start, end):
    # Dictionary to store video information
    urls = {}
    # Counter variable for video number
    count_1 = 1

    # Iterate over each playlist URL
    for playlist in playlists:
        # Create a Playlist object using the URL
        playlist_urls = Playlist(playlist)

        # Iterate over each video URL in the playlist
        for url in playlist_urls:
            # Check if the current video falls within the desired range
            if count_1 < end + 1 and count_1 > start - 1:
                # Create a YouTube object for the video
                yt = YouTube(url)
                # Retrieve relevant information about the video
                title = yt.title
                publish_date = yt.publish_date.date()
                length_of_video = yt.length
                hours, remainder = divmod(length_of_video, 3600)
                minutes, seconds = divmod(remainder, 60)
                length_of_video = f'{hours}:{minutes:02d}:{seconds:02d}' if hours else (f'{minutes}:{seconds:02d}' if seconds else f'{minutes}')
                number_of_views = yt.views
                # Store the video information in a dictionary with the title as the key
                urls[title] = (url, count_1, publish_date, length_of_video, number_of_views)
            else:
                pass

            # Increment the video number counter
            count_1 += 1

    # Return the dictionary of video information
    return urls

# Define the playlist URLs
playlist = ['https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f']
# Call the function to get video information from the playlist within the range 1-21
pl_urls = get_playlist(playlist, 1, 21)

# Write the video information to a CSV file
with open('info.csv', 'w', encoding='utf-8-sig') as f:
    # Write the header row
    f.write('Title,URL,Number,Publish Date,Length,Views\n')
    # Iterate over the video information dictionary and write each row
    for key, value in pl_urls.items():
        f.write(f'{key},{value[0]},{value[1]},{value[2]},{value[3]},{value[4]}\n')



