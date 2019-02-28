class Photo:
    def __init__(self, id, orientation, numTags, tags):
        self.id = id
        self.orientation = orientation
        self.numTags = numTags
        self.tags = tags
    

class Slide:
    def __init__(self, photoIds, tags):
        self.photoIds = photoIds
        self.tags = tags

# Read input    
def processFile(fileName):
    f = open(fileName)
    lines = f.readlines()

    numPhotos = int(lines[0])
    photos = []

    for i in range(1, numPhotos+1):
        line = lines[i].split(" ")
        orientation = line[0]
        numTags = int(line[1])
        tags = line[2:]
        photo = Photo(i -1, orientation, numTags, tags)
        photos.append(photo)

    return photos

# Output the slideshow
def outputFile(slideshow):
    outfile = open("files/Output.txt","w")
    outfile.write(str(len(slideshow)) + "\n")

    for slide in slideshow:
        outfile.write(str(slide.photoIds) + "\n")
        
    outfile.close()

# Calculate the interest factor of the whole slideshow
def getScore(slideshow):
    sum = 0
    for i in range(0, len(slideshow) - 1):
        sum += getInterest(slideshow[i], slideshow[i+1])

    return sum


# Calcutale the interest factor between 2 slides
def getInterest(slide1, slide2):
    left = []
    union = []
    right = []

    for tag1 in slide1.tags:
        if tag1 in slide2.tags:
            union.append(tag1)
        else:
            left.append(tag1)
    
    for tag2 in slide2.tags:
        if tag2 in slide1.tags:
            union.append(tag2)
        else:
            right.append(tag2)

    leftLen = len(left)
    unionLen = len(set(union))
    rightLen = len(right)
    return min(leftLen, unionLen, rightLen)


def main():
    fileName = "files/e_shiny_selfies.txt"
    #"b_lovely_landscapes.txt"
    #"c_memorable_moments.txt"
    #"d_pet_pictures.txt"
    #"e_shiny_selfies.txt"
    
    photos = processFile(fileName)
    slideShow = []
    spareVertical = ""
    noSpare = True

    # No time to worry about vertical, just stick them into one slide as they come in
    for photo in photos:
        print(noSpare)
        if(photo.orientation == "V"):
            if noSpare:
                spareVertical = photo
                noSpare = False
            else:
                slide = Slide(str(spareVertical.id) + " " + str(photo.id), set(spareVertical.tags + photo.tags))
                slideShow.append(slide)
                noSpare = True
        else:
            slide = Slide(photo.id, photo.tags)
            slideShow.append(slide)

    OrderedSlideShow = []
    OrderedSlideShow.append(slideShow[0])
    slideShow.remove(slideShow[0])

    # Try to get a better Interest factor between the slides
    # If no better slide found in 3 attempts, skip to next
    for slide in slideShow:
        bestInterest = 0
        bestIndex = 0
        bestSlide = ""
        numTries = 0

        for compareSlide in slideShow:
            tempInterest = getInterest(OrderedSlideShow[-1], compareSlide)
            if tempInterest >= bestInterest:
                numTries += 1
                bestInterest = tempInterest
                bestSlide = compareSlide
                bestIndex = slideShow.index(compareSlide)
            elif(numTries >= 3):
                break
        
        OrderedSlideShow.append(bestSlide)
        slideShow.remove(slideShow[bestIndex])

    # Add whatever is left to Ordered Slide Show
    OrderedSlideShow += slideShow
    outputFile(OrderedSlideShow)


if __name__=="__main__":
    main()