


# Active Directory Auth script

Tool for authenticating users and checking group memberships in an Active Directory environment using LDAP and Win32 libraries.

## Features
- User authentication against Active Directory
- LDAP queries for user and group information
- Configurable via JSON configuration file

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ADAuthManager.git
    cd ADAuthManager
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create and edit the configuration file:
    ```sh
    cp config.json.example config.json
    # Edit config.json to match your environment
    ```

## Usage

Run the main script:
```sh
python main.py




Configuration

Update the config.json file with your domain, LDAP server, bind user, and password.
License

This project is licensed under the MIT License.

