from Bio import SeqIO
import os
import json
file_path='D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\data.gbff'

genbank_object= SeqIO.parse(file_path, 'genbank')
# print(genbank_object)
####################################################################################
#Annotation (Parsing, features extraction, taxid extraction and saving it as a json
#ONLY those that have isolation source info                                        #
####################################################################################
a= enumerate(genbank_object)
# print(type(a))
# for x,i in a:
#     print (i)
phage_source_dict={}
def source_parcer(depth, file_path):
    genbank_object = SeqIO.parse(file_path, 'genbank')
    a = enumerate(genbank_object)
    for index, record in zip(range(depth), a):
        # print(index, item)
        # print(dir(record[1]))
        r=record[1]
        # print(r.annotations['source'])
        source = r.features[0]
        if 'isolation_source' in source.qualifiers:
            taxid = source.qualifiers['db_xref'][0]
            tax0 = taxid.split(':')[1]
            isolation_source = source.qualifiers
            phage_source_dict[tax0] = isolation_source
        else:
            # phage_source_dict[r.annotations['source']] = None
            pass

source_parcer(500000, file_path)

for i in phage_source_dict:
    print(f"{i} is isolated from:  {phage_source_dict[i]}")
'''SEQ Objects have: 'annotations', 'count', 'dbxrefs', 'description', 'features', 'format', 'id', 'islower', 'isupper',
 'letter_annotations', 'lower', 'name', 'reverse_complement', 'seq', 'translate', 'upper'''
print(len(phage_source_dict))
# with open("processed_phage_data.json", "w") as outfile:
#     json_object = json.dumps(phage_source_dict, indent=4)
#     outfile.write(json_object)
# def get_cds_feature_with_qualifier_value(seq_record, name, value):
#     """Function to look for CDS feature by annotation value in sequence record.
#
#     e.g. You can use this for finding features by locus tag, gene ID, or protein ID.
#     """
#     # Loop over the features
#     for feature in genome_record.features:
#         if feature.type == "CDS" and value in feature.qualifiers.get(name, []):
#             return feature
#     # Could not find it
#     return None
#
#
# genome_record = SeqIO.read(file_path, "genbank")
# cds_feature = get_cds_feature_with_qualifier_value(genome_record, "old_locus_tag", "ECA0662")
# print(cds_feature)