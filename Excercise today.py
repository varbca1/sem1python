print("1. Enter Marks")
print("2. Calculate Total Marks")
print("3. Calculate Percentage")
print("4. Exit")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject{i + 1}: "))
        marks.append(mark)
    print("Entered marks: ", marks)
elif choice == "2":
     total = sum(marks)
     print("Total Marks: ", total)         