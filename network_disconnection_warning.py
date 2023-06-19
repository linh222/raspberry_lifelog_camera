import time
from datetime import datetime
import glob
def checking_latest_image(image_folders):
    # Input: The name of the device -> the folder name saving of that device
    #  Output: A text indicating the gap between latest image and current time in every 20 seconds. Warning if the gap is over 2 minutes
    now = datetime.now()
    year=str(now.year)+'0'+str(now.month)
    day='0'+str(now.day)
    while True:
        for folder in image_folders:
            list_image = glob.glob('{}/{}/{}/*.jpg'.format(folder, year, day))
            list_image = [i[-19:-4] for i in list_image]

            list_image = sorted(list_image, reverse=True)
            latest = list_image[0]
            latest = datetime.strptime(latest, '%Y%m%d_%H%M%S')
            latest = latest.timestamp()
            if (int(time.time()) - int(latest))> 120:
                print(now.hour, now.minute, now.second)
                print("[WARNING: data of camera {} is late over {} seconds".format(folder , (int(time.time()) - int(latest))))
        
        time.sleep(30)
        
if __name__=="__main__":
    list_folder = ['folder1']
    checking_latest_image(list_folder)