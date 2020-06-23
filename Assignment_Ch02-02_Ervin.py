doorLength = input('Enter the doors length : ')
doorWidth = input('Enter the doors width : ')
firstWindowLength = input('Enter the first windows length : ')
firstWindowWidth = input('Enter the first windows width : ')
secondWindowLength = input('Enter the second windows length : ')
secondWindowWidth = input('Enter the second windows width : ')
bookshelfLength = input('Enter the bookselfs length : ')
bookshelfWidth = input('Enter the bookshelfs width : ')
roomLength = input('Enter the rooms length : ')  
roomWidth = input('Enter the rooms width : ')
roomHeight = input('Enter the rooms height : ')

oneGallon = 120

door = (int(doorLength)* int(doorWidth))
firstWindow = (int(firstWindowLength)* int(firstWindowWidth))
secondWindow = (int(secondWindowLength)* int(secondWindowWidth))
bookShelf = (int(bookshelfLength)* int(bookshelfWidth))
room = int(2* (int(roomLength)+ int(roomWidth)) * int(roomHeight)) 


totalPaint = (room - door - firstWindow - secondWindow - bookShelf)


gallonsNeeded = totalPaint/ oneGallon

paint = round(gallonsNeeded, 2)
print('The amount of paint needed to paint the room: ',paint)


