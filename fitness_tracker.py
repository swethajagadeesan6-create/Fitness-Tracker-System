import pandas as pd
import numpy as np

from ai_fitness import fitness_assistant


class FitnessTracker:

    def __init__(self):

        self.records = {}

        try:

            df = pd.read_excel("fitness_data.xlsx")

            for _, row in df.iterrows():

                self.records[str(row["Record ID"])] = {

                    "name": row["Name"],

                    "age": int(row["Age"]),

                    "activity": row["Activity"],

                    "duration": int(row["Duration"]),

                    "calories": int(row["Calories Burned"]),

                    "steps": int(row["Steps"])
                }

        except FileNotFoundError:

            pass


    # ADD FITNESS RECORD
    def add_record(self):

        record_id = input("Enter Record ID: ")

        if record_id in self.records:

            print("Record ID already exists!")

            return


        name = input("Enter Name: ")


        # AGE VALIDATION
        while True:

            try:

                age = int(input("Enter Age: "))

                if age <= 0:

                    print("Age must be greater than 0.")

                    continue

                break

            except ValueError:

                print("Invalid input! Please enter a valid age.")


        activity = input("Enter Activity: ")


        # DURATION VALIDATION
        while True:

            try:

                duration = int(
                    input("Enter Workout Duration (in minutes): ")
                )

                if duration <= 0:

                    print("Duration must be greater than 0.")

                    continue

                break

            except ValueError:

                print(
                    "Invalid input! Please enter a valid integer."
                )


        # CALORIES VALIDATION
        while True:

            try:

                calories = int(
                    input("Enter Calories Burned: ")
                )

                if calories < 0:

                    print("Calories cannot be negative.")

                    continue

                break

            except ValueError:

                print(
                    "Invalid input! Please enter a valid integer."
                )


        # STEPS VALIDATION
        while True:

            try:

                steps = int(
                    input("Enter Steps: ")
                )

                if steps < 0:

                    print("Steps cannot be negative.")

                    continue

                break

            except ValueError:

                print(
                    "Invalid input! Please enter a valid integer."
                )


        # STORE DATA
        self.records[record_id] = {

            "name": name,

            "age": age,

            "activity": activity,

            "duration": duration,

            "calories": calories,

            "steps": steps
        }


        self.export_to_excel()

        print("Fitness Record Added Successfully!")


    # VIEW ALL RECORDS
    def view_all_records(self):

        if not self.records:

            print("No fitness records found.")

            return


        for record_id, details in self.records.items():

            print("\nRecord ID:", record_id)

            print("Name:", details["name"])

            print("Age:", details["age"])

            print("Activity:", details["activity"])

            print(
                "Duration:",
                details["duration"],
                "minutes"
            )

            print(
                "Calories Burned:",
                details["calories"]
            )

            print(
                "Steps:",
                details["steps"]
            )


    # VIEW RECORD BY ID
    def view_record_by_id(self):

        record_id = input("Enter Record ID: ")


        if record_id not in self.records:

            print("Record not found!")

            return


        details = self.records[record_id]


        print("\n===== FITNESS RECORD =====")

        print("Record ID:", record_id)

        print("Name:", details["name"])

        print("Age:", details["age"])

        print("Activity:", details["activity"])

        print(
            "Duration:",
            details["duration"],
            "minutes"
        )

        print(
            "Calories Burned:",
            details["calories"]
        )

        print(
            "Steps:",
            details["steps"]
        )


    # UPDATE RECORD
    def update_record(self):

        record_id = input("Enter Record ID: ")


        if record_id not in self.records:

            print("Record not found!")

            return


        print("\n===== ENTER NEW DETAILS =====")


        name = input("Enter New Name: ")


        # AGE
        while True:

            try:

                age = int(
                    input("Enter New Age: ")
                )

                if age <= 0:

                    print("Age must be greater than 0.")

                    continue

                break

            except ValueError:

                print("Invalid input! Enter a valid age.")


        activity = input("Enter New Activity: ")


        # DURATION
        while True:

            try:

                duration = int(
                    input("Enter New Workout Duration: ")
                )

                if duration <= 0:

                    print("Duration must be greater than 0.")

                    continue

                break

            except ValueError:

                print("Invalid input! Enter a valid duration.")


        # CALORIES
        while True:

            try:

                calories = int(
                    input("Enter New Calories Burned: ")
                )

                if calories < 0:

                    print("Calories cannot be negative.")

                    continue

                break

            except ValueError:

                print("Invalid input! Enter valid calories.")


        # STEPS
        while True:

            try:

                steps = int(
                    input("Enter New Steps: ")
                )

                if steps < 0:

                    print("Steps cannot be negative.")

                    continue

                break

            except ValueError:

                print("Invalid input! Enter valid steps.")


        self.records[record_id] = {

            "name": name,

            "age": age,

            "activity": activity,

            "duration": duration,

            "calories": calories,

            "steps": steps
        }


        self.export_to_excel()

        print("Fitness Record Updated Successfully!")


    # DELETE RECORD
    def delete_record(self):

        record_id = input("Enter Record ID: ")


        if record_id not in self.records:

            print("Record not found!")

            return


        del self.records[record_id]


        self.export_to_excel()

        print("Fitness Record Deleted Successfully!")


    # EXPORT TO EXCEL
    def export_to_excel(self):

        data = []


        for record_id, details in self.records.items():

            data.append({

                "Record ID": record_id,

                "Name": details["name"],

                "Age": details["age"],

                "Activity": details["activity"],

                "Duration": details["duration"],

                "Calories Burned": details["calories"],

                "Steps": details["steps"]
            })


        df = pd.DataFrame(data)


        df.to_excel(
            "fitness_data.xlsx",
            index=False
        )


        print(
            "Data Exported Successfully to fitness_data.xlsx!"
        )


    # AVERAGE CALORIES
    def average_calories(self):

        if not self.records:

            print("No fitness records found.")

            return


        calories = []


        for details in self.records.values():

            calories.append(
                details["calories"]
            )


        arr = np.array(calories)


        average = np.mean(arr)


        print(
            "Average Calories Burned:",
            round(average, 2)
        )


    # MOST ACTIVE ACTIVITY
    def most_active_activity(self):

        if not self.records:

            print("No fitness records found.")

            return


        activities = []

        durations = []


        for details in self.records.values():

            activities.append(
                details["activity"]
            )

            durations.append(
                details["duration"]
            )


        unique_activities = np.unique(
            activities
        )


        activity_totals = []


        for activity in unique_activities:

            total = 0


            for i in range(len(activities)):

                if activities[i].lower() == activity.lower():

                    total += durations[i]


            activity_totals.append(total)


        arr = np.array(
            activity_totals
        )


        max_index = np.argmax(arr)


        print(
            "Most Active Activity:",
            unique_activities[max_index]
        )


        print(
            "Total Duration:",
            arr[max_index],
            "minutes"
        )


    # AI FITNESS ASSISTANT
    def ai_fitness_assistant(self):

        record_id = input(
            "Enter Record ID: "
        )


        if record_id not in self.records:

            print("Record not found!")

            return


        details = self.records[record_id]


        try:

            result = fitness_assistant(

                details["activity"],

                details["duration"],

                details["calories"]
            )


            print(
                "\n===== AI FITNESS ASSISTANT =====\n"
            )

            print(result)


        except Exception as e:

            print(
                "Unable to connect to AI Assistant."
            )

            print("Error:", e)


    # MENU
    def menu(self):

        while True:

            print(
                "\n===== FITNESS TRACKER ====="
            )

            print("1. Add Fitness Record")

            print("2. View All Records")

            print("3. View Record By ID")

            print("4. Update Record")

            print("5. Delete Record")

            print("6. Average Calories Burned")

            print("7. Most Active Activity")

            print("8. AI Fitness Assistant")

            print("9. Exit")


            choice = input(
                "\nEnter Choice (1-9): "
            )


            if choice == "1":

                self.add_record()


            elif choice == "2":

                self.view_all_records()


            elif choice == "3":

                self.view_record_by_id()


            elif choice == "4":

                self.update_record()


            elif choice == "5":

                self.delete_record()


            elif choice == "6":

                self.average_calories()


            elif choice == "7":

                self.most_active_activity()


            elif choice == "8":

                self.ai_fitness_assistant()


            elif choice == "9":

                print(
                    "Fitness Records Saved Successfully!"
                )

                print("Thank You!")

                break


            else:

                print(
                    "Invalid Choice! Please select 1 to 9."
                )