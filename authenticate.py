import win32security

def isValid(username, password):

    try:
        token = win32security.LogonUser(username, 'springfield.loval', password,
                                        win32security.LOGON32_LOGON_NETWORK, win32security.LOGON32_PROVIDER_DEFAULT)
        
        return bool(token)

    except: 
        return False


username = input("Enter your Active Directory Username: ")
password = input("Enter the password for the account: ")

loggedInUser = username if isValid(username, password) else ""

if loggedInUser != "":
    print("Here are the Springfield Trade Secrets: ")
else:
    print("Springfield Trade Secrets are for residents of Springfield only.")