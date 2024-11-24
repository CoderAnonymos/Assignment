# Input the total number of school days
total_days = int(input("Enter the total number of school days: "))

# Input the number of days attended
days_attended = int(input("Enter the number of days attended: "))

# Calculate the number of days missed
days_missed = total_days - days_attended

# Ensure the inputs are valid
if days_attended > total_days or days_attended < 0:
    print("Invalid input. Days attended cannot exceed total days or be negative.")
else:
    # Calculate the attendance percentage
    attendance_percentage = (days_attended / total_days) * 100

    # Set the eligibility threshold
    threshold = 75

    # Display the results
    print(f"Total Days: {total_days}")
    print(f"Days Attended: {days_attended}")
    print(f"Days Missed: {days_missed}")
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    # Check eligibility
    if attendance_percentage >= threshold:
        print("Eligible for exam!")
    else:
        print("Not eligible for exam.")
