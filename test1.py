import subprocess

# 1. Get input from the user first
user_data = input("Enter the text you want to process: ")

# 2. Pass it to the subprocess
# We use text=True so we can pass strings instead of bytes
result = subprocess.run(
    ['cat'], 
    input=user_data, 
    text=True, 
    capture_output=True
)

print("Subprocess output:", result.stdout)
