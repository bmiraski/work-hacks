import string
import sys

def get_properties(file):
    """
    Returns a list of all the property values in a file that are not commented out
    """
    f = open(file, "r")
    xs = f.readlines()
    f.close()
    new_xs = []
    for x in range(len(xs)):
        if "#" not in xs[x]:
            if "=" in xs[x]:
                new_xs.append(xs[x])  

    new_xs.sort()
    a = "clean_{0}".format(file)
    
    g = open(a, "w")
	
    for v in new_xs:
        g.write(v)
    g.close()

    return a
	

def removevalues(file):
    """
    Removes all of the values for properties
    """
    f = open(file, "r")
    xs = f.readlines()
    f.close()

    new_xs = []
    for i in xs:
        a = 0
        for c in i:
            if c != "=" and c != " ":
                a += 1
            else: 
                if a != 0:
                    newstr = i[0:a] + "\n"      
                    new_xs.append(newstr)
                break
    new_xs.sort()

    a = "stripped_{0}".format(file)
    g = open(a, "w")
	
    for v in new_xs:
        g.write(v)
    g.close()

    return a
    
def comparelists(filea, fileb):
    """ Return a set of values missing in files """
    missinga = []
    missingb = []    
    f = open(filea, "r")
    xs = f.readlines()
    f.close()

    b = open(fileb, "r")
    ys = b.readlines()
    b.close()    

    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            break       # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            break

        # Both lists still have items, compare item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            missingb.append(xs[xi])
            xi += 1
        else:
            missinga.append(ys[yi])              
            yi += 1
   
    g = open("results.txt", "w")
    
    g.write("Items missing in {0}\n".format(filea))
    for v in missinga:
        g.write(v)
    
    g.write("\n\n\n")

    g.write("Items missing in {0}\n".format(fileb))
    for n in missingb:
        g.write(n)

    g.close()





	
# Open first file
# Create list of lines, skipping comments, sorted


# Iterate on list and remove everything after the equals


# Open second file
# Create list of lines, skipping comments, sorted


# Iterate on list and remove everything after the equals	



# Compare two lists, write to file items in A not B
# Compare two lists, write to file items in B not A	
	
comparelists(removevalues(get_properties(sys.argv[1])), removevalues(get_properties(sys.argv[2])))
	
	
