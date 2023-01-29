
import praw
from redvid import Downloader

import logging

logger = logging.getLogger(__name__)

class Reddit:
    def __init__(self, credentials: dict) -> None:
        self._reddit = praw.Reddit(
            **credentials
        )

    def get_content(self, subreddit: str, limit: int = 25) -> list:
        """
        The get_content function is a function that takes in the limit of 25 posts from the subreddit and returns them.
        
        :param self: Reference the instance of the class
        :param limit: int: Limit the number of posts to return
        :return: A list of the top 25 posts in a subreddit
        """
        sub = self._reddit.subreddit(subreddit).top(limit=limit)
        return sub

    def get_videos(self, subreddit: str, limit: int = 25, time_filter: str = "week") -> list:
        """
        The get_videos function takes a subreddit name and returns a list of tuples.
        Each tuple contains the URL, title, and author of each video found on the given subreddit.
        
        :param self: Reference the class instance
        :param subreddit: str: Specify the subreddit to be parsed
        :param limit: int: Limit the number of posts that are parsed
        :return: A list of tuples
        """
        output = []
        sub = self._reddit.subreddit(subreddit).top(time_filter=time_filter, limit=limit)
        
        for elem in sub:
            logger.info(f"Parsing: title - {elem.title}")
            
            # Get Videos
            if not elem.is_video:
                continue

            # Filter content
            if elem.stickied:
                continue
            
            # Filter for age
            if elem.over_18:
                continue
            
            url = elem.url
            title = elem.title
            author = elem.author_fullname
            logging.info(f"Found video: {title} - {elem.subreddit} - {author} - {url}")
            video = {
                "title": title,
                "url": url,
                "author": author
            }
            output.append(video)
        return output

    def download_video(self, url: str, save_to: str):
        """
        The download_video function downloads a video from the given url to the specified save_to location.
        
        :param self: Access the class attributes
        :param url: str: Specify the url of the video that will be downloaded
        :param save_to: str: Specify the path to save the video to
        :return: The path to the video that was downloaded
        """
            
        logging.info(f"Downloading: {url} to {save_to}")
        downloader = Downloader(url, max_q=True)
        downloader.path = save_to
        downloader.download()
        logging.info(f"Download complete. {save_to}")
    
