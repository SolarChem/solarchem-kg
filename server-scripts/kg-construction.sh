#!/bin/bash

source .venv/kgc/bin/activate
python -m morph_kgc mappings/config.ini
deactivate
