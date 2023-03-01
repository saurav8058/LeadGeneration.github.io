def ParseToDictAll(cursor):
    records=cursor.fetchall()
    description=cursor.description
    columnnames=[]
    for des in description:
      columnnames.append(des[0])
    print("Column Names:",columnnames)  
    data=[]
    for row in records:
      data.append(dict(zip(columnnames,list(row))))
    print("Data:",data)  
    return data

def ParseToDictOne(cursor):
    row=cursor.fetchone()
    description=cursor.description
    columnnames=[]
    for des in description:
      columnnames.append(des[0])
    print("Column Names:",columnnames)  
    data=dict(zip(columnnames,list(row)))
    print("Data:",data)  
    return data    