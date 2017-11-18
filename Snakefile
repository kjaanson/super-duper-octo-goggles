rule all_models:
    input:
        "api/model_pickles/logreg.pickle",
        "api/model_pickles/randforest.pickle"

rule build_model:
    input:
        "data/geoplaces2.csv",
        "data/chefmozparking.csv",
        "data/rating_final.csv",
        script="scripts/{modelname}.py"
    params:
        datadir="data/"
    output:
        picklefile="api/model_pickles/{modelname}.pickle"
    shell:
        "python {input.script} {params.datadir} {output.picklefile}"