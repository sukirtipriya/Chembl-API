
# Chembl API

################################################################################################

# Find a compound by pref_name using the molecule endpoint

import pandas as pd

from chembl_webresource_client.new_client import new_client #Import ChEMBL python client

input_list = "aspirin"

Export_df = pd.DataFrame()

for i in input_list:
	molecule = new_client.molecule
	mols = molecule.filter(pref_name__iexact= i )
	res = pd.DataFrame(mols)
	Export_df = pd.concat([Export_df, res])

Export_df


################################################################################################

# Find a compound by its synonyms

import pandas as pd

from chembl_webresource_client.new_client import new_client

input_list = "viagra"

Export_df = pd.DataFrame()

for i in input_list:
	molecule = new_client.molecule
	mols = molecule.filter(molecule_synonyms__molecule_synonym__iexact='viagra')
		.only('molecule_chembl_id')
	res = pd.DataFrame(mols)
	Export_df = pd.concat([Export_df, res])

Export_df

##############################################################################################

# Get many compounds using a list of their identifiers (ChEMBL_id)

from chembl_webresource_client.new_client import new_client

import pandas as pd

molecule = new_client.molecule
mols = molecule.filter(molecule_chembl_id__in=['CHEMBL25', 'CHEMBL192','CHEMBL27'])
	.only(['molecule_chembl_id', 'pref_name'])
mols

################################################################################################

# Find compounds with the same connectivity

from chembl_webresource_client.new_client import new_client

import pandas as pd 

molecule = new_client.molecule
res = molecule.filter(molecule_structures__canonical_smiles__connectivity='CN(C)C(=N)N=C(N)N')
	.only(['molecule_chembl_id', 'pref_name'])

pd.DataFrame(res)

##############################################################################################

# target chembl id to mechanism of action

from chembl_webresource_client.new_client import new_client
import pandas as pd

mechanism = new_client.mechanism
res = mechanism.filter(target_chembl_id='CHEMBL1980')
	.only(['mechanism_of_action','molecule_chembl_id', 'target_chembl_id'])
res = pd.DataFrame(res)
res


###############################################################################################

# Find a target by gene name

from chembl_webresource_client.new_client import new_client

target = new_client.target
gene_name = 'BRD4'

res = target.filter(target_synonym__icontains=gene_name)
	.only(['organism', 'pref_name', 'target_type'])
for i in res:
    print(i)
    

##############################################################################################

# Find a protein target using its Uniprot_id

from chembl_webresource_client.new_client import new_client

target = new_client.target
uniprot_id = 'P35916' #Vascular endothelial growth factor receptor 3; Uniprot accession P35916
res = target.filter(target_components__accession=uniprot_id)

res = pd.DataFrame(res)
res

#############################################################################################




















