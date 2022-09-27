#import reqired Libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import glob

#user input path
path = input("Enter the path of your file: ")
     
#assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
print("Hooray we found your csv!")

all_files = glob.glob(path+'/*.csv')

#/home/user/Documents/Train-jerk-detection/Code
#print(all_files)

print('Combining all files')

final = pd.concat(map(pd.read_csv, all_files))

print('Frequency of data reading :')

#Extract time frm datetime and Divide time in hour , minute , second ,microsecond

final['jerkCurrentTimeInUTC'] = pd.to_datetime(final['jerkCurrentTimeInUTC'], errors='coerce')
final[['h','m','s','ms']] = pd.DataFrame([(x.hour, x.minute, x.second,x.microsecond) for x in final['jerkCurrentTimeInUTC']])
final['m:s.ms'] = list(zip(final['m'],final['s'],final['ms']))

#Frequency every microsecond
f = final['m:s.ms'].value_counts()
print(f.mean())
print(f)


#Extract first and last value of csv 
last = []
first = []
for files in all_files:
    df = pd.read_csv(files)
    df.iloc[:,4] = pd.to_datetime(df.iloc[:,4], errors='coerce')
    #First reading in time
    first.append(df.iloc[0,4])
    #last time reading
    last.append(df.iloc[-1,4])

#Time diff in last value of first csv and first value of second csv
diff = first[1]-last[0]
print('Time differnce {}'.format(diff))

df2 = pd.DataFrame(columns=['First time value','Last time value'])
#append lists to df2
df2['First time value'] = first
df2['Last time value'] = last

#Max value of first csv
mx = max(final.iloc[:,4])
#print(mx)
mn = min(final.iloc[:,4])
#print(mn)
avg = (mx-mn)/(len(final.iloc[:,4])-1)
print('Average time differnce {}'.format(avg))

if diff > avg :
    print('time diffence unatural')







