from typing import Any, Optional
from datetime import datetime


reclaims=[]

#question 1:

def get_reclaim()->dict:
    """
    Prompts the user for details of an insurance reclaim and returns a dictionary with the reclaim information.

    The reclaim contains the following details:
    - ID: Unique identifier of the reclaim.
    - Amount: reclaim amount in euros.
    - Type: Category of the reclaim (e.g., "health", "accident").
    - Status: Current status of the reclaim ("approved", "pending", "rejected").
    - Date: Submission date of the reclaim (format: "YYYY-MM-DD").

    :return: A dictionary containing the reclaim's information.
    """
    reclaim={}
    reclaim['id']=int(input('id ? = '))
    reclaim['amount']=float(input('amount ? = '))
    reclaim['type']=input('type ? = ')
    reclaim['status']=input('status ? = ')
    #reclaim['date']=input('date ? = ')
    #if we want to get it like as a date
    reclaim['date']= datetime.strptime(input('date ? = '), "%Y-%m-%d").date()  # Convert to date

    return reclaim

def create_reclaim():

    """
    Creates a new insurance reclaim and adds it to the global list of reclaims.

    :return: None
    """
    rc=get_reclaim()
    reclaims.append(rc)

#question 2:

def eval_approved_reclaims()->float:

    """
    Calculates the total amount of all approved reclaims.

    :return: The sum of the amounts of approved reclaims.
    """
    s=0
    for i in range(len(reclaims)):
        if reclaims[i]['status'] == 'approved':
            s+=reclaims[i]['amount']
    return s

def eval_approved_reclaims_v2()->float:
    s=0
    for reclaim in reclaims:
        if reclaim['status'] == 'approved':
            s+=reclaim['amount']
    return s

##question 3:

def extract_unique_types()->set:
    """
    Extracts a set of unique reclaim types from the list of insurance reclaims.

    :return: A set containing all unique reclaim types.
    """
    types=set() #empty set
    for reclaim in reclaims:
        types.add(reclaim['type'])
    return types
#returns the reclaim(dict) that have the id given as argument
#Optional can take one value or None (here the one value is the dictionary, which is the reclaim)
def find_reclaim(id:int)->Optional[dict]:

    """
    Finds and returns a reclaim by its ID.

    :param id: The ID of the reclaim to find.
    :return: The reclaim dictionary if found, otherwise None.
    """
    i=0
    found=False
    while i<len(reclaims) and not found:
        if reclaims[i]['id']==id:
            found=True
        else:
            i+=1
    if not found:
        return None
    return reclaims[i]
#question 4:

def update_reclaim_status(id:int,new_status:str)-> None:
    """
    Updates the status of a specific insurance reclaim by its ID.

    :param id: The ID of the reclaim to update.
    :param new_status: The new status to assign to the reclaim (e.g., "approved", "pending", "rejected").
    :return: None. Prints a message if the reclaim with the given ID is not found.
    """
    reclaim=find_reclaim(id)
    if reclaim is None:
        print(f'There is no reclaim with the id {id}.')
    reclaim["status"]=new_status

#question 5:

def get_reclaims_by_status(status:str)->list[dict[str, Any]]:
#or
#def get_reclaims_by_status(status:str)->list[dict[str, int|str|float]]:
    
    """
    Filters the list of insurance reclaims by a given status.

    :param status: The status to filter reclaims by (e.g., "pending", "approved", "rejected").
    :return: A list of dictionaries containing reclaims with the specified status.
    """
    return [reclaim for reclaim in reclaims if reclaim["status"]==status]

def get_reclaims_by_status_v2(status:str)->list[dict[str, int|str|float]]:
    
    """
    Filters the list of insurance reclaims by a given status.

    :param status: The status to filter reclaims by (e.g., "pending", "approved", "rejected").
    :return: A list of dictionaries containing reclaims with the specified status.
    """

    status_reclaims=[]
    for reclaim in reclaims :
        if reclaim["status"]==status:
            status_reclaims.append(reclaim)
    return status_reclaims

#question 6:

def find_most_recent_reclaim()->Optional[dict[str,Any]]:
    """
    Finds the most recently submitted reclaim.

    :param reclamations: List of reclaims.
    :return: The most recent reclaim or None if the list is empty.
    """
    if not reclaims:
        return None
    return max(reclaims,key=lambda r: r["date"])

def find_most_recent_reclaim_v2()->Optional[dict[str,Any]]:
    """
    Finds the most recently submitted reclaim.

    :param reclamations: List of reclaims.
    :return: The most recent reclaim or None if the list is empty.
    """
    if not reclaims:
        return None
    sorted_reclaims=sorted(reclaims, key= lambda r : datetime.strptime(r["date"], '%Y-%m-%d'),reverse=True)
    return sorted[0]

#question 7:

def reclaims_by_type()->dict:
    """
    Counts the number of insurance reclaims for each type.

    :param reclaims: List of insurance reclaims, where each reclaim is a dictionary with a "type" key.
    :return: A dictionary with reclaim types as keys and their counts as values.
    """
    result={}
    for reclaim in reclaims:
        type=reclaim["type"]
        if  type in result.keys():
            result[type]+=1
        else:
            result[type]=1
    return result

#question 8:

def remove_reclaim(id:int)->None:
    reclaim=find_reclaim(id)
    if reclaim is None:
        print(f'There is no reclaim with the id {id}.')
    else:
        reclaims.remove(reclaim)
        print(f'The reclaim with id {id} have been successufly removed.')
    


#fonction main

