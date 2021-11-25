# 2021-VRDL-HW2

This repository is the official implementation of [2021 VRDL HW1](https://competitions.codalab.org/competitions/35668?secret_key=09789b13-35ec-4928-ac0f-6c86631dda07). 


## Reproducing Submission
1. [Requirements](#Requirements)
2. [Pretrained_Model](#Pretrained_Model)(After downloading, put it into 'model_to_inference' folder.)
3. [Dataset](#Dataset)(Download the testing_images,unzip it and put it into 'dataset' folder)
4. [Inference](#Inference)

### Environment
-Anoconda



## Requirements

To install requirements:

```setup
#run the Anaconda Prompt
conda create -n hw2 python=3.7 -y
conda activate hw2
conda install pytorch torchvision cudatoolkit -c pytorch -y

git clone https://github.com/wl02227976/2021-VRDL-HW2
cd 2021-VRDL-HW2

pip install -r requirements.txt
```


##Data
Download the dataset(test.zip and train.zip) from [data](https://drive.google.com/drive/folders/1rcPvAKc6IzfcppW4ShS8HRmYsaB6llvk?usp=sharing)
put them into the data folder and unzip them

```data
python data_preprocess.py
```

create the folder named "valid" in "data" folder
put 30001.png-33402.png(in "/data/train/") and 30001.txt-33402.txt(in "/data/train/") into "valid"folder




