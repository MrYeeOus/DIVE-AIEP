# DIVE-AIP: Development of Interactive Virtual Environments using AI-Enhanced Photogrammetry
* The DIVE-AIP pipline explores a novel method of quickly creating virtual environments that simulates real-world scenarios from a single image. In this process, we are able to create a 3D scene that not only matches the scale of the source scene, but also produces independent placeholder assets that represent objects in the source scene. The DIVE-AIP pipeline aims to fast-track the development of virtual environments by reducing the time spent in developing 3D assets.

---
## Update June 2024:
Thesis completed. Research paper can be viewed [here](./BenjaminYee_45425108_ThesisB.pdf).

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

_This repo needs cleaning up - there are currently a lot of fluff files and vague naming conventions. Some or all of these steps may not apply to your system._
=======
Activate Jupyter Labs with:

1. `conda activate jupyterLabs`
2. jupyter lab


---
