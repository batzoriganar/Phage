'''
Annotation (Parsing, features extraction, taxid extraction and saving it as a json
ONLY those that have isolation source info
'''
from Bio import SeqIO

file_path='D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\data.gbff'

genbank_object= SeqIO.parse(file_path, 'genbank')

a= enumerate(genbank_object)
listtocheck = []
phage_source_dict={}
NOSOURCE=0
SOURCE=0

'''SEQ Objects have: 'annotations', 'count', 'dbxrefs', 'description', 'features', 'format', 'id', 'islower', 'isupper',
 'letter_annotations', 'lower', 'name', 'reverse_complement', 'seq', 'translate', 'upper'''

def source_parcer(depth, file_path):

    global SOURCE,NOSOURCE
    genbank_object = SeqIO.parse(file_path, 'genbank')
    a = enumerate(genbank_object)
    for index, record in zip(range(depth), a):
        r=record[1]
        source = r.features[0]

        if 'isolation_source' in source.qualifiers:
            taxid = source.qualifiers['db_xref'][0]
            tax0 = taxid.split(':')[1]
            isolation_source = source.qualifiers['isolation_source'][0]
            listtocheck.append(([tax0,isolation_source]))
            SOURCE+=1
        else:
            NOSOURCE+=1



print(source_parcer(5000000, file_path))
print(f"source info count: {SOURCE}")
print(f"no source info count: {NOSOURCE}")

print(len(phage_source_dict))

print('+this is the list containging both "appearing" and non appearing ')
print((listtocheck))

import pickle
with open("phagesource", "wb") as fp:   #Pickling
    pickle.dump(listtocheck, fp)

"""
The following script was used to create the processed_phage_data.json
"""
# for i in phage_source_dict:
#     print(f"{i} is isolated from:  {phage_source_dict[i]}")
# print(len(phage_source_dict))
# with open("processed_phage_data.json", "w") as outfile:
#     json_object = json.dumps(phage_source_dict, indent=4)
#     outfile.write(json_object)