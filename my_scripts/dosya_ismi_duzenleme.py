import os

os.chdir("D:\DeepLearningProjects\LettuceDetection\lettuce_images")

count=1

while (count<=400):

    os.rename("lettuce ("+str(count)+").jpg","lettuce"+str(count)+".jpg")

    count+=1

    