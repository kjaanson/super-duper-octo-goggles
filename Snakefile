

rule all_models:
    input:
        "api/model_pickles/logregression.pickle"

rule build_model:
    input:
        "data/geoplaces2.csv",
        "data/chefmozparking.csv",
        "data/rating_final.csv",
        datadir="data/",
        script="models/{modelname}.py"
    output:
        picklefile="api/model_pickles/{modelname}.pickle"
    shell:
        "python {input.script} {input.datadir} {output.picklefile}"