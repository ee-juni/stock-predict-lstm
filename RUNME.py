import os
 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
createFolder('data')
createFolder('data/kospi')
createFolder('data/kospi')
createFolder('performance')

print("Directory creation successful")