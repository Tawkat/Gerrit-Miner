import time, sys

def show_progress(job_title, index,total):
    length = 50 # modify this to change the length
    progress=index/total
    block = int(round(length*progress))
    msg = "\r{0}  [{1} / {2}]: [{3}] {4}%".format(job_title, index,total, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

# Test
'''for i in range(10):
    time.sleep(0.1)
    show_progress("Some job", i,10)'''