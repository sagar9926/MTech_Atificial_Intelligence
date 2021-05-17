
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
from numpy import linalg as LA
from sklearn.metrics import accuracy_score


class KmeansClustering :

  def __init__(self,n_clusters):
    self.n_clusters = n_clusters
    self.cluster_centers = None

  def distance(self,mean_array,feature_array):
    # subtracting vector
    temp = (mean_array - feature_array)

    # Calculate euclidean distance between arrays
    euclid_dist = np.sqrt(np.dot(temp.T,temp))

    return euclid_dist

  def fit(self,features):

    # Initialize mean centers with random points 
    idx = np.random.randint(len(features), size=self.n_clusters)
    #idx = [0,1]
    old_mean = None
    new_mean = features[idx]
    comparison = new_mean == old_mean
    while ~(comparison.all()):
      closest_cluster = []
      for f in features:
        keys = [i + 1 for i in range(self.n_clusters)]
        dist = dict.fromkeys(keys)
        for index , mu in enumerate(new_mean) :
          dist[index + 1] = self.distance(mu,f)
        closest_cluster.append(sorted(dist.items(),key = lambda x : x[1])[0][0])
      old_mean = new_mean
      new_mean = pd.DataFrame(features).groupby(closest_cluster).mean().values
      comparison = new_mean == old_mean
    self.cluster_centers = new_mean

  def predict(self,features):
    predicted_cluster = []
    for f in features:
      keys = [i + 1 for i in range(self.n_clusters)]
      dist = dict.fromkeys(keys)
      for index , mu in enumerate(self.cluster_centers) :
        dist[index + 1] = self.distance(mu,f)
      predicted_cluster.append(sorted(dist.items(),key = lambda x : x[1])[0][0])
    return predicted_cluster

class SpectralClustering : 
  def __init__(self, n_clusters):
    self.n_clusters = n_clusters
    self.weight_matrix = np.zeros((len(features),len(features)))
    self.degree_matrix = np.zeros((len(features),len(features)))
    self.lalpacian_matrix = np.zeros((len(features),len(features)))
    self.H = None

  def similarity(self,vector_1,vector_2,variance = 1):
    
    # subtracting vector
    temp = (vector_1 - vector_2)

    # Calculate euclidean distance between arrays
    euclid_dist = np.dot(temp.T,temp)

    similarity = np.exp(-1*euclid_dist/variance)

    return similarity

  def fit_predict(self,features) : 

    #   Calculate the adjacency matrix
    for row , node1 in enumerate(features):
      for column , node2 in enumerate(features):
        self.weight_matrix[row][column] = self.similarity(node1,node2)

    # Calculate the degree matrix 
    for row,vector in enumerate(self.weight_matrix):
      self.degree_matrix[row][row] =  sum(vector)

    # Perform eigen value decomposition of graph laplacian matrix
    self.lalpacian_matrix = self.degree_matrix - self.weight_matrix
    w, v = LA.eig(self.lalpacian_matrix)

    # Calculate Cluster assignment matrix, which is simply the eigen vectors corresponding to n_clusters eigen values
    idx = np.argpartition(w, self.n_clusters)
    H = v[:,idx[:self.n_clusters]]

    # Predict clusters using K means
    km = KmeansClustering(self.n_clusters)
    km.fit(H)
    predicted_clusters = km.predict(H)

    return predicted_clusters

if __name__ == "__main__":
    
    # KMeans Prediction
    
    np.random.seed(42)
    data = pd.read_csv("http://cs.joensuu.fi/sipu/datasets/jain.txt",delimiter = '\t',names=["feature_1" ,"feature_2","cluster"])
    features = data[['feature_1','feature_2']].values
    y_true = data[['cluster']].values
    
    data_km_plot = data.copy()
    
    # Kmeans Model Fitting
    km = KmeansClustering(2)
    km.fit(features)
    
    # Kmeans Prediction
    km_prediction = km.predict(features)
    km_prediction = [1 if pred == 2 else 2 for pred in km_prediction]

    # PLot K means Result
    data_km_plot['cluster'] = km_prediction
    cluster_1 = plt.scatter(data_km_plot[data_km_plot['cluster'] == 1].iloc[:,0], data_km_plot[data_km_plot['cluster'] == 1].iloc[:,1], alpha=0.3)
    cluster_2 = plt.scatter(data_km_plot[data_km_plot['cluster'] == 2].iloc[:,0], data_km_plot[data_km_plot['cluster'] == 2].iloc[:,1], alpha=0.3)
    plt.legend((cluster_1, cluster_2),
           ('Cluster 1', 'Cluster 2'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)
    km_accuracy = "K-Means Clustering : Accuracy = " + str(round(accuracy_score(y_true, km_prediction)*100,2))+"%"
    plt.title(km_accuracy)
    plt.xlabel("feature_1")
    plt.ylabel("feature_2")
    #sns.scatterplot(x = "feature_1",y = "feature_2",data = data,hue = 'cluster')
    #plt.plot([mean[0][0] ,mean[1][0]] , [mean[0][1] ,mean[1][1]],"*",markersize=12)
    plt.show()
    
    print("Kmeans Clustering Accuracy Score : ",round(accuracy_score(y_true, km_prediction)*100,2),"%")
    
    #Spectral Clustering
    
    data_SC_plot = data.copy()
    sc_prediction = SpectralClustering(n_clusters=2).fit_predict(features)

    data_SC_plot['cluster'] = sc_prediction
 
    cluster_1 = plt.scatter(data_SC_plot[data_SC_plot['cluster'] == 1].iloc[:,0], data_SC_plot[data_SC_plot['cluster'] == 1].iloc[:,1], alpha=0.3)
    cluster_2 = plt.scatter(data_SC_plot[data_SC_plot['cluster'] == 2].iloc[:,0], data_SC_plot[data_SC_plot['cluster'] == 2].iloc[:,1], alpha=0.3)
    plt.legend((cluster_1, cluster_2),
           ('Cluster 1', 'Cluster 2'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)
    sc_accuracy = "Spectral Clustering : Accuracy = " + str(round(accuracy_score(y_true, sc_prediction)*100,2))+"%"
    plt.title(sc_accuracy)
    plt.xlabel("feature_1")
    plt.ylabel("feature_2")
    plt.show()
    print("Spectral Clustering Accuracy Score : ",round(accuracy_score(y_true, sc_prediction)*100,2),"%")
    
