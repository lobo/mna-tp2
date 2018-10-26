import numpy as np
import argparse
import data_collector as dc
import utils as ut

parser = argparse.ArgumentParser(description="Analyze a video's different window sizes")
parser.add_argument("video", help="Video to analyze", type=str)
args = parser.parse_args()

# [30, 60, ..., 270, 300]
window_sizes = np.arange(30,301,30)
data = np.ones((len(window_sizes), 2))
for i in range(len(window_sizes)):
    data[i][0] = window_sizes[i]
    data[i][1] = dc.collect(args.video, window_sizes[i], filter_signal=True, persist=False, verbose=False) 


header = "# {}'s video, full length\n size, bpm".format(args.video.split('/')[-1].split('.')[0])

ut.pretty_print(header, data)
