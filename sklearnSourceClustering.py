from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import json
with open('IsolationSource.json' , 'r') as datafile:
    data=json.load(datafile)

print(data)
# Extract terms from the data
terms = list(data.values())
ids = list(data.keys())
print(terms,ids)
#Data Preprocessing (convert to lowercase)
terms = [term.lower() for term in terms]

# Step 2: Feature Extraction (BoW representation)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(terms)

#Clustering (KMeans with n clusters)
num_clusters = 10


kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Interpretation (group terms by clusters)
clusters = {}
for idx, term in zip(ids, terms):
    cluster_label = kmeans.predict(vectorizer.transform([term]))[0]
    if cluster_label not in clusters:
        clusters[cluster_label] = []
    clusters[cluster_label].append((idx, term))


lookupname={2: 'soil', 7: "_water_", 10: "seawater", 5: 'sewage',
            1: 'miscellaneous', 9: '_sea_', 4: "wastewater", 8: 'patient + some strain',
            3: 'iron chloride ppt', 6: "municipal sewage"}

clusters = {str(lookupname[cluster_label+1]): cluster_terms for cluster_label, cluster_terms in clusters.items()}

clusters_json = json.dumps(clusters, indent=2)
# with open('Clusteredbysources_sk.json' , 'w') as datafile:
#     datafile.write(clusters_json)
