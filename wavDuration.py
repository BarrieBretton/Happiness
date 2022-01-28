import wave
import contextlib
import os
import math

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return (hour, minutes, math.floor(seconds))

def readFolder(dirName, wavLogOnly = True, hideLogs = False, showExceptions = True):
    wavFileDurations = []

    os.chdir(dirName)
    for _index, fname in enumerate(os.listdir(dirName)):
        if fname.endswith('.wav'):
            try:
                with contextlib.closing(wave.open(fname,'r')) as f:
                    frames = f.getnframes()
                    rate = f.getframerate()
                    duration = frames / float(rate)

                wavFileDurations.append(convert(duration))
                print(f'{_index+1}: wav   > {fname}')
                print("    %d:%02d:%02d" % convert(duration))

            except Exception:
                wavFileDurations.append(-1)
                if showExceptions:
                    print(f'{_index+1}: Read exception   > {os.path.splitext(fname)[-1][1:]}   > {fname}')

        else:
            wavFileDurations.append(-1)
            if not wavLogOnly:
                print(f'{_index+1}: {os.path.splitext(fname)[-1][1:]}   > {fname}')
    
    totalSecondsFromHours = sum([i[0] for i in wavFileDurations if type(i) == tuple])*3600
    totalSecondsFromMinutes = sum([i[1] for i in wavFileDurations if type(i) == tuple])*60
    totalSecondsOnly = sum([i[2] for i in wavFileDurations if type(i) == tuple])

    totalSeconds = round(totalSecondsFromHours + totalSecondsFromMinutes + totalSecondsOnly)

    return (wavFileDurations, convert(totalSeconds))

# Reading a Random Folder
output = readFolder('D:\FL Utils\Downloaded Songs')
