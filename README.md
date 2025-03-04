# Social Media Video Downloader

Social Media Video Downloader app for downloading social media videos with it link.
The app downloads automatically the highest resolution video.
Note: Designed for personal use, respecting platform terms and content creators.

## Features

- Support for multiple platforms: YouTube, Instagram, Facebook, LinkedIn, Snapchat, and Twitter.
- Advanced scraping techniques to retrieve video content.
- Automatic merging of video and audio streams for platforms that separate media components.
- User-friendly web interface built with HTML, CSS, and JavaScript.
- Backend powered by Django and Python for robust performance.
- Video processing with FFmpeg, ensuring wide format support and high-quality outputs.

## Installation

Before you begin, ensure you have the latest version of Python installed on your system. Additionally, FFmpeg should be installed and accessible in your system's PATH.

1. Clone the repository:
   ```sh
   git clone https://github.com/erik-pinhasov/socialDownloader.git
   cd socialDownloader
2. Install the required Python dependencies:
   ```sh
   pip install -r requirements.txt
3. Run the Django development server:
   ```sh
   python manage.py runserver
4. Open your web browser and navigate to http://127.0.0.1:8000/ to start using the application.
* In case you don't have FFmpeg installed download it from FFmpeg offical website: https://ffmpeg.org/download.html. You can add it to your OS path or placing binary file in mediaHandler directory.

## Usage
   1. Navigate to the homepage of the application.
   2. Enter the URL of the video you wish to download in the input field.
   3. Click the download button.
   4. The application will process the request, and download the highest resolution video.
   * Do not support private accounts videos and age restricted videos.
