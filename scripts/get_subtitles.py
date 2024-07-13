#!/usr/bin/env python3

import requests
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='get_subtitles',
                    description='gets the sustitles for a given series of Masterchef from subsaga.com',
                    )

parser.add_argument('series')

args = parser.parse_args()

# set the url
series_url = f"https://subsaga.com/bbc/entertainment/masterchef/series-{str(args.series)}/"

# some series are incomplete, very annoying
# start with the complete series


# requests post request to ge the subtitles

# save it in text format in the data dir