def main():
    """
    Main function to interact with the insurance reclaims system.
    Provides a menu-based interface for various reclaim operations.
    """
    while True:
        print("\nInsurance Reclaims Management System")
        print("1. Create a new reclaim")
        print("2. View all reclaims")
        print("3. Evaluate total approved reclaims amount")
        print("4. Extract unique reclaim types")
        print("5. Find a reclaim by ID")
        print("6. Update reclaim status")
        print("7. Get reclaims by status")
        print("8. Find the most recent reclaim")
        print("9. Count reclaims by type")
        print("10. Remove a reclaim by ID")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_reclaim()
        elif choice == "2":
            print("\nAll reclaims:")
            for reclaim in reclaims:
                print(reclaim)
        elif choice == "3":
            total_approved = eval_approved_reclaims()
            print(f"\nTotal amount of approved reclaims: {total_approved} euros")
        elif choice == "4":
            unique_types = extract_unique_types()
            print(f"\nUnique reclaim types: {unique_types}")
        elif choice == "5":
            id_to_find = int(input("Enter the ID of the reclaim to find: "))
            reclaim = find_reclaim(id_to_find)
            if reclaim:
                print(f"\nFound reclaim: {reclaim}")
            else:
                print(f"No reclaim found with ID {id_to_find}")
        elif choice == "6":
            id_to_update = int(input("Enter the ID of the reclaim to update: "))
            new_status = input("Enter the new status (approved, pending, rejected): ")
            update_reclaim_status(id_to_update, new_status)
        elif choice == "7":
            status_to_filter = input("Enter the status to filter reclaims by: ")
            filtered_claims = get_reclaims_by_status(status_to_filter)
            print(f"\nClaims with status '{status_to_filter}':")
            for reclaim in filtered_claims:
                print(reclaim)
        elif choice == "8":
            most_recent = find_most_recent_reclaim()
            if most_recent:
                print(f"\nMost Recent reclaim: {most_recent}")
            else:
                print("No reclaims available.")
        elif choice == "9":
            counts_by_type = reclaims_by_type()
            print("\nNumber of reclaims by type:")
            for claim_type, count in counts_by_type.items():
                print(f"{claim_type}: {count}")
        elif choice ==10:
            id_to_remove = int(input("Enter the ID of the reclaim to remove: "))
            remove_reclaim(id_to_remove)
        elif choice == "0":
            print("Exiting the the application. Goodbye!")
            break
        else:
            print("Invalid choice.\nPlease try again.")

# Run the main function
if __name__ == "__main__":
    main()


#other version

def main():
    """
    Main function to interact with the insurance reclaims system using a switch-like approach.
    Provides a menu-based interface for various reclaim operations.
    """
    def menu_create_reclaim():
        create_reclaim()
    
    def menu_view_all_reclaims():
        print("\nAll reclaims:")
        for reclaim in reclaims:
            print(reclaim)
    
    def menu_eval_approved_reclaims():
        total_approved = eval_approved_reclaims()
        print(f"\nTotal amount of approved reclaims: {total_approved} euros")
    
    def menu_extract_unique_types():
        unique_types = extract_unique_types()
        print(f"\nUnique reclaim types: {unique_types}")
    
    def menu_find_reclaim():
        id_to_find = int(input("Enter the ID of the reclaim to find: "))
        reclaim = find_reclaim(id_to_find)
        if reclaim:
            print(f"\nFound reclaim: {reclaim}")
        else:
            print(f"No reclaim found with ID {id_to_find}")
    
    def menu_update_reclaim_status():
        id_to_update = int(input("Enter the ID of the reclaim to update: "))
        new_status = input("Enter the new status (approved, pending, rejected): ")
        update_reclaim_status(id_to_update, new_status)
    
    def menu_get_reclaims_by_status():
        status_to_filter = input("Enter the status to filter reclaims by: ")
        filtered_claims = get_reclaims_by_status(status_to_filter)
        print(f"\nClaims with status '{status_to_filter}':")
        for reclaim in filtered_claims:
            print(reclaim)
    
    def menu_find_most_recent_reclaim():
        most_recent = find_most_recent_reclaim()
        if most_recent:
            print(f"\nMost Recent reclaim: {most_recent}")
        else:
            print("No reclaims available.")
    
    def menu_reclaims_by_type():
        counts_by_type = reclaims_by_type()
        print("\nNumber of reclaims by type:")
        for claim_type, count in counts_by_type.items():
            print(f"{claim_type}: {count}")
    def menu_remove_reclaim():
        id_to_remove = int(input("Enter the ID of the reclaim to remove: "))
        remove_reclaim(id_to_remove)
    
    def menu_exit():
        print("Exiting the system. Goodbye!")
        exit()

    # Dictionary to simulate a switch statement
    menu_actions = {
        "1": menu_create_reclaim,
        "2": menu_view_all_reclaims,
        "3": menu_eval_approved_reclaims,
        "4": menu_extract_unique_types,
        "5": menu_find_reclaim,
        "6": menu_update_reclaim_status,
        "7": menu_get_reclaims_by_status,
        "8": menu_find_most_recent_reclaim,
        "9": menu_reclaims_by_type,
        "10": menu_remove_reclaim,
        "0": menu_exit,
    }

    while True:
        print("\nInsurance reclaims Management System")
        print("1. Create a new reclaim")
        print("2. View all reclaims")
        print("3. Evaluate total approved reclaims amount")
        print("4. Extract unique reclaim types")
        print("5. Find a reclaim by ID")
        print("6. Update reclaim status")
        print("7. Get reclaims by status")
        print("8. Find the most recent reclaim")
        print("9. Count reclaims by type")
        print("10. Remove a reclaim by ID")
        print("0. Exit")

        choice = input("Enter your choice: ")
        action = menu_actions.get(choice)
        #or
        #action = menu_actions[choice]


        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

