import numpy as np
import argparse
import data_collector as dc
import utils as ut

parser = argparse.ArgumentParser(description="Analyze a video's different time frames")
parser.add_argument("video", help="Video to analyze", type=str)
args = parser.parse_args()

starting_times = [0, 0.25, 0.5, 0.75, 0, 0.5, 0]
ending_times = [0.25, 0.5, 0.75, 1, 0.5, 1, 1]

data = np.ones((len(starting_times), 3))
for i in range(len(data)):
   data[i][0] = starting_times[i]
   data[i][1] = ending_times[i]
   data[i][2] = dc.collect(args.video, filter_signal=True, persist=False, verbose=False, time_start=starting_times[i], time_finish=ending_times[i]) 

header = "# {}'s video. Fixed window size, varying times\n time_start, time_finish, bpm".format(args.video.split('/')[-1].split('.')[0])

ut.pretty_print(header, data)
