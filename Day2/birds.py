class Birds:

    def __init__(self):
        """constructor for this class"""
        #create member animals
        self.members = ['Sparrow', 'Robin', 'Dock']

    def printMemebers(self):
        print('Printing members of the Birds class')
        for member in self.member:
            print('/t%s ' % member)
