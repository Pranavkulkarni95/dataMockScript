

#Create the Item class

class item:
    def __init__(self,Item,Item_description,Department,final_pack_qty,final_cost_amt,final_allo_amt):
        self.Item = Item
        self.Item_description = Item_description
        self.Department = Department
        self.final_pack_qty = final_pack_qty
        self.final_cost_amt = final_cost_amt
        self.final_allo_amt = final_allo_amt

    def print_item_description(self):
        print("::::::::::::::::::::ITEM DETAILS::::::::::::::::: ")
        print("Item: ", self.Item)
        print("Item_description: ", self.Item_description)
        print("Department: ", self.Department)
        print("final_pack_qty: ", self.final_pack_qty)
        print("final_pack_qty: ", self.final_cost_amt)
        print("final_pack_qty: ", self.final_allo_amt)




