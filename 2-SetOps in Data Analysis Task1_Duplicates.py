# 2. Set Operations in Data Analysis
# Task 1: Duplicate Entries Cleanup 

def remove_duplicates(customer_ids):
    unique_ids = set()
    for customer_id in customer_ids:
        unique_ids.add(customer_id)
    unique_ids_list = list(unique_ids)
    unique_ids_list.sort()
    for unique_id in unique_ids_list:
        print(unique_id)
    # return unique_ids   # unique_ids  is a set
    # We can return unique_ids  or  unique_ids_list 
    return unique_ids_list

# Example usage:
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_customer_ids = remove_duplicates(customer_ids)
print(unique_customer_ids)
