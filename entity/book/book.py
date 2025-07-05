
class Book:
    def __init__(self,name:str,author:str,desc:str,price:float,image:str,file:str):
        self.name = name
        self.author = author
        self.desc = desc
        self.price = price
        self.image = image
        self.file = file

    def to_json(self):
        return {
            'name': self.name,
            'author': self.author,
            'desc': self.desc,
            'price': self.price,
            'image': self.image,
            'file': self.file
        }