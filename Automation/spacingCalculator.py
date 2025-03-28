numRectangles = 3 #int(input("Number of rectangles: "))
rectangleWidth = 100 #int(input("Width of rectangles: "))
totalWidth = 640 #int(input("Screen width: "))

widthOfTotalRec = numRectangles * rectangleWidth
totalSpace = totalWidth - widthOfTotalRec
spacing = totalSpace / (numRectangles + 1)

prev = 0
for i in range(numRectangles):
    print("xPos: ", i, spacing + (i * 100) + (i * 85))
    