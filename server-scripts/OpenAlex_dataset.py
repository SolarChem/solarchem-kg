#!/home/solarchem/scripts/.venv/kgc/bin/python

import pandas as pd
from datetime import datetime
import os.path
import requests
import json

def generating_OA_file():
	"""
		Downloads and merges the JSON files from OpenAlex corresponding to the papers in the file paper_references_curated.csv.
	"""

	print('['+str(datetime.now().time())[0:8]+'] Obtaining papers information from OpenAlex')

	## opening curated file of papers
	papers_df = pd.read_csv("/home/solarchem/data/raw/paper_references_curated.csv", sep=';')

	headers = {'Accept': 'application/json'}
	query ='https://api.openalex.org/works/https://doi.org/{}'
	path = '/home/solarchem/data/raw/jsonOA/'

	print('['+str(datetime.now().time())[0:8]+'] Downloading JSON file for each paper')

	# download papers from OpenAlex with the DOIs in the papers file
	for index, row in papers_df.iterrows():
		response = requests.get(query.format(row['DOI']), headers=headers)
		print(index)
	    
		if response.status_code == 200:
			res_json = response.json()
			res_json['solar_id'] = row['No_de_Ref']
			with open(path+str(row['No_de_Ref'])+'.json', 'w') as file:
				file.write(json.dumps(res_json, indent=4))
		else:
			print(f"Error with {row['DOI']}, id {str(row['No_de_Ref'])}")
	
	print('['+str(datetime.now().time())[0:8]+'] Merging obtained files')

	# merging individual JSONs into one JSON file
	json_file_names = os.listdir(path)
	merged_json = []
	for file in json_file_names:
		filename = path + file
		with open(filename, 'r') as infile:
			merged_json.append(json.load(infile))
	
	print('['+str(datetime.now().time())[0:8]+'] Saving file in ~/data/processed/papersOA.json')
	
	# save file 
	with open('/home/solarchem/data/processed/papersOA.json', 'w') as out_json:
	    json.dump(merged_json, out_json)

def main():
	
	generating_OA_file()


if __name__ == '__main__':
    main()

