import mysql.connector as sql

mydb = sql.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'dahaka1961',
    database = 'mydb'
)
mycursor = mydb.cursor()

print('ВНИМАНИЕ! Вы зашли в систему!')
print ('Вот ваша база данных')
mycursor.execute('SELECT * FROM students')
myresult = mycursor.fetchall()
for row in myresult:
    print (row)
print('Если вы хотите изменить вашу базу данных, напишите "0"')
print('Если вы хотите добавить нового студента в вашу базу данных, напишите "1"')
    
a = int(input())

if a == 0:
    print('Введите номер студента в списке и что вы хотите у него изменить')
    print('Введите его номер в списке:')
    number = input()
    print('Если вы хотите изменить его ФИО, введите "ФИО"')
    print('Если вы хотите изменить его предмет, введите "Предмет"')
    print('Если вы хотите изменить его количество долгов, введите "Долги"')
    change = input()
    if change == 'ФИО':
        print('Введите новое ФИО студента:')
        changeName = input()
        mycursor.execute("UPDATE `mydb`.`students` SET `Name` = '" + changeName + "' WHERE (`Students` = '" + number + "')")
    if change == 'Предмет':
        print('Введите новый предмет студента:')
        changeSubject = input()
        mycursor.execute("UPDATE `mydb`.`students` SET `Subject` = '" + changeSubject + "' WHERE (`Students` = '" + number + "')")
    if change == 'Долги':
        print('Введите новое количество долгов студента:')
        changeDebts = input()
        mycursor.execute("UPDATE `mydb`.`students` SET `Debts` = '" + changeDebts + "' WHERE (`Students` = '" + number + "')")
    mydb.commit()
    print('С учётом ваших изменений база данных теперь выглядит вот так:')
    mycursor.execute('SELECT * FROM students')
    myresult = mycursor.fetchall()
    for row in myresult:
        print (row)
if a == 1:
    sqlFormula = 'INSERT INTO students (Students, Name, Subject, Debts) VALUES (%s, %s, %s, %s)'
    
    print('Введите поочерёдно сначала номер студента в списке, затем его ФИО, затем предмет, затем количество долгов студента:')
    students = input()
    name = input()
    subject = input()
    debts = input()
    
    insertsql = (students, name, subject, debts)
    
    mycursor.execute(sqlFormula, insertsql)
    mydb.commit()
    
    print('С учётом ваших изменений база данных теперь выглядит вот так:')
    mycursor.execute('SELECT * FROM students')
    myresult = mycursor.fetchall()
    for row in myresult:
        print (row)