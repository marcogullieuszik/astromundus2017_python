def count_lines(f):
    with open(f) as ff:
        lines=ff.readlines()
        return len(lines)

n1=count_lines("files/example1.txt")
n2=count_lines("files/example2.txt")
n3=count_lines("files/example_table.txt")
print (n1,n2,n3)