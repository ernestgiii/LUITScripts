# Listing AWS services

# My list will initally be empty
myawsservices_list= []

# Populating list using append
myawsservices_list.append('S3')
myawsservices_list.append('EC2')
myawsservices_list.append('DynamoDB')
myawsservices_list.append('Lambda')
myawsservices_list.append('Cloud9')

# Print the list and length of the list
print(myawsservices_list)
print(len(myawsservices_list))

# Remove two specific services from the list 
del myawsservices_list[1]
del myawsservices_list[3]

# Print the new list and its new length

print(myawsservices_list)
print(len(myawsservices_list))
