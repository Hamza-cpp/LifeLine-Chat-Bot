import os
import shutil

ENV_EXAMPLE = ".env.example"
ENV_FILE = ".env"

def create_env_file():
    """Create the .env file from the .env.example template and prompt the user to fill in the values."""
    if os.path.exists(ENV_FILE):
        print(f"{ENV_FILE} already exists.")
        return

    if not os.path.exists(ENV_EXAMPLE):
        print(f"Error: {ENV_EXAMPLE} does not exist.")
        return

    shutil.copyfile(ENV_EXAMPLE, ENV_FILE)
    print(f"{ENV_FILE} has been created from {ENV_EXAMPLE}. Please provide the necessary values.")

    with open(ENV_FILE, "r") as f:
        lines = f.readlines()

    with open(ENV_FILE, "w") as f:
        for line in lines:
            if "TWILIO_ACCOUNT_SID" in line:
                value = input("Enter your Twilio Account SID: ")
                line = f"TWILIO_ACCOUNT_SID={value}\n"
            elif "TWILIO_AUTH_TOKEN" in line:
                value = input("Enter your Twilio Auth Token: ")
                line = f"TWILIO_AUTH_TOKEN={value}\n"
            f.write(line)

    print(f"{ENV_FILE} has been updated with your values.")

if __name__ == "__main__":
    create_env_file()