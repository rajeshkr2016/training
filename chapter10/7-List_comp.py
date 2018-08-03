fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

'''
 The if statement says to only add those items that are not equivalent to the string 'octopus', 
 so the new list only takes in items from the tuple that do not match 'octopus'.
'''