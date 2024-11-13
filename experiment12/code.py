import csv
import math

with open('C:/Users/nalaw/OneDrive/Desktop/dm/experiment12/output.txt', 'w') as output_file:
    def read_csv(file_path):

        with open(file_path,'r') as file:
            reader =csv.DictReader(file)
            data =[]
            for row in reader:
                data.append(row)
        return data
    
    def calculate_prior_probabiity(data,target_attribute):
        unique_count ={}

        for row in data:
            if row[target_attribute] in unique_count:
                unique_count[row[target_attribute]]+=1
            else:
                unique_count[row[target_attribute]]=1
        prior ={}
        for key,count in unique_count.items():
            probability=count/len(data)
            output_file.write(f"probability for {key} is {probability}\n")
            prior[key]=probability
        return prior
    
    def calculate_likelihood(data,features,target_attribute,prior):
        likelihood={}

        labels =set()

        for row in data:
          labels.add(row[target_attribute])

        for label in labels:
             likelihood[label]={}
             subset =[]

             for row in data:
                 if row[target_attribute]==label:
                     subset.append(row)
             
             for feature in features:
                 likelihood[label][feature]={}

                 unique_values= set()
                 for row in subset:
                     unique_values.add(row[feature])
                
                 for value in unique_values:
                     count=0
                     for row in subset:
                         if row[feature]==value:
                             count+=1
                     likelihood[label][feature][value]=(count/len(subset))
        return likelihood

    def calculate_bayesian(data,features,target_attribute,new_instance):
        prior =calculate_prior_probabiity(data,target_attribute)
        likelihood= calculate_likelihood(data,features,target_attribute,prior)
        posteriors ={}

        for labels in prior.keys():
            posteriors[labels]=prior[labels]
            output_file.write(f"calculating the likelihood for {labels}\n")

            for feature in features:
                if new_instance[feature] in likelihood[labels][feature]:
                    posteriors[labels]*=likelihood[labels][feature][new_instance[feature]]
                    output_file.write(f"likelyhood probability for P({new_instance[feature]}/{labels}) is  {likelihood[labels][feature][new_instance[feature]]}\n")
                else:
                    posteriors[labels]=0
        
        return posteriors
    

    file_path='C:/Users/nalaw/OneDrive/Desktop/dm/experiment12/code.csv'
    data =read_csv(file_path)
    target_attribute='play'
    features = data[0].keys()-{target_attribute}
    new_instance={}

    for feature in features:
        feature_value =input(f"enter the value for {feature}  ")
        new_instance[feature]=feature_value
    
    posteriors = calculate_bayesian(data,features,target_attribute,new_instance)
    min_value =float('-inf')
    value=''
    for label,probability in posteriors.items():
        if probability>min_value:
            value=label
    output_file.write(f"class label for {new_instance} is {value}")
    


        
    




    

