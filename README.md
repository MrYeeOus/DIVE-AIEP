# ~JSON file format --> COLLADA format~
# DIVE-AIP: Development of Interactive Virtual Environments using AI-Enhanced Photogrammetry
    * Given a single source image, this project will produce a COLLADA scene with interactive objects representing objects within the source image.
    * At present (pre-cleanup), the two important files are:
        * `object_detection.ipynb`: Load an image and it will produce a JSON file, to be loaded into
        * `json2dae_v2.ipynb`: Which will generate a COLLADA fragment for each line in the JSON file. This code fragment will need to be reinserted into a COLLADA file structure (of which the function to do so has not yet been uploaded to this repo).

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
* `json2dae_v2.ipynb`:
    * Jupyter notebook for training seq2seq model on dataset. To be used in comparison with `object_detection.ipynb`
* `object_detection.ipynb`:
    * Contains depth estimation and object detection models, used to generate a JSON file for use in `json2dae_v2.ipynb`

---

_This repo needs cleaning up. Some or all of these steps may not apply to your system._
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
