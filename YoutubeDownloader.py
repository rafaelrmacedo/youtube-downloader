import os
from pytube import YouTube
from moviepy.editor import AudioFileClip

def MP4ToMP3(mp4, mp3):
    try:
        FILE_TO_CONVERT = AudioFileClip(mp4)
        FILE_TO_CONVERT.write_audiofile(mp3)
        FILE_TO_CONVERT.close()
        print("Conversion successful! MP3 file saved.")
    except Exception as e:
        print(f"Error during conversion: {e}")

while True:
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print('Youtube Downloader'.center(40, '_'))

        option = 0

        while option not in (1, 2, 3):
            option = int(input('\n1. Download audio\n2. Download video\n3. Exit\n\nOption here: '))

            if option == 1:
                URL = input('Enter youtube url: ')
                yt_audio = YouTube(url=URL)
                audio_stream = yt_audio.streams.filter(only_audio=True).first()
                audio_stream.download()
                MP4ToMP3(audio_stream.default_filename, audio_stream.default_filename.split('.')[0] + '.mp3')

            elif option == 2:
                URL = input('Enter youtube url: ')
                yt_video = YouTube(url=URL)
                video_stream = yt_video.streams.get_highest_resolution()
                video_stream.download()

            elif option == 3:
                break
            else:
                print("Invalid option. Please enter a valid option.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        option = input('\n1. Download again\n2. Exit\n\nOption here: ')

        if option != '1':
            break
        else:
            print('Invalid option.')