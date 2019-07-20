def addOne(number):
    return number + 1
# grid = input("Enter grid:")
def get_grid(grid):
    grid_list = grid.split(",")
    xcord = grid_list[0]
    ycord = grid_list[1]
    return (int(xcord), int(ycord))

class Rover():

    def __init__(self, cordinates, orientation, planet_cord):
        self.cordinates = cordinates
        self.orientation = orientation
        self.planet_cord = planet_cord

    
    def rotate_right(self,orientation):
        if orientation == "N":
            self.orientation = "E"
        elif orientation == "E":
            self.orientation = "S"
        elif orientation == "S":
            self.orientation = "W"
        else:
            self.orientation = "N"
   
        return (self.cordinates,self.orientation)
        
    def rotate_left(self,orientation):
        if orientation == "N":
            self.orientation = "W"
        elif orientation == "W":
            self.orientation = "S"
        elif orientation == "S":
            self.orientation = "E"
        else:
            self.orientation = "N"
   
        return (self.cordinates,self.orientation)
    
    def move_forward(self, cordinates, orientation):
        
        x = int(cordinates[0])
        y = int(cordinates[1])

        if orientation == 'N':
            self.cordinates = (x,y+1)
            self.orientation = orientation
            return (self.cordinates, self.orientation)
        elif orientation == 'E':
            self.cordinates = (x+1,y)
            self.orientation = orientation
            return (self.cordinates, self.orientation)
        elif orientation == 'W':
            self.cordinates = (x-1,y)
            self.orientation = orientation
            return (self.cordinates, self.orientation)
        else:
            self.cordinates = (x,y-1)
            self.orientation = orientation
            return (self.cordinates, self.orientation)

    def get_instructions(self,instructions, orientation, cordinates):

        for inst in instructions:
            
            if inst == 'L':
                self.rotate_left(orientation=self.orientation)

            if inst == 'R':
                self.rotate_right(orientation=self.orientation)
            if inst == 'M':
                self.move_forward(cordinates=self.cordinates, orientation=self.orientation)


def main():
    
    grid = input("Enter a grid: ")
    cord_orint = input("Enter cordinates and orientation: ")
    instr = input("Instructions: ")

    cords_list = cord_orint.split(',')
    x_y = (cords_list[0],cords_list[1])
    orientation_str = cords_list[2]

    grid_cordinates = get_grid(grid)
    rov = Rover(cordinates = x_y, orientation= orientation_str, planet_cord= grid_cordinates)
    rov.get_instructions(instructions=instr,orientation=orientation_str,cordinates=x_y)


if __name__ == '__main__':
      main()

            




        

