from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import json
with open('IsolationSource.json' , 'r') as datafile:
    data=json.load(datafile)


# Extract terms from the data
terms = list(data.values())
ids = list(data.keys())

# Step 1: Data Preprocessing (convert to lowercase)
terms = [term.lower() for term in terms]

# Step 2: Feature Extraction (BoW representation)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(terms)

# Step 3: Clustering (KMeans with 4 clusters)
num_clusters = 10


kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Step 4: Interpretation (group terms by clusters)
clusters = {}
for idx, term in zip(ids, terms):
    cluster_label = kmeans.predict(vectorizer.transform([term]))[0]
    if cluster_label not in clusters:
        clusters[cluster_label] = []
    clusters[cluster_label].append((idx, term))

# Step 5: Print the clusters
# for cluster_label, cluster_terms in clusters.items():
#     print(f"Cluster {cluster_label + 1}:")
#     for idx, term in cluster_terms:
#         print(f"ID: {idx}, Term: {term}")


# CLuster 2: soil
# Cluster 7: _water_
# CLuster 10: Seawater
# CLuster 5: sewage
# Cluster 1 : Miscellaneous (river, lakes included)
# Cluster 9: Sea
# CLuster 4: Wastewater
# Cluster 8: Patient + some strain
# CLuster 3: iron chloride precipitation of 0.2um-filtered seawater, resuspended in oxalate solution]
# Cluster 6: Municipal Sewage
print(clusters)

lookupname={2: 'soil', 7: "_water_", 10: "seawater", 5: 'sewage',
            1: 'miscellaneous', 9: '_sea_', 4: "wastewater", 8: 'patient + some strain',
            3: 'iron chloride ppt', 6: "municipal sewage"}

clusters = {str(lookupname[cluster_label+1]): cluster_terms for cluster_label, cluster_terms in clusters.items()}

clusters_json = json.dumps(clusters, indent=2)
with open('ClusteredCorrect.json' , 'w') as datafile:
    datafile.write(clusters_json)
