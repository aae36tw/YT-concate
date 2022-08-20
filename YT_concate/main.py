from pipeline.Steps.get_video_list import GetVideoList
from pipeline.Steps.step import StepException
from pipeline.pipeline import Pipeline
from pipeline.Steps.get_video_list import GetVideoList


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
