import mysql.connector

class imsdatabase():

    def __init__(self):
       self.conn = mysql.connector.connect(
            host="107.180.50.225",
            user="admin3",
            passwd="joshua747",
            database="imsdb3"
        )

    def __del__(self):
        self.conn.close()

    def getAllItems(self):
        sql = """SELECT * FROM ITEM"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # result contains the data in tuples
        # [['123','Pants','50.99','M','230','801234','0986263'],['145','Shoes','30.49','M','90','087234','65892']]
        # data does not have headers
        #convert it to JSON
        items =[]
        for row in result:
            items.append({ 'ItemID' : row[0], 'Name' : row[1], 'Price' : row[2], 'Gender' : row[3], \
             'Stock' : row[4], 'StoreID' : row[5], 'SupplierID' : row[6], 'Image' : row[7]})
        cursor.close()
        return items

    def getAllTops(self):
        sql = """SELECT * FROM TOPS"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        items =[]
        for row in result:
            items.append({ 'ItemID' : row[0], 'Chest_Size' : row[1], 'Shirt_Length' : row[2], 'Type' : row[3]})
        cursor.close()
        return items

    def getAllBottoms(self):
        sql = """SELECT * FROM BOTTOMS"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        items =[]
        for row in result:
            items.append({ 'ItemID' : row[0], 'Waist_Size' : row[1], 'Pant_Length' : row[2], 'Type' : row[3]})
        cursor.close()
        return items

    def getAllShoes(self):
        sql = """SELECT * FROM SHOES"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        items =[]
        for row in result:
            items.append({ 'ItemID' : row[0], 'ShoeSize' : row[1], 'Type' : row[2]})
        cursor.close()
        return items

    def getAllAccessories(self):
        sql = """SELECT * FROM ACCESSORIES"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        items =[]
        for row in result:
            items.append({ 'ItemID' : row[0], 'Type' : row[1]})
        cursor.close()
        return items

    def addNewUser(self, uid, fname, lname, address, email, password):
        sql = """INSERT INTO USER VALUES ('{0}','{1}','{2}','{3}','{4}','{5}', {6})"""
        cursor = self.conn.cursor()
        admin = False
        cursor.execute(sql.format(uid,fname, lname, address, email, password, admin))
        self.conn.commit()
        retval = cursor.lastrowid
        cursor.close()
        return retval;

    #new purchases should be new tuple 
    def addPurchase(self, PurchaseID, ItemID, UserID, DateTime, Quantity):
        # sql = """SELECT * FROM PURCHASE WHERE UserID = '{0}' AND ItemID = '{1}'"""
        cursor = self.conn.cursor()
        # cursor.execute(sql.format(UserID, ItemID))
        # result = cursor.fetchone()

        # if result == None:
        sql2 = """INSERT INTO PURCHASE VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"""
        cursor.execute(sql2.format(PurchaseID, ItemID, UserID, DateTime, Quantity))
        self.conn.commit()

        sql4 = """ UPDATE ITEM 
                    SET Stock = Stock - '{0}'
                    WHERE ItemID = '{1}' """

        cursor.execute(sql4.format(Quantity, ItemID))
        self.conn.commit()
        # else:
        #     sql3 = """  UPDATE PURCHASE 
        #                 SET Quantity = {0} 
        #                 WHERE ItemID = {1} AND UserID = {2}"""
        #     cursor.execute(sql3.format(result[2] + quantity, ItemID, UserID))
        #     self.conn.commit()

        cursor.close()
        return "Success"


    def getPurchases(self, uid):
        sql = """   SELECT *
                    FROM PURCHASE as P, ITEM as I
                    WHERE P.UserID = '{0}' AND P.ItemID = I.ItemID  """ # Might not work because of same attribute names
        cursor = self.conn.cursor()
        cursor.execute(sql.format(uid))
        result = cursor.fetchall()
        
        items =[]
        for row in result:
            items.append({'Image': row[12], 'Name': row[6], 'Price': row[7], 'Date': row[3], 'ItemID': row[1]}) # I dont know the order -- This will be 3D array
        cursor.close()
        return items
    
    def getItemById(self, itemId):
        sql = """   SELECT *
                    FROM ITEM
                    WHERE ItemID='{0}'"""
        cursor = self.conn.cursor()
        cursor.execute(sql.format(itemId))
        result = cursor.fetchone()

        item = {'ItemID' : result[0], 'Name' : result[1], 'Price' : result[2], 'Gender': result[3], \
        'Stock' : result[4], 'StoreID' : result[5], 'SupplierID' : result[6], \
        'Image' : result[7]}
        
        cursor.close()
        return item

    def validateUser(self, email):
        sql = """   SELECT UserID
                    FROM USER
                    WHERE Email = '{0}' """
        cursor = self.conn.cursor()
        row_count = cursor.execute(sql.format(email))
        result = cursor.fetchone()
        cursor.close()
        if row_count == None:
            return "success"
        else:
            return "failed"

    def getAllCart(self, UserID):
        sql = """   SELECT *
                    FROM ITEM as I, CART as C
                    WHERE C.ItemID = I.ItemID AND C.UserID = {0}"""
        cursor = self.conn.cursor()
        cursor.execute(sql.format(UserID))
        result = cursor.fetchall()
    
        items = []
        for row in result:
            items.append({ 'ItemID' : row[0], 'Name' : row[1], 'Price' : row[2], 'Gender' : row[3], \
             'Stock' : row[4], 'StoreID' : row[5], 'SupplierID' : row[6], 'Image' : row[7], 'Quantity': row[10]})
        cursor.close()
        return items

    def addToCart(self, ItemID, UserID, Quantity):
        sql = """   SELECT Quantity
                    FROM CART
                    WHERE ItemID = '{0}' AND UserID = '{1}' """
        cursor = self.conn.cursor()
        cursor.execute(sql.format(ItemID, UserID))
        result = cursor.fetchone()

        if result == None:
            sql2 = """  INSERT INTO CART VALUES ('{0}', '{1}', '{2}') """
            cursor.execute(sql2.format(ItemID, UserID, Quantity))
            self.conn.commit()
        else:
            sql3 = """  UPDATE CART
                        SET Quantity = '{0}'
                        WHERE ItemID = '{1}' AND UserID = '{2}' """
            cursor.execute(sql3.format(result[0] + Quantity, ItemID, UserID))
            self.conn.commit()
        cursor.close()
        return "success"

    def checkLogin(self, email, password):
        sql = """SELECT  * FROM USER WHERE Email = '{0}' AND Password = '{1}'"""
        cursor = self.conn.cursor()
        cursor.execute(sql.format(email, password))
        retval = cursor.fetchone()
        cursor.close()
        return retval

    def restock(self, itemID, amount, date):
        sql = """UPDATE ITEM SET Stock = Stock + '{0}' WHERE ItemID = '{1}';"""
        cursor = self.conn.cursor()
        cursor.execute(sql.format(amount, itemID))
        self.conn.commit()

        sql2 = """ SELECT * FROM ITEM WHERE ItemID = '{0}'; """
        cursor.execute(sql2.format(itemID))
        result = cursor.fetchone()
        storeid = result[5]
        suppid = result[6]
        
        sql3 = """ INSERT INTO RESTOCKORDER VALUES(null, '{0}', '{1}', '{2}', '{3}', '{4}'); """
        cursor.execute(sql3.format(date, amount, itemID, suppid, storeid))
        self.conn.commit()
        cursor.close()
        return

    #Adding CART to PURCHASE
    def cartByUser(self, UserID):
        sql = """ SELECT * FROM CART WHERE UserID = '{0}' """
        cursor = self.conn.cursor()
        cursor.execute(sql.format(UserID))
        result = cursor.fetchall()

        items = []
        for row in result:
            items.append({'ItemID': row[0], 'UserID': row[1], 'Quantity': row[2]}) #assuming [ItemID, UserID, Quantity]
        
        cursor.close()
        return items # call add to purchase after
    
    def deleteCartItem(self, ItemID, UserID):
        sql = """   DELETE FROM CART WHERE ItemID = '{0}' AND UserID = '{1}' """
        cursor = self.conn.cursor()
        cursor.execute(sql.format(ItemID, UserID))
        self.conn.commit()
        cursor.close()
        return

    def getHistory(self):
        sql = """ SELECT * FROM RESTOCKORDER """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        history = []
        for row in result:
            history.append({'OrderID': row[0], 'Date': row[1], 'Quantity': row[2], 'ItemID': row[3], 'SupplierID': row[4], 'StoreID': row[5]})
        cursor.close()
        return history

    # def getAllPurchases(self):
    #     #we need user table
