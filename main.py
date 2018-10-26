import argparse
import data_collector as dc

parser = argparse.ArgumentParser(description="Beats per minute monitor using FFT by analyzing a video")
parser.add_argument("video", help="Video to analyze", type=str)
parser.add_argument("--size", "-s", help="Size of observed window. It is a square in the center of the screen.",
        type=int, default=300)
parser.add_argument("--npfft",help="Use numpy's fft method if True, use custom method if False",type=bool,default=True)
parser.add_argument("--filter", help="Filter the frecuencies between 50 and 130 bpm.", type=bool, default=False)
parser.add_argument("--persist", help="Persist the data.", type=bool, default=True)
parser.add_argument("--time_start",help="Double between [0,1) that determines the % of the length of the video from which to start. (time_start < time_finish)]", type=float, default=0)
parser.add_argument("--time_finish",help="Double between (0,1] that determines the % of the length of the video until we stop analyzing. (time_start < time_finish))", type=float, default=1)

args = parser.parse_args()

dc.collect(args.video, args.size, args.npfft, args.filter, args.persist, True, args.time_start, args.time_finish)
