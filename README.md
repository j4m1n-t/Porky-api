# Porky-API

This Python script provides a command-line interface (CLI) for interacting with the [Porkbun](https://www.porkbun.com) DNS [API](https://porkbun.com/api/json/v3/documentation). It allows you to create, list, and delete DNS records for a specified domain.

### Requirements
* Python 3.x
* requests library
* python-dotenv library

### Setup
1. Clone the repository.
        
        git clone https://github.com/j4m1n-t/porky-api.git
        cd porky-api
2. Install the dependencies
   
        pip install -r requirements.txt
3. Create new `.env` file in the project directory with your Porkbun API credentials. The file should look like this:

        apikey = your_api_key
        secretkey = your_secret_key
4. Update the path to the `.env` file in `porky-api.py` if necessary. By default, it is set to: 

        dotenv_path = os.path.expanduser("~/.porkbun/.env")

### Usage

To use the CLI tool, run the script with the following arguments:

    --domain: The domain name to operate on (e.g., example.com)
    --type: The DNS record type (e.g., A, TXT, CNAME)
    --value: The DNS record value (e.g., IP address, text value)
    --name: Optional subdomain name (e.g., www)

### Create DNS Record

To create a DNS record, use the following command:

        python porky-api.py --domain example.com --type A 
        --value 192.0.2.1 --name www

### List DNS Records

The script automatically lists all DNS records for the domain after creating a new record.

### Delete DNS Record

To delete a DNS record, you can add a method in the PorkbunAPIHelper class for handling deletion and adjust the execute method accordingly.

### Code Overview

* `PorkbunAPIHelper`: Handles command-line argument parsing and calls the Porkbun API.
* `PorkbunAPI`: Manages API requests to Porkbun for creating, listing, and deleting DNS records.
* `main()`: Entry point of the script that initializes PorkbunAPIHelper, parses arguments, and executes the operations.

### License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/j4m1n-t/Porky-api/blob/main/LICENSE) file for details.

### Contact

For any questions or issues, please contact Jamin Thompson at j.thompson@j4m1n.me.

---