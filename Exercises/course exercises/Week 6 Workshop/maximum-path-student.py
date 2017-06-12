def maxpath(triangle):
    pass

if __name__ == "__main__":

    triangle = open("triangle.txt","r").read().split("\n")

    for x in range(len(triangle)):
        triangle[x] = triangle[x].split(" ")
        for y in range(len(triangle[x])):
            triangle[x][y] = int(triangle[x][y])

    for row in triangle:
        print(row)

    print()
    print("The maximum path results in: ", maxpath(triangle))
    # Answer is 538 for the test case in triangle.txt

    for row in triangle:
        print(row)
