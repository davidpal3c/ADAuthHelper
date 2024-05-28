from ldap3 import Server, Connection, ALL
import logging
import getpass

def queryLDAP(server, bindUser, bindPassword, query):
    serverObj = Server(server, get_info=ALL)
    
    try:
        with Connection(serverObj, bindUser, bindPassword, auto_bind=True) as conn:
            conn.search('dc=springfield,dc=local', query)
            return conn.entries
    except Exception as e:
        logging.error(f"LDAP query failed: {e}")
        return []

def checkMembership(server, bindUser, bindPassword, username, group):
    user_filter = f'(&(objectclass=user)(sAMAccountName={username}))'
    users = queryLDAP(server, bindUser, bindPassword, user_filter)
    if not users:
        logging.info(f'User {username} does not exist')
        return False 

    user_dn = users[0].entry_dn

    group_filter = f'(&(objectclass=group)(cn={group}))'
    groups = queryLDAP(server, bindUser, bindPassword, group_filter)
    if not groups:
        logging.info(f'Group {group} does not exist')
        return False

    group_dn = groups[0].entry_dn

    membership_filter = f'(&(objectclass=group)(member={user_dn}))'
    group_membership = queryLDAP(server, bindUser, bindPassword, membership_filter)

    for entry in group_membership:
        if entry.entry_dn == group_dn:
            return True  
    
    return False  

def main():
    server = input("Enter LDAP server (e.g., dc0.springfield.local): ")
    bindUser = input("Enter LDAP bind user (e.g., CN=Student,CN=Users,DC=springfield,DC=local): ")
    bindPassword = getpass.getpass("Enter LDAP bind password: ")
    
    username = input("Enter Active Directory Username: ")
    group = input("Enter its Group: ")
    
    result = checkMembership(server, bindUser, bindPassword, username, group)

    if result:
        print(f"{username} is a member of {group}")
    else:
        print(f"{username} is NOT a member of {group}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()