#!/bin/bash

source .venv/kgc/bin/activate
python -m mapeathor -i ../mappings/outputs-solarchem-mapping.xlsx -l yarrrml -o ../mappings/outputs-solarchem-mapping
python -m mapeathor -i ../mappings/solarchem-mapping.xlsx -l yarrrml -o ../mappings/solarchem-mapping
python -m morph_kgc ../mappings/config.ini
deactivate
