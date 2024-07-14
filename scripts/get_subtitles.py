#!/usr/bin/env python3

import requests
import argparse
from pathlib import Path
import logging

logger = logging.getLogger("logs")
logger.setLevel(logging.DEBUG)

ch_logs = logging.StreamHandler()
ch_logs.setLevel(logging.INFO)
logger.addHandler(ch_logs)

parser = argparse.ArgumentParser(
    prog="get_subtitles",
    description="gets the subtitles for a given series of Masterchef from subsaga.com",
)

parser.add_argument("series", type=str)

args = parser.parse_args()

# set the url
series_url = f"https://subsaga.com/bbc/entertainment/masterchef/series-{args.series}/"

logger.info(f"Fetching subtitles for series {args.series} from {series_url}")

# set up directories to save subtitle data
# skips if the directories already exist
subtitles_dir = Path(__file__).parent.parent / f"data/subtitles"
subtitles_dir.mkdir(exist_ok=True)
series_dir = subtitles_dir / f"series_{args.series}"
series_dir.mkdir(exist_ok=True)

logger.info(f"Made subtitle directory at {series_dir}")

# number of episodes is variable per series
# it is always <30, so iterate through episodes up to 30

successful_eps = []
for number in range(1, 30):
    ep_url = series_url + f"episode-{str(number)}.srt"
    subs = requests.post(ep_url)
    if subs.status_code == 200:
        out_path = series_dir / f"series{args.series}_{str(number)}.txt"
        with open(out_path, "w") as f:
            f.write(subs.content.decode())
        successful_eps.append(number)

logger.info(f"{str(len(successful_eps))} episodes found  - finished!")
