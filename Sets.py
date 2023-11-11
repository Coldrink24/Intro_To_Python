set1 = {1,2,3,4,5,6}
set2 = {"Eslam", "Mohamed", "Apas", "Apas", "Hmad"}
set3 = {1,2,3,2,1}
set4 = {100,10,20,30,40,50}
set5 = {10,60,70,80,90,100}
set6 = {11,22,33,44,55}
set7 = {11,22,77,88,99}


print (set1.union(set2))    # Union() Method Used To Add A Set To Another One , And You Can Do This Jop Like This Code " set1|set2 "

set1.add(7)
print (set1)

set1.remove(1)
print (set1)   # Remove() Method Used To Remove A Element From The Set, But If You Input A Element Doesn't In The Set Then Remove() Method Will Print To You An Error

set1.discard(2)
print (set1)   # Discard() Method Do The Same Jop Of Remove() But Without Error

print (set2.pop())        # Pop() Method Print To You A Random Element From The Set
print (set2) 

set3.clear()
 
set3.update(set4)
print (set3)  # Update() Method Do The Same Jop Of Union() But You Can With Update() Add A List To Set

set5.update((1,2,3,4))
print (set5)    # Updating With List

print (set4.difference(set5))    # Differance() Method Used to Show You The Differance Between The Two Sets ,By Printing The Elements In The First Set Don't Exist In The Second Se
print (set4-set5)        # By This Code You Can Do The Same Jop Of Difference() Method

set4.difference_update(set2)
print (set4)   # Difference_update() Method used To Add The Different Elemnsts To The Main Set "Set4 In This Example"


print (set4.intersection(set5))  # Intersection() Method Print The Mutual Elements Between The Two Sets
print (set4&set5)        # Do The Same Jop Of Intersection() Method

set4.intersection_update(set5)
print (set4)   # The Mothod Of Intersection_update() Update The Main Set With The Mutual Elements Between The Two Sets

print (set6.symmetric_difference(set7))   #Symmtric_Difference() Method Print The All UnMutual Elements Between The Two Sets
print (set6^set7)              # Another Code To Do The Same Prev Jop

print (set6.issuperset(set3))    # IsSuperSet() Prints Thats True If The First Method Exists Completely In The Second Set And Prints False If Not
print (set3.issubset(set1))    # IsSubSet() Tell You If The Elemensts Of The Second Set Exist Completely In The First Set Or Not
print (set3.isdisjoint(set1))  # IsDisJoint() Tell You If The Elements Of The Tow Sets Completly Different Or Not ( There Isn't Any Mutual Element Between The Two Sets)

