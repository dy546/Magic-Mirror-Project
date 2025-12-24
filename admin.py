import json
import os

DATA_FILE = "company_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"global": {"alerts": []}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ System Updated Successfully!")

def main():
    while True:
        data = load_data()
        print("\n--- MAGIC MIRROR ADMIN PANEL ---")
        print("1. Add Global Announcement")
        print("2. Assign Task to User")
        print("3. Send Direct Alert to User")
        print("4. Clear All Data for a User")
        print("5. Exit")
        
        choice = input("Select option: ")

        if choice == "1":
            msg = input("Enter Announcement: ")
            if "global" not in data: data["global"] = {"alerts": []}
            data["global"]["alerts"].append(msg)
            save_data(data)

        elif choice == "2":
            user = input("Enter Username (e.g., ELON): ").upper()
            task = input("Enter Task: ")
            
            if user not in data: data[user] = {"alerts": [], "tasks": []}
            if "tasks" not in data[user]: data[user]["tasks"] = []
            
            data[user]["tasks"].append(task)
            save_data(data)

        elif choice == "3":
            user = input("Enter Username (e.g., ELON): ").upper()
            alert = input("Enter Urgent Message: ")
            
            if user not in data: data[user] = {"alerts": [], "tasks": []}
            if "alerts" not in data[user]: data[user]["alerts"] = []
            
            data[user]["alerts"].append(alert)
            save_data(data)

        elif choice == "4":
            user = input("Enter Username to CLEAR: ").upper()
            if user in data:
                data[user] = {"alerts": [], "tasks": []}
                save_data(data)
            else:
                print("User not found.")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()