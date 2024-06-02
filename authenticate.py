import win32security
import getpass
import logging

def isValid(username, domain, password):
    try:
        token = win32security.LogonUser(username, domain, password,
                                        win32security.LOGON32_LOGON_NETWORK, win32security.LOGON32_PROVIDER_DEFAULT)
        return bool(token)
    except Exception as e:
        logging.error(f"Authentication failed for user {username}: {e}")
        return False

def main():
    domain = input("Enter your domain: ")
    username = input("Enter your Active Directory Username: ")
    password = getpass.getpass("Enter the password for the account: ")

    loggedInUser = username if isValid(username, domain, password) else ""

    if loggedInUser:
        print("User Authentication Success")
    else:
        print(f"There was an error authenticating '{username}'. Please try again.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
