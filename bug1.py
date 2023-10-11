class Base:
  def __init__(self, x, y, size):
     self.x = x
     self.y = y
     self.size = size
     
  def shape(self):
    return "This is a circle"

class Circle(Base):
    pass
    
    def draw(self):
        return f"""({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """
    
    
def main():
  c = Circle(1,2,3)
  print(c.shape())
  print(c.draw())
        
        
main()