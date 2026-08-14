from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

names_flower = list(y['class'].unique())
different_flowers = len(names_flower)

print("Total number of different flowers available:", different_flowers)
print("Names of all different flowers:", names_flower)