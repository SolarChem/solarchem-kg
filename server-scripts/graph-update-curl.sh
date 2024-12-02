curl -X 'POST' \
  'https://solarchem.linkeddata.es/repositories/solarchem/rdf-graphs/service?default' \
  -H 'accept: */*' \
  -H 'Content-Type: text/plain' \
  -H 'Authorization: GDB eyJ1c2VybmFtZSI6InNvbGFyY2hlbSIsImF1dGhlbnRpY2F0ZWRBdCI6MTcyNzg3MzIyMjM1MX0=.9FucE8drUU8SW2Aq0m4kbMDew61+4O3emKION6WbrPE=' \
  --data-binary '@/home/solarchem/data/data.nt'
