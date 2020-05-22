import os
import time
import random
import sys 

# For random string generation
# UUID ( Universally Unique IDentifier)
import uuid

# For converting urandom random binaries to
# human readable strings.
from base64 import b64encode

MAX_DEPTH = 12

def get_contentsize():
    
    content_size = round(random.normalvariate(1024,768))
    return max([content_size,16])



def bernoulli(probability):

    return random.random() <= probability



def create_directory(path,depth,directory_probability = 0.6,file_probability = 0.75,max_depth=MAX_DEPTH) -> None:

    while(bernoulli(directory_probability)):
        dir_basename = get_filename()
        os.mkdir(os.path.join(path,dir_basename))
        create_directory(os.path.join(path,dir_basename),depth+1)

    while(bernoulli(file_probability)):
        with open(os.path.join(path,get_filename()),"w") as fp:
            random_bytes = os.urandom(get_contentsize())
            fp.write(b64encode(random_bytes).decode("utf-8"))




def get_filename() -> str:

    return uuid.uuid1().hex[0:6]


if __name__ == "__main__":
    
    # Fully randomize the generation process.
    random.seed(time.time())

    entry_basename = get_filename()
    os.mkdir(os.path.join(os.getcwd(),entry_basename))
    create_directory(os.path.join(os.getcwd(),entry_basename),1)
    


    