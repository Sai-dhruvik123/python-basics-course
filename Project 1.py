#traffic light simulator
colour=input()
if(colour == 'green'):
    print('you may now go')
elif(colour == "red"):
    print("stop now")
elif(colour == 'orange'):
    print('slow down and wait')
else:
    print('this colour is not there in traffic lights')