import shutil

nessora = input('Ну что, обошлось? (y/n): ')
if nessora == 'y':

    f = open('nessora', 'r+')    # opening file + create if not exists
    counter = f.read()  # here we read the file
    if counter == '':   # if file is empty
        counter = 1
    else:
        counter = int(counter) + 1  # plus 1 to the number in file

    f.seek(0, 0)    # cursor to begining
    f.write(str(counter))

elif nessora == 'n':   # if nessora = 'n' - write the number to new file; clear the 'nessora' fil
    f = open('nessora', 'r+')
    counter = f.read()  # here we read the file

    new_f = open('achievement', 'r+')
    new_result = new_f.read()

    if counter != '':   # compare number in file with new result
        counter = int(counter)
        new_result = int(new_result)
        if counter > new_result:
            new_f.truncate(0)
            new_f.seek(0)
            new_f.write(str(counter))
            # shutil.copy('/Users/liudmila/PycharmProjects/les01-start/nessora', '/Users/liudmila/PycharmProjects/les01-start/achievement')
    f.truncate(0)

else:
    print('Incorrect input, check the answer, use only lowercase')






