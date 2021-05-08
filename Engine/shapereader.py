class shapereader(shapefile):
    
    
    def __init__(self, path):
        self.path = path

    def reader(self, path):
        with shapefile.reader(self.path) as shp:
            print(shp)
