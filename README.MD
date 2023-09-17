Data retrieved from https://afproject.org/phdaily/
2023/07/21 13.24


The data.json file contains 15011 phage info
in the structure:

>dict_keys(['name', 'synonymes', 'species_taxid', 'genome_composition', 'taxonomy_ncbi', 'taxonomy_ictv', 'assemblies', 'hosts'])

The 'host' key contains the the list of hosts that can be infected by the phage. 

phages_with_multiple_hosts=560\
number of unique hosts=1049

\
data. gbff file contains
annotation of the phages. 

11028 source info out of 15011 were provided
It is stored in the 'phagesource'.pkl file

===

Network_isolation.py 
can be run to visualize the interaction network and save the data into a csv file.
For that one should use the functions subsetplot() and save_dftocsv()
