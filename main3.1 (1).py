#Write a function called linear_Search_product name as input.the function should perform a linear search to find the target product in the list and return a list of indices of all occurrence of the product if found,or an empty list if the product is not found.
def linearsearchproduct(productList,targetproduct):
  indices=[]
  for index, product in enumerate(productList):
    if product==targetproduct:
      indices.append(index)
  return indices
#Example usage:
product=["shoes","boot","loafer","sandel","shoes",]
target="shoes"
target2="apple"
result=linearsearchproduct(product,target2)
print(result)
