#!/bin/bash

# Download the last version of the four ontology modules and upload it into GraphDB, after cleaning the named graph 'https://w3id.org/solar/o/', where they are stored.

KEY=$(<access.txt)

TIME=$( date '+%R:%S' )
echo [$TIME] Deleting ontology named graph

curl -X 'DELETE' \
  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?graph=https%3A%2F%2Fw3id.org%2Fsolar%2Fo%2F' \
  -H 'accept: */*' \
  -H 'Authorization: GDB '$KEY

for MODULE in core ec pc pec
do
	TIME=$( date '+%R:%S' )
	echo [$TIME] Processing module $MODULE
	curl -sH 'Accept: application/rdf+xml' -L https://w3id.org/solar/o/$MODULE/ > ../data/ontologies/$MODULE.owl

	curl -X 'POST' \
	  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?graph=https%3A%2F%2Fw3id.org%2Fsolar%2Fo%2F' \
	  -H 'accept: */*' \
	  -H 'Content-Type: application/rdf+xml' \
  	  -H 'Authorization: GDB '$KEY \
	  --data-binary '@../data/ontologies/'$MODULE'.owl'
done
