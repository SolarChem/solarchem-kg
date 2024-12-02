# Solarchem KG generation and publication

## Contents

Data and scripts needed to produce and update in GraphDB the Solarchem Knowledge Graph.

There are two main repositories:
* `data/`: input and output data of the process
	* `raw/`: data extracted from the original sources
	* `processed/`: data preprocessed for transformation
	* `kg/`: transformed processed data into a knowledge graph
* `scripts/`: contains all the scripts (bash and python) used to extract, transform and load data, each one detailed below
	* `mappings/`: YARRRML mapping files and config file for the transformation of data into the KG
	* `.venv/`: Python virtual environment used for the python scripts, automatically activated and deacivated when used

## Running the scripts
### Update ontologies
To download the latest version of the four ontology modules and upload them to GraphDB.
They are stored in the named graph `w3id.org/solar/o`, which is cleared before the upload. 
Thus, this update is **independent from the updates of the KG**
It is written in bash, only performs `curl` operations.
```
./update-ontologies.sh
```

### Preparing data for transformation
The scripts written in Python use an environment when being run, with the needed packages intstalled. 
It is stored in `~/scripts/.venv/kgc`, and activated automatically when the scripts are run.

#### OpenAlex Dataset
This script downloads the information from OpenAlex of the papers indicated in the file `~/data/raw/paper_references_curated.csv`. 
It produces a unique JSON file with all the information: `~/data/processed/papersOA.json`.
Everytime there are new papers in this file, the script must be run to keep up to date of the papers information. 

```
./OpenAlex_dataset.py
```

#### Cleaning `raw_catalystsdata.csv`
The file `~/data/raw/raw_catalystsdata.csv` needs some preprocessing and cleaning before being transformed into the KG. 
The processed file is generated as `~/data/processed/catalystsdata.csv`.
Everytime there is an update on the file (or the original database table, `catalystsdata`) this script must be run to keep the KG up to date.

```
./cleaning_catalystsdata.py
```


### Managing the KG

#### Constructing the KG
The KG is built using as input the files stored in `~/data/processed/`:
* `catalystsdata.csv`
* `papersOA.json`
* `chemicals.csv`
And generates the output KG in n-triples in: `~/data/kg/solarchem-kg.nt`
It is written in bash, activating the python environment to run morph-kgc, the KG materializer.

```
./kg-construction.sh
```

#### Updating the KG in GraphDB
Updates the triples in the GraphDB, stored in the named graph `http://w3id.org/i`. The script performs a `curl` operation. There are two ways of updating it:

* The first is recommended when new data is added, and when the structure of the KG is not altered.
```
./update-kg.sh
```
* The second is recommended when there have been changes on the ontology that modify the existing triples, so the named graph in which it is stored is cleaned before the new upload. 
```
./clean-update-kg.sh
```
