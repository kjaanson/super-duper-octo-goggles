

rule all_models:
    input:
        "api/model_pickles/logregression.pickle"

rule build_model:
    input:
        "data/geoplaces2.csv",
        "data/chefmozparking.csv",
        "data/rating_final.csv",
    params:
        module="modeling.{modelname}",
        datadir="data/"
    output:
        picklefile="api/model_pickles/{modelname}.pickle"
    shell:
        "python -m {params.module} {params.datadir} {output.picklefile}"