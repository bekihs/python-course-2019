import pymysql

connection = pymysql.connect(host='localhost', port=3306,user='root',password='1234',db='course_python1')

# try:
#     #cursor = connection.cursor()
#     with connection.cursor() as cursor:
#         # sql = "insert into document(text  , employeeID) value (%s , %s);" 
#         sql = "select text, office.name officeName , employee.name employeeName , manager.name managerName"
#         sql += " from document "
#         sql += "join employee on  document.employeeID = employee.employeeID "
#         sql += "join manager on employee.managerID = manager.managerID "
#         sql += "join office on manager.officeID = office.officeID"
#         cursor.execute(sql)  
#         result = cursor.fetchall()
#         print(result)
#     # connection.commit()     
# finally:
#     connection.close()


    #     # Read a single record
    #     sql = "INSERT INTO `animals` (`id`,`name`,`age`,`animal_type_id`) VALUES (%s, %s, %s, %s)"
    #     cursor.execute(sql , (4,'Griz',5,1))
     
    # connection.commit()
     


    # # with connection.cursor() as cursor:
    # #     # Create a new record
    # #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    # #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # # # connection is not autocommit by default. So you must commit to save
    # # # your changes.
    # # connection.commit()

    # # with connection.cursor() as cursor:
    # #     # Read a single record
    # #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    # #     cursor.execute(sql, ('webmaster@python.org',))
    # #     result = cursor.fetchone()
    # #     print(result)