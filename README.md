# solarchem-kg
Knowledge Graph for he [Solarchem Ontology](https://w3id.org/solar/) with photocatalysis experiments.

## Description

This repository contains the resources used to build a knowledge graph containing the information about photocatalysis experiments extracted from scientific articles. The source data is extracted from the [ArtLeafs Database](http://www.artleafs.eu/public/home.php), and enriched with papers from [OpenAlex](https://openalex.org/) and with chemical entities from [ChEBI](https://www.ebi.ac.uk/chebi/) and [Wikidata](https://www.wikidata.org/). The ontology used for constructing the knowledge graph is the [Solarchem Ontology](https://w3id.org/solar/). 

## Structure

This repository is organized as follows:
* `mappings/` contains the RML mappings needed to construct the knowledge graph from the input data sources.
* `notebooks/` conains three notebooks, for (i) cleaning the source data, (ii) construct and enrich the knoweldge graph, and (iii) querying the knowledge graph.
* `server-scripts/` contains the code organized in scripts to execute the cleaning and preparation of data, KG construction and update of ontologies and KG in GraphDB.

## Installation
The code in this repository has been tested in `Python 3.9`

In order to run the code, you need to either install [Jupyter Notebooks](https://jupyter.org/install) to test the notebooks, or execute the scripts in `server-scripts/`.

```
pip install notebook
```

The requirements of the project can be installed as follos. Creating an environment is highly recommended. 

```
pip install -r requirements.txt
```

Finally, start Jupyter notebook and run the notebooks in the `notebooks` folder.