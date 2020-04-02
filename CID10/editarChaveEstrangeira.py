#!/usr/bin/env python
#-*- coding: UTF-8-*-

'''
sites usados na aula
Banco
http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html

    sql = """
            UPDATE cid_sub_categoria
            SET  categoria_id = ?
            WHERE id = ?
    """
    cursor.execute(sql, (subString, id))
    conn.commit()

'''

import sqlite3

sqlSubCategoria = "SELECT * FROM cid_sub_categoria;"

conn = sqlite3.connect('auxiliar.db')
conn.text_factory = str
cursor = conn.cursor()

cursor.execute(sqlSubCategoria)

consultSubCategoria = cursor.fetchall()

for regSubCat in consultSubCategoria:
    id = regSubCat[1]
    subString = id[0:3]
    # trecho upDate
    sql = """
            UPDATE cid_sub_categoria
            SET  categoria_id = ?
            WHERE id = ?
    """
    cursor.execute(sql, (subString, id))
    conn.commit()

    print(subString)
    
print("Dados alterados com sucesso!")    

conn.close()



