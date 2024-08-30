import argparse, requests, dotenv, os
from dotenv import load_dotenv

dotenv_path = os.path.expanduser("~/Porky-api/.env")
load_dotenv(dotenv_path)
apiKey = os.getenv("apikey")
secretKey = os.getenv("secretkey")

class PorkbunAPIHelper:
    def __init__(self):
        self.apikey = apiKey
        self.secretapikey = secretKey
        self.api = PorkbunAPI(self.apikey, self.secretapikey)

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Porkbun API Command-Line Interface")
        parser.add_argument('--domain', required=True, help='Domain name to operate on')
        parser.add_argument('--type', required=True, help='DNS record type (e.g., A, TXT, CNAME)')
        parser.add_argument('--value', required=True, help='DNS record value (e.g., IP address, text value)')
        parser.add_argument('--name', default="", help='Optional subdomain name (e.g., www)')

        return parser.parse_args()

    def execute(self, args):
        domain = args.domain
        record_type = args.type
        value = args.value
        name = args.name

        dns_record = self.api.create_dns_record(domain, record_type, value, name=name)
        print(f"Create DNS Record for {domain}: {dns_record}")

        dns_records = self.api.list_dns_records(domain)
        print(f"DNS Records for {domain}: {dns_records}")
class PorkbunAPI:
    def __init__(self, apikey, secretapikey):
        self.apikey = apikey
        self.secretapikey = secretapikey
        self.base_url = "https://porkbun.com/api/json/v3"
        self.headers = {"Content-Type": "application/json"}

    def _post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def create_dns_record(self, domain, record_type, value, name=""):
        data = {
            "apikey": self.apikey,
            "secretapikey": self.secretapikey,
            "name": name,
            "type": record_type,
            "content": value,
            "ttl": 600,
        }
        return self._post(f"dns/create/{domain}", data)

    def list_dns_records(self, domain):
        data = {
            "apikey": self.apikey,
            "secretapikey": self.secretapikey,
        }
        return self._post(f"dns/retrieve/{domain}", data)

    def delete_dns_record(self, domain, record_id):
        data = {
            "apikey": self.apikey,
            "secretapikey": self.secretapikey,
            "id": record_id,
        }
        return self._post(f"dns/delete/{domain}", data)

def main():
    helper = PorkbunAPIHelper()
    args = helper.parse_args()
    helper.execute(args)


if __name__ == "__main__":
    main()

