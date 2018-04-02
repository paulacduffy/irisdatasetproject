with open ("data/iris.csv") as f:
       for line in f:
        total = sum(float((line.split(',')[0])))
        print (total)
     
