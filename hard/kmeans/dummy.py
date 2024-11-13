import csv
import math

with open("C:/Users/nalaw/OneDrive/Desktop/dm/hard/kmeans/output.txt",'w') as op:
  def read_csv(file_path):
    with open(file_path,'r') as file:
        reader =csv.reader(file)
        next(reader)
        data=[]
        for row in reader:
           a =[]
           a.append(float(row[1]))
           a.append(float(row[2]))
           data.append(a)
    return data
  
  def calculate_distance(p1,p2):
    dist =0.0

    for i in range(len(p1)):
         dist+=(p2[i]-p1[i])**2
    return math.sqrt(dist)
  
  def calculate_mean(cluster):
     mean_x=0
     mean_y=0
     for i in range(len(cluster)):
        mean_x+=cluster[i][0]
        mean_y+=cluster[i][1]
     return [mean_x/len(cluster),mean_y/len(cluster)]
  

        
        
  def apply_kmeans(k,data,centroids):
     count =1
     while True:
        
        op.write(f"Centroids for this iteration {count} is {centroids}\n")

        clusters =[]
        for i in range(k):
           clusters.append([])
          
        
        for point in data :
            min_dist =calculate_distance(point,centroids[0])
            nearest_centroid =0
            for i in range(len(centroids)):
               distance =calculate_distance(point,centroids[i])
               if distance<min_dist:
                  min_dist=distance
                  nearest_centroid =i
            clusters[nearest_centroid].append(point)
            op.write(f" {point}  is nearest to the centroid {centroids[nearest_centroid]} with distance is {min_dist}\n")

        new_centroids=[]
        for i,cluster in enumerate(clusters):
           if cluster:
             new_centroids.append(calculate_mean(cluster))
           else:
             new_centroids.append(centroids[i])
            

        if new_centroids==centroids:
           op.write(f"final centroid are {new_centroids}\n")
           op.write(f"final cluster {clusters} \n")
           break
        centroids=new_centroids
        
                      

  file_path="C:/Users/nalaw/OneDrive/Desktop/dm/hard/kmeans/code.csv"
  data =read_csv(file_path)
  k= int(input("Enter the no of clusters "))

  centroids =[]
  for i in range(0,k):
     centroids.append(data[i])
  apply_kmeans(k,data,centroids)


  