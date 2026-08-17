print("LAB 14: STRUCTURED OUTPUT GENERATION")
print("=" * 40)

print("\nPROMPT:")
print("Generate Python code to find the largest number in a list.")

print("\nGENERATED PYTHON CODE:")
print("""
numbers = [10, 25, 7, 40, 15]

largest = max(numbers)

print("Largest number:", largest)
""")

numbers = [10, 25, 7, 40, 15]
largest = max(numbers)

print("OUTPUT:")
print("Largest number:", largest)


print("\nSQL QUERY GENERATION")

print("Prompt:")
print("Generate SQL query to find students having marks greater than 80.")

print("\nGenerated SQL:")
print("""
SELECT id, name, marks
FROM Students
WHERE marks > 80;
""")
