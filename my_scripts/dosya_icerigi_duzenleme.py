import os

direction= os.getcwd()

file_test=open("lettuce_testing.txt","a+",encoding="utf-8")

file_train=open("lettuce_training.txt","a+",encoding="utf-8")

count=1

while (count <= 320):

    file_train.write(r"lettuce_data/lettuce_images/lettuce{}.jpg".format(count)+"\n")

    count += 1

    if count == 321:

        while (count <= 400):

             file_test.write(r"lettuce_data/lettuce_images/lettuce{}.jpg".format(count)+"\n")

             count += 1
