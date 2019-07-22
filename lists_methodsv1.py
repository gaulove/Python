names =["Gaurav","Sagar","Neupane","Govinda"]
nums =[2, 4, 6, 7]
print(max(names))
print(max(nums))
print(min(names))
print(min(nums))
print(len(names))
print(sorted(names))
print(sorted(nums))
print(sorted(nums,reverse=True))

#v2
print(','.join(names))
nums_names =["Gaurav",4,"Sagar"]
#Error will occur :print('-'.join(nums_names))
#Error will occur :print('-'.join(nums))
names.append('Garima')
print(names)