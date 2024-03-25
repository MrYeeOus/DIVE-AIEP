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
* 
