from moviepy.editor import VideoFileClip, CompositeVideoClip, vfx
from pathlib import Path
from skimage.filters._gaussian import gaussian

import logging
logger = logging.getLogger(__name__)


class Renderer:
    def __init__(self, base_dir: Path, resolution: tuple[str, str], audio_codec: str = "aac", blur: bool = False):
        self.base_dir = base_dir
        self.resolution = resolution
        self.blur = blur
        self.audio_codec = audio_codec

    @staticmethod
    def __blur(image):
        """ Returns a blurred (radius=2 pixels) version of the image """
        return gaussian(image.astype(float), sigma=25)


    def render(self, video_file: Path):
        """
        The render function takes a video file and renders it with the given parameters.
        It also creates a directory to store the rendered video in.
        
        :param self: Access the class attributes
        :param video_file: Path: Specify the path to the video file that is being rendered
        :return: The path to the rendered video
        """
        logging.info(f"Processing video: {video_file.name}")
        out_clip = self.base_dir.joinpath("results")
        out_clip.mkdir(parents=True, exist_ok=True)
        
        out_clip = out_clip.joinpath(video_file.name)
        main_clip = VideoFileClip(video_file.as_posix())

        bg = VideoFileClip(video_file.as_posix()).resize(self.resolution)
        bg = bg.fx(vfx.colorx, 0.5)
        if self.blur:
            logging.info("Applying blur to background.")
            bg = bg.fl_image(self.__blur)

        main_clip = main_clip.resize(width=self.resolution[0])  # resize clip to fit screen
        main_clip = main_clip.set_start(0)

        # combine bg and clip with centering
        video = CompositeVideoClip([bg, main_clip.set_position("center", "center")])
        # render clip given directory
        video.write_videofile(out_clip.as_posix(), audio_codec=self.audio_codec)
        logging.info(f"Completed video file and saved as: {out_clip}")
        