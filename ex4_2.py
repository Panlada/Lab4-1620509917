class pyramid():
    pyramid_base = ""
    pyramid_with = ""
    pyramid_height = ""

    def calculaotor(self):
        vlp = (self.pyramid_base.P_base*self.pyramid_with.P_width*self.pyramid_height.P_height)/3
        print(vlp)



class pyramidbase():
    P_base = ""

class pyramidwidth():
    P_width = ""

class pyramidheight():
    P_height = ""

Pyramid = pyramid()
pyramid1base = pyramidbase()
pyramid1width = pyramidwidth()
pyramid1height = pyramidheight()

pyramid1base.P_base = 10
pyramid1height.P_height = 17
pyramid1width.P_width = 7 

Pyramid.pyramid_base = pyramid1base
Pyramid.pyramid_height = pyramid1height
Pyramid.pyramid_with = pyramid1width

Pyramid.calculaotor()