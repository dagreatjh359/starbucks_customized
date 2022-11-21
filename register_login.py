import datetime
import pymysql

cnx = pymysql.connect(user='root', password='YooJH@0319', host='localhost', database='starbucks_customized',autocommit=True)
cursor = cnx.cursor()

## 4 querys from hw2

print("1.")
# 1. SELECT query
query_1 = "Select * From starbucks_bread;"
cursor.execute(query_1)
for data in cursor:
    print("bread_id {}, {}'s description is {}".format(data[0], data[1], data[2]))

print("\n--------------------------------------------------------------------------------------------------------\n2.")
# 2. Using more than one tables by "FROM"
# selecting customized bread's id whose name is peanut sand and no lurpak butter is applied.
query_2 = "Select * From Starbucks_Bread as SB, Customized_bread as CB " \
          "Where SB.product_name=\"peanut_sand\" and CB.Lurpak_Butter = \"yes\" and SB.bread_id = CB.bread_id;"
cursor.execute(query_2)
peanut_sand_with_no_LB = []
for data in cursor:
    peanut_sand_with_no_LB.append((data[1], data[4], data[5]))

for out in peanut_sand_with_no_LB:
    print("Customized peanut sand's id is {} and the owner is {}.".format(out[1], out[2]))

print("\n--------------------------------------------------------------------------------------------------------\n3.")
# 3. Using SET query
# Update payment amount by applying 10% discount if purchase is done by credit card.

query = "select * from customized_order"
cursor.execute(query)
print("Order_id customer_id shop_id custom_bread    custom_coffee   price")
for data in cursor:
    print(data)
    print("{} {} {} {}            {} {}".format(data[1], data[2], data[3], data[4], data[5], data[6]))

query_3 = "UPDATE customized_order SET payment_amount = " \
          "CASE " \
          "WHEN payment_method = \"credit_card\" " \
          "THEN payment_amount*0.7 " \
          "ELSE payment_amount " \
          "END;"
cursor.execute(query_3)

print("after update")
query = "select * from customized_order"
cursor.execute(query)
print("Order_id customer_id shop_id custom_bread    custom_coffee   price")
for data in cursor:
    print(data)
    print("{} {} {} {}            {} {}".format(data[1], data[2], data[3], data[4], data[5], data[6]))

print("\n--------------------------------------------------------------------------------------------------------\n4.")
# 4. Using Subquery
# select shop id whose address is in 'Seoul’ and has drive through.

query_4 = "select shop_id, shop_address " \
          "From starbucks_shop " \
          "Where shop_address like \"%Gyeonggido%\" and " \
          "shop_id in( select shop_id " \
          "From starbucks_shop " \
          "Where DriveThrough_or_not = \"no\");"
cursor.execute(query_4)
print("shop_id whoese in Gyeonggido : ")
for data in cursor:
    print("{}, address is {}".format(data[0], data[1]))

cursor.close()
cnx.close()
