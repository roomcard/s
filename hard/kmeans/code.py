import csv

def dist(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i] - p2[i]) ** 2  
    return total ** 0.5 


def mean(cluster):
    mean_x=0.0
    mean_y=0.0
    for i in cluster:
        mean_x+=i[0]
        mean_y+=i[1]
    return [mean_x/len(cluster),mean_y/len(cluster)]


def kmeans(data, centroids, max_iters=100):
    k = len(centroids)

    for iteration in range(max_iters):
      
        clusters = []
        for _ in range(k):
           clusters.append([])



        for point in data:
            nearest_centroid = 0

            min_distance = dist(point, centroids[0])
            
            for i in range(1, len(centroids)):
                current_distance = dist(point, centroids[i])
                if current_distance < min_distance:
                    min_distance = current_distance
                    nearest_centroid = i
            
            print(f"point {point} is assigned to cluster {nearest_centroid} with min_distance {min_distance} ")
            clusters[nearest_centroid].append(point)

        new_centroids = []
        for i in range(k):
            if clusters[i]:
                new_centroids.append(mean(clusters[i]))
            else:
                new_centroids.append(centroids[i])


        print(f"/nIteration {iteration + 1}:")
        for i, cluster in enumerate(clusters):
            print(f"Cluster {i + 1}: {cluster}")
        print(f"Centroids: {new_centroids}")

        if new_centroids == centroids:
            break
        centroids = new_centroids
        
    return clusters, centroids

def read_csv(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            a=[]
            a.append(float(row[1]))
            a.append(float(row[2]))
            data.append(a)
    return data


filename ="C:/Users/nalaw/OneDrive/Desktop/dm/hard/kmeans/code.csv"
data = read_csv(filename)
print(data)

k = int(input("Enter the number of clusters (k): "))
centroids = []
for i in range(k):
    centroids.append(data[i])


clusters, final_centroids = kmeans(data, centroids)

print("/nFinal Clusters:")
for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}: {cluster}")

print("/nFinal Centroids:")
for c in final_centroids:
        print(c)
 
