
my_list=[1,2,3,4,5,6]

my_second_list=["Good","Bad","Wonderful","Awful"]

#List elements are saved in lists starting with position 0

# print("\nPrinting first element of lists")

# print my_list[0]
#
# print "\n"
#
# print my_second_list[0];

#lets use a variable for the index and print some information from both lists

# chosen_index=0;
#
# print my_list[chosen_index]
# print "\n"
# print my_second_list[chosen_index]

#List elements in even positions
for n in my_list[::2]:
    print n

print "\n"

#List elements from position 2 to 4
for n in my_list[2:4]:
    print n

#TODO: List elements from second list like above