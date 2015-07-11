import datetime
import boto3
#from boto3.session import Session
from datetime import datetime

timeNowStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
timeNow = datetime.strptime(timeNowStr, "%Y-%m-%d %H:%M:%S")

#session = Session(aws_access_key_id='AKIAJRXQMFUU2XEMVP3Q',
#  aws_secret_access_key='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',
#  region_name='us-west-1')

AWSRegion = open("aws_region.txt", 'r')
awsRegionList = AWSRegion.readlines()
AWSRegion.close()

#ec2 = session.resource('ec2')
#ec2 = boto3.resource('ec2')

print("AWS Region List:")
for thisRegion in awsRegionList:
    print("======================================")
    thisCount = 0
    thisRegion = thisRegion.strip()
    print(thisRegion)
    this_ec2_region = boto3.resource('ec2', region_name=thisRegion)
    #this_ec2_region = ec2.resource('ec2', region_name=thisRegion)
    for instance in this_ec2_region.instances.all():
        thisLaunchTimeStr =instance.launch_time.strftime("%Y-%m-%d %H:%M:%S")
        thisLaunchTime = datetime.strptime(thisLaunchTimeStr, "%Y-%m-%d %H:%M:%S")
        timeDiff = timeNow - thisLaunchTime
        print(str(instance.id) + " is " + instance.state['Name'] + " for " +  str(timeDiff.days) + " days")
        thisCount = thisCount + 1
        print(" ")
    if thisCount > 0:
        print("Total Count: " + str(thisCount))
