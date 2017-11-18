import sys
import pickle
import os

from os.path import dirname, realpath
sys.path.append(os.path.join(dirname(realpath(__file__)),".."))

if __name__ == '__main__':
    from modeling.logregression import LogRegModel

    print(os.getcwd())

    dir = sys.argv[1]
    output_modelfile = sys.argv[2]

    model = LogRegModel(dir)

    with open(os.path.join(output_modelfile),"wb") as model_file:
        pickle.dump(model, model_file)