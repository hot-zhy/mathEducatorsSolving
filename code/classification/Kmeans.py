import json
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from umap import UMAP
import re

# data_path = '../../dataset/AAAI/TAL-SAQ6K-EN.jsonl'
data_path = '../../dataset/data/college_mathematics_test.jsonl'

# 1. data preparing
with open(data_path, 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]

texts = [item['problem']
         for item in data]

# 2. extract characteristics
# Adjusting the min_df and max_df parameters
vectorizer = TfidfVectorizer(max_features=1024, min_df=0.01, max_df=0.7)
X = vectorizer.fit_transform(texts)

# 3. apply K-Means with increased n_init for more stable centroids
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, n_init=50)  # Increase n_init to 20
kmeans.fit(X)
labels = kmeans.labels_

# 4. save results to different jsonl file
clustered_data = [[] for _ in range(num_clusters)]
for text, label in zip(data, labels):
    clustered_data[label].append(text)

for i, cluster in enumerate(clustered_data):
    with open(f'../classification/MMLU-Math/college/college_{i}.jsonl', 'w', encoding='utf-8') as file:
        for item in cluster:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')

# 5. 使用UMAP进行降维，并绘制聚类结果
umap = UMAP(n_neighbors=8, min_dist=0.001, n_components=2, random_state=42)
reduced_X = umap.fit_transform(X.toarray())

plt.figure(figsize=(10, 8))
for i in range(num_clusters):
    points = reduced_X[labels == i]
    plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {i}')

plt.title('K-Means Clustering of Math Questions with UMAP')
plt.xlabel('UMAP Feature 1')
plt.ylabel('UMAP Feature 2')
plt.legend()
plt.show()
