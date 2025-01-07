#!/bin/bash

# Updates KG, suitable for updates that involve change of structure.
# The KG is uploaded to the named graph `https://w3id.org/solar/i/`, after being cleaned up.

KEY=$(<access.txt)

TIME=$( date '+%R:%S' )
echo [$TIME] Cleaning named graph and updating KG

curl -X 'PUT' \
  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?graph=https%3A%2F%2Fw3id.org%2Fsolar%2Fi%2F' \
  -H 'accept: */*' \
  -H 'Content-Type: text/plain' \
  -H 'Authorization: Basic '$KEY \
  --data-binary '@../data/kg/solarchem-kg.nt'

TIME=$( date '+%R:%S' )
echo [$TIME] Update completed
