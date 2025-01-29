# YouTube Video Downloader

This repository hosts a Python script, `youtubevideo.py`, that allows you to download YouTube videos in the best available quality. It leverages the `yt-dlp` command-line tool for downloading. This project is intended to be straightforward to use, educational, and a demonstration of video downloading techniques.

## Key Features

*   Downloads videos in the best available video and audio quality.
*   Combines audio and video into a single MP4 file.
*   Provides basic error handling for common issues.
*   Includes clear usage instructions.

## Prerequisites

Before you can use this script, you'll need to ensure you have the necessary software installed:

1.  **Python 3.6 or Higher:**
    *   This script is written in Python and requires version 3.6 or later.
    *   Download the latest version from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    *   Follow the installation instructions for your specific operating system.
    
2. **yt-dlp:**
    *   This is a command-line program that is used for downloading videos.
    *   Install this by running the following command in your terminal or command prompt:
         ```bash
        pip install yt-dlp
         ```

## How to Use

Follow these steps to start downloading YouTube videos:

1.  **Clone or Download the Repository:**
    *   You can either clone this repository to your local machine using Git, or download it as a ZIP file:
        ```bash
        git clone https://github.com/weld1993/YouTube-Video-Downloader.git
        ```
    *   If you choose to download the ZIP file, you'll need to extract it.
    
2.  **Locate the Script:**
    *   Navigate to the location on your computer where you downloaded or cloned the repository.
    *   You should find a file named `youtubevideo.py`.

3.  **Modify Download Path (Optional):**
    *   By default, the videos will be downloaded to a directory specified in the code.
    *   If you wish to use a different download location, you need to:
         1.  Open `youtubevideo.py` with a text editor.
         2.  Locate the `download_dir` variable and modify the path as needed.
          ```python
          download_dir = r"PATH_TO_YOUR_DOWNLOAD_DIRECTORY" # Replace with your preferred download directory.
          ```
       *   Replace `PATH_TO_YOUR_DOWNLOAD_DIRECTORY` with your desired path.
   
 4. **Modify the video url (Optional)**
   *   By default, the code has a hardcoded video url.
   *   If you want to download a different video, you need to:
     1. Open `youtubevideo.py` with a text editor.
     2. Locate the `video_url` variable and modify the url as needed.
      ```python
       video_url = "https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID" # Replace with the url of the youtube video you want.
      ```
   *   Replace `https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID` with the url of the youtube video that you want.

5.  **Run the Script:**
    *   Open a terminal (macOS/Linux) or command prompt (Windows)
    *   Navigate to the directory where you have `youtubevideo.py`.
    *   Run the script by entering:
       ```bash
       python youtubevideo.py
        ```

6. **Check for Downloaded Videos:**
    * Once the script finishes, your video will be in the directory you specified.
    * The name of the downloaded video will be the same as the name of the video on youtube.

## Important Notes
*  **Legal and Ethical Considerations**: It is important to note that downloading copyrighted material might be against YouTube's terms of service. This script is meant for educational purposes, personal use, and for content where you have permission to download.
*   **Video Quality**: The script downloads the best available video and audio quality and merges them.

## Issues

If you experience any issues with the script or have any suggestions for improvement, please feel free to open an issue on this repository. Your contributions and feedback are always welcome!
