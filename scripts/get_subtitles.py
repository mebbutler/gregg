#!/usr/bin/env python3

import requests
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='get_subtitles',
                    description='gets the subtitles for a given series of Masterchef from subsaga.com',
                    )

parser.add_argument('series', type=str)

args = parser.parse_args()

# set the url
series_url = f"https://subsaga.com/bbc/entertainment/masterchef/series-{str(args.series)}/"

# number of episodes is variable per series
# it is always <30, so iterate through episodes up to 30
# if the request returns a 404, skip the number
# requests post request to get the subtitles

for number in range(1,30):
    ep_url = series_url + f"episode-{str(number)}.srt"
    subs = requests.post(ep_url)
    print(subs.status_code)
    if subs.status_code == 200:
        out_path = Path(__file__).parent.parent / f"data/masterchef/series{str(args.series)}_{str(number)}.txt"
        with open(out_path, "w") as f:
            f.write(subs.content.decode())


# save it in text format in the data dir
