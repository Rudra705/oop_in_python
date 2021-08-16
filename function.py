def count():
    file_name = input("Enter the file name\n")
    file = open(file_name,'r')

    num_of_words = 0

    for line in file:
        words = line.split()
        num_of_words = num_of_words + len(words)
    
    print("Number of words : ")
    print(num_of_words)

    
count()
        
