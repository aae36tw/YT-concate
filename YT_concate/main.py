from pipeline.Steps.download_captions import DownloadCaptions
from pipeline.pipeline import Pipeline
from pipeline.Steps.step import StepException
from pipeline.Steps.get_video_list import GetVideoList
from utils import Utils
from pipeline.Steps.preflight import Preflight
from pipeline.Steps.postflight import Postflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
