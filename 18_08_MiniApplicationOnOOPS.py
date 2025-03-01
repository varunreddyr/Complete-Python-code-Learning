class Movie:
    """THis class developed by varun for demo"""
    def __init__(self,title,hero,heroine):  #(self,x,y,z)
        self.title=title                    #self.title=x
        self.hero=hero                      #self.hero=y
        self.heroine=heroine                #self.heroine=z


    def info(self):
        print("Movie name:",self.title)
        print("Movie hero",self.hero)
        print("Movie heroine",self.heroine)

list_of_movies=[]
while True:
    title=input("Enter Movie name:")
    hero=input("Enter Hero name:")
    heroine=input("Enter heroine name:")
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Movie added successfully.....")
    option=input("Do you want to add one more movie[Yes/No]")
    if option.lower()=='no':
        break
print('All Movies information....')
for movie in list_of_movies:
    movie.info()
    print()
                                            # While execution the objects , data are stored in heap memory
                                            # Once the execution is completed the Heap memory is cleared
                                            # We can store the data permanently by using files, Databases etc
