import pymysql

# 1. 建立连接
conn = pymysql.connect(host='rm-uf68x30b87b9zi061yo.mysql.rds.aliyuncs.com',
                    port=3306,
                    user='root',
                    passwd='Zyq1234560',   # password也可以
                    db='gameserv_order',    #数据库名字
                    charset='utf8')   # 如果查询有中文需要指定数据库编码
                    
# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

# 3. 查询数据库（读）
cur.execute("select order_no from gameserv_card_order_info_1 where id='1181835261673672706'")

# 4. 获取查询结果
result = cur.fetchall()[0][0]
print(result)

# # 3. 更改数据库（写）
# cur.execute("delete from user where name='李四'")

# # 4. 提交更改
# conn.commit()  # 注意是用的conn不是cur

# 5. 关闭游标及连接
cur.close()
conn.close()