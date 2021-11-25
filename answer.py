import os
import cv2
import json

filepath = 'runs/detect/exp/labels/'
filenames_path='data/test'

filenames=os.listdir(filenames_path)
filenames.sort(key=lambda x:int(x[:-4]))

data = []
for i in range(13068):
    if not os.path.isfile(filepath+filenames[i].replace('.png','.txt')):
        a = {"image_id":int(filenames[i].replace('.png','')),"bbox": [1,1,1,1], "score":0.5, "category_id":10}
        ##a["image_id"].append(filenames[i])
        ##print(a)
        #f = open(filepath+filenames[i]+'.txt','r')
        data.append(a)
    else:
        f = open(filepath+filenames[i].replace('.png','.txt'),'r')
        contents = f.readlines()

        img_name = filenames[i]
        im = cv2.imread('data/svhn/test/'+img_name)
        h, w, c = im.shape
        # print(h,w)
        
        ##a = {"image_id":filenames[i],"bbox": [], "score": [], "category_id": []}
        ##a["image_id"].append(filenames[i])
        for content in contents:
            content = content.replace('\n','')
            ##print(content)
            c = content.split(' ')
            ##print(c)
            ##if(int(c[0])==0):
                ##print(c)
            ##if(int(c[0])==0):
                ##c[0]='10'
            ##a['category_id'].append(int(c[0]))
            w_center = w*float(c[1])
            h_center = h*float(c[2])
            width = w*float(c[3])
            height = h*float(c[4])
            left = float(w_center - width/2)
            right = float(w_center + width/2)
            top = float(h_center - height/2)
            bottom = float(h_center + height/2)
            ##a['bbox'].append(tuple((top, left, bottom, right)))
            ##a['score'].append(float(c[5]))
            
            a = {"image_id":int(filenames[i].replace('.png','')),"bbox":[left, top, width, height], "score":float(c[5]), "category_id":int(c[0])}
        
            data.append(a)
        f.close()
    # print(a)
    ##data.append(a)
    ##f.close()

ret = json.dumps(data)

print(len(data))
with open('answer.json', 'w') as fp:
    fp.write(ret)