from pipeline.Steps.preflight import Preflight
from pipeline.Steps.get_video_list import GetVideoList
from pipeline.Steps.initialize_yt import InitializeYT
from pipeline.Steps.download_captions import DownloadCaptions
from pipeline.Steps.read_caption import ReadCaption
from pipeline.Steps.search import Search
from pipeline.Steps.download_videos import DownloadVideos
from pipeline.Steps.postflight import Postflight
from pipeline.Steps.step import StepException
from pipeline.pipeline import Pipeline
from utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
