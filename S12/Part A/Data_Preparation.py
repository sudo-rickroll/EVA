import os
import requests 
import zipfile
import shutil as sh

class Prep_Data:

    def __init__(self, url, target):
        self.url = url
        self.target = target

    def download_url(self, chunk_size=128):
        if os.path.exists(self.target):
            return "Zip File already exists"
        r = requests.get(self.url, stream=True)
        with open(self.target, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def unzip_file(self):
        if os.path.exists(self.target.rsplit(".", 1)[0]):
            return "Unzipped file already exists"
        if os.path.exists(self.target):
            with zipfile.ZipFile(self.target, 'r') as zip_ref:
                zip_ref.extractall(self.target.rsplit("/", 1)[0])
            os.remove(self.target)
        else:
            return "Zip File does not exist"

    def split_dataset(self, working_dir, percent_move_to_train):
        os.chdir(working_dir)
        class_count = len([folder for folder in os.listdir('./data/tiny-imagenet-200/train')])
        image_count = len([file for folder in os.listdir('./data/tiny-imagenet-200/train') for file in os.listdir('./data/tiny-imagenet-200/train/{}/images'.format(folder))])
        move_per_class_count = ((percent_move_to_train / 100) * image_count ) // class_count
        if os.path.exists("./data/tiny-imagenet-200/new_train") and os.path.exists("./data/tiny-imagenet-200/new_test") and len([file for folder in os.listdir('./data/tiny-imagenet-200/new_train') for file in os.listdir('./data/tiny-imagenet-200/new_train/{}'.format(folder))]) == ((percent_move_to_train / 100) * image_count):
            return "Dataset has already been split" 
        if not os.path.exists("./data/tiny-imagenet-200/new_train"):
            os.mkdir("./data/tiny-imagenet-200/new_train")
        if not os.path.exists("./data/tiny-imagenet-200/new_test"):
            os.mkdir("./data/tiny-imagenet-200/new_test") 
        for folder in os.listdir('./data/tiny-imagenet-200/train'):
            count = 0
            if not os.path.exists("./data/tiny-imagenet-200/new_train/{}".format(folder)):
                os.mkdir("./data/tiny-imagenet-200/new_train/{}".format(folder))
            if not os.path.exists("./data/tiny-imagenet-200/new_test/{}".format(folder)):
                os.mkdir("./data/tiny-imagenet-200/new_test/{}".format(folder))
            for file in reversed(os.listdir('./data/tiny-imagenet-200/train/{}/images'.format(folder))):
                if count < move_per_class_count:
                    sh.copy("./data/tiny-imagenet-200/train/{0}/images/{1}".format(folder, file), "./data/tiny-imagenet-200/new_train/{0}/{1}".format(folder, file))
                    count += 1
                else:
                    sh.copy("./data/tiny-imagenet-200/train/{0}/images/{1}".format(folder, file), "./data/tiny-imagenet-200/new_test/{0}/{1}".format(folder, file))    
        class_dict={}
        f = open('./data/tiny-imagenet-200/val/val_annotations.txt','r')
        for line in f:
            class_dict.setdefault(line.split('\t')[0], line.split('\t')[1])
        f.close()
        for file in os.listdir("./data/tiny-imagenet-200/val/images"):
            if not os.path.exists("./data/tiny-imagenet-200/new_test/{}".format(class_dict[file])):
                os.mkdir("./data/tiny-imagenet-200/new_test/{}".format(class_dict[file]))
            sh.copy("./data/tiny-imagenet-200/val/images/{}".format(file), "./data/tiny-imagenet-200/new_test/{0}/{1}".format(class_dict[file], file))

    def class_id_txt(self, txt_path):
        class_dict = {}
        file = open(txt_path, 'r')
        for line in file:
            if "," in line.split("\t")[1]:
                class_dict.setdefault(line.split("\t")[0], line.split("\t")[1].split(",")[0])
            else:
                class_dict.setdefault(line.split("\t")[0], line.split("\t")[1].rstrip('\n'))
        return class_dict