import csv
import numpy as np

def load_frames(cap,upperLeftCornerX,upperLeftCornerY,lowerRightCornerX,lowerRightCornerY,length, time_start, time_finish):

    current_frame_no = 0
    frame_start  = int(time_start * length)
    frame_finish = int(time_finish * length)
    r = np.zeros((1,frame_finish - frame_start))
    g = np.zeros((1,frame_finish - frame_start))
    b = np.zeros((1,frame_finish - frame_start))
    while(cap.isOpened() and current_frame_no < frame_finish):
        ret, frame = cap.read()

        if ret == True and frame_start <= current_frame_no <= frame_finish:
            r[0,current_frame_no-frame_start] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,2])
            g[0,current_frame_no-frame_start] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,1])
            b[0,current_frame_no-frame_start] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,0])
        elif not ret or current_frame_no > frame_finish:
            break
        current_frame_no += 1
    return [r, g, b]

def write_csv(filename, r, g, b, R, G, B):
    with open("{}.csv".format(filename), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(['r','g','b','R','G','B'])
        for i in range(len(r)):
            csv_writer.writerow([r[i],g[i],b[i],R[i],G[i],B[i]])


def read_csv(file_name):
    split_file_name = file_name.split('.')[0].split('_')
    length = int(split_file_name[-1])
    fps = int(split_file_name[-2])
    r , g, b = np.zeros((1,length)), np.zeros((1,length)), np.zeros((1,length))
    R , G, B = np.zeros((1,length)), np.zeros((1,length)), np.zeros((1,length))
    with open('./recolected_info/{}'.format(file_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                r[0][line_count-1] = row[0]
                g[0][line_count-1] = row[1]
                b[0][line_count-1] = row[2]
                R[0][line_count-1] = row[3]
                G[0][line_count-1] = row[4]
                B[0][line_count-1] = row[5]
            line_count += 1
        return r, g, b, R, G, B, fps

# file name convention:
# '{video name}_{frames per second}_{amount of frames}_{window size}_{filtered or not}.{[png|csv]}'
def filename_builder(title, fps, len_r, window_size, filtered):
    return './recolected_info/{}_{}_{}_{}_{}'.format(title, int(fps), len_r, window_size, "filtered" if filtered else "nfiltered")


def pretty_print(headers, data):
    print(headers)
    for i in range(len(data)):
        print(",".join([str(round(j,2)) for j in data[i]]))

