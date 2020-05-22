import os
import time
import random
import sys 

# For converting urandom random binaries to
# human readable strings.
from base64 import b64encode

import faker


MAX_DEPTH = 8
FAKER = faker.Faker()

get_filename = lambda : FAKER.first_name_male()
get_dirname = lambda : FAKER.first_name_female()

def get_contentsize():
    
    content_size = round(random.normalvariate(1024,768))
    return max([content_size,16])



def bernoulli(probability):

    return random.random() <= probability



def create_directory(path,depth,directory_probability = 0.6,file_probability = 0.75,max_depth=MAX_DEPTH) -> None:

    if depth == MAX_DEPTH:
        return

    while(bernoulli(directory_probability)):
        dir_basename = get_dirname()
        os.mkdir(os.path.join(path,dir_basename))
        create_directory(os.path.join(path,dir_basename),depth+1)

    i = 0

    while(bernoulli(file_probability)):
        i += 1
        file_path = os.path.join(path,get_filename())
        try:
            
            with open(file_path,"w") as fp:
                random_bytes = os.urandom(get_contentsize())
                fp.write(b64encode(random_bytes).decode("utf-8"))
        
        except FileExistsError:
            file_path += str(i)
            with open(file_path,"w") as fp:
                random_bytes = os.urandom(get_contentsize())
                fp.write(b64encode(random_bytes).decode("utf-8"))



if __name__ == "__main__":
    
    # Fully randomize the generation process.
    random.seed(time.time())

    entry_basename = get_filename()

    root_path = os.path.join(os.getcwd(),entry_basename)
    os.mkdir(root_path)
    create_directory(root_path,1)

    


    