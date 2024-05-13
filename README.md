<<<<<<< HEAD
# JSON file format --> COLLADA format

---

### Environment:
1. `conda env create -f environment.yml`
2. `conda info --envs` OR `conda env list`
3. `conda activate dataTraining`

### Files:
* `blender_room_generator.py`:
    * Used in Blender, generates a large rectangular prism "room" with smaller cubes (children objects) inside
* `daeToJson.py`:
    * Converts `.dae` files (xml-based) into `.json` format. Combines the resulting file with the generated `.json` descriptor file, and creates a supertype for `generated_data` and `generated_description`
* `jsonConcat.py`:
    * Merges all `.json` files into a single `.jsonl` file, for use as a dataset
* `json2dae.ipynb`:
    * Jupyter notebook for training seq2seq model on dataset

---

_This repo needs cleaning up._
=======
Activate Jupyter Labs with:

1. `conda activate jupyterLabs`
2. jupyter lab


---

This repo needs cleaning up.
>>>>>>> notebooks/master

* 6/5/24: Odd error where there are more files being produced than number of objects (room/cubes). Must investigate.
* Abandoned: ~9/5/24: `sliding_window` branch for implementing a sliding window for long target sequences~
* 11/5/24: Working example of translating `.json` to `.dae`: see `json2dae_v2.ipynb`
    * Requires tweaks to training data to produce a result that can be directly imported into a `.dae` structure
