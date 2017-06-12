def distance(xy1,xy2):
    return ( (xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2 ) ** 0.5

def min_manhattan(coordinates):
    pass
            

if __name__ == "__main__":
    # Read test.txt, create list of coordinates
    all_coords = open("test.txt","r").read().split("\n")[:-1]
    coordinates = []
    for xypair in all_coords:
        x,y = xypair.split(" ")[0], xypair.split(" ")[1]
        coordinates.append( (int(x),int(y)) )

    # Compute the x,y pair that is on average closest to all points
    closest_avg = min_manhattan(coordinates)

    # Answer is (8,3) for the test case
    print("Most central point to all points in test.txt: ", closest_avg) 
