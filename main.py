import config
import argparse
import shutil
from src.reddit import Reddit
from src.renderer import Renderer
from src.youtube import upload2YT

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="monetizer.log",
    format="[%(asctime)s] %(funcName)s %(levelname)s - %(message)s",
)

def main():
    reddit = Reddit(config.REDDIT)
    renderer = Renderer(config.BASE, **config.VIDEO)
    videos = reddit.get_videos(config.SUBREDDIT)
    
    # Create output directory
    temp_dir = config.TEMP_DIR
    temp_dir.mkdir(parents=True, exist_ok=True)

    output_dir = config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    # Loop over videos and download
    for video in videos:
        url = video["url"]
        reddit.download_video(url, temp_dir.as_posix())
    
    for video in temp_dir.glob("*.mp4"):
        renderer.render(video)
        video.unlink()
    
    shutil.rmtree(temp_dir)

    for video in output_dir.glob("*.mp4"):
        video_details = {
            'title': 'Reddit shorts #1',
            'description': 'Reddit shorts testing #1',
            'tags': 'Reddit',
            'category': 23,  # has to be an int, more about category below
            'status': 'private'  # {public, private, unlisted}
        }


        upload2YT(
            video,
            video_details
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Automatic youtube video generator from reddit content!")

    main()