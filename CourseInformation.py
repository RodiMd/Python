#Course Information
#dictionary contain course numbers and room numbers

def main():

    courseRoomNumber = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
    courseNTeacherN = {'CS101':'Haynes', 'CS102':'Alvardo', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    courseTime = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

    studentInput = input('Enter the course number ')
    x = studentInput.upper()

    print('Room number: ', courseRoomNumber[x])
    print('Teacher: ', courseNTeacherN[x])
    print('Time: ', courseTime[x])
    
main()
