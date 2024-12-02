#!/bin/bash

# Download the last version of the four ontology modules and upload it into GraphDB, after cleaning the named graph 'http://w3id.org/o', where they are stored.

TIME=$( date '+%R:%S' )
echo [$TIME] Deleting ontology named graph

curl -X 'DELETE' \
  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?graph=http%3A%2F%2Fw3id.org%2Fo' \
  -H 'accept: */*' \
  -H 'Authorization: GDB eyJ1c2VybmFtZSI6InNvbGFyY2hlbSIsImF1dGhlbnRpY2F0ZWRBdCI6MTcyNzg3MzIyMjM1MX0=.9FucE8drUU8SW2Aq0m4kbMDew61+4O3emKION6WbrPE='

for MODULE in core ec pc pec
do
	TIME=$( date '+%R:%S' )
	echo [$TIME] Processing module $MODULE
	curl -sH 'Accept: application/rdf+xml' -L https://w3id.org/solar/o/$MODULE/ > /home/solarchem/solarchem-kg/data/ontologies/$MODULE.owl

	curl -X 'POST' \
	  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?graph=http%3A%2F%2Fw3id.org%2Fo' \
	  -H 'accept: */*' \
	  -H 'Content-Type: application/rdf+xml' \
	  -H 'Authorization: GDB eyJ1c2VybmFtZSI6InNvbGFyY2hlbSIsImF1dGhlbnRpY2F0ZWRBdCI6MTcyNzg3MzIyMjM1MX0=.9FucE8drUU8SW2Aq0m4kbMDew61+4O3emKION6WbrPE=' \
	  --data-binary '@/home/solarchem/solarchem-kg/data/ontologies/'$MODULE'.owl'
done
