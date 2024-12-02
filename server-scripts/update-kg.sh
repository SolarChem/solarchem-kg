#!/bin/bash

# Updates KG, suitable for updates with only new data and no change of structure.
# The KG is uploaded to the named graph `http://w3id.org/solar/i`.

TIME=$( date '+%R:%S' )
echo [$TIME] Updating KG

curl -X 'POST' \
  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?graph=http%3A%2F%2Fw3id.org%2Fi' \
  -H 'accept: */*' \
  -H 'Content-Type: text/plain' \
  -H 'Authorization: GDB eyJ1c2VybmFtZSI6InNvbGFyY2hlbSIsImF1dGhlbnRpY2F0ZWRBdCI6MTcyNzg3MzIyMjM1MX0=.9FucE8drUU8SW2Aq0m4kbMDew61+4O3emKION6WbrPE=' \
  --data-binary '@/home/solarchem/data/kg/solarchem-kg.nt'

TIME=$( date '+%R:%S' )
echo [$TIME] Update completed
