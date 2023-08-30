

#Create the vendor class
#this is the new case
class vendor:
    def __init__(self, vendor_id,Vendor_name,vendor_sub_account_id,vendor_collect_on_delivery_ind):
        self.vendor_id = vendor_id
        self.Vendor_name = Vendor_name
        self.vendor_sub_account_id = vendor_sub_account_id
        self.vendor_collect_on_delivery_ind = vendor_collect_on_delivery_ind

    def print_vendor_details(self):
        print("::::::::::::::::::::VENDOR DETAILS::::::::::::::::: ")
        print("vendor_id: ", self.vendor_id)
        print("Vendor_name: ", self.Vendor_name)
        print("vendor_sub_account_id: ", self.vendor_sub_account_id)
        print("vendor_collect_on_delivery_ind: ", self.vendor_collect_on_delivery_ind)



