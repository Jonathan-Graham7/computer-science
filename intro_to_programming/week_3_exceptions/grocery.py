"""
Suppose that you're in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one's input to a program).
Then output the user's grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user's input case-insensitively.
"""
def main():
    grocery_list = []
    while True:
        try:
            grocery = input().upper()
            grocery_list.append(grocery)
        except EOFError:
            print("")
            purchaseList(grocery_list)
            break
    return

def purchaseList(grocery_list):
    grocery_list.sort()
    new_list = []
    item_counts = []
    for i in range(len(grocery_list)):
        item_count = 0
        for item in grocery_list:
            if grocery_list[i] == item:
                if grocery_list[i] not in new_list:
                    item_count += 1
        if grocery_list[i] not in new_list:
            new_list.append(grocery_list[i])
            item_counts.append(item_count)
    item_counts = item_counts[:len(new_list)]
    for num in range(len(item_counts)):
        print(f"{item_counts[num]} {new_list[num]}")

main()