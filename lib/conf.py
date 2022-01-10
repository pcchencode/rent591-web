import os
import json

class AWS_db_credential(object):
    def __init__(self, env=None):
        try:
            self.env_path = os.environ['E_PATH']
        except:
            self.env_path = os.getcwd()+'/lib/db_config.cfg' # export E_PATH="~/cred/db_config.cfg"
        print(os.getcwd())
        print(self.env_path)
        with open(self.env_path, 'r' ) as f:
            data = f.read()
            self.env_parameter = json.loads(data)
        
        self.host_name = self.env_parameter['host_name']
        self.user_name = self.env_parameter['user_name']
        self.password = self.env_parameter['password']
        self.port = self.env_parameter['port']
        self.db_name = self.env_parameter['db_name']

# a = AWS_db_credential()
# print(a.env_path)
# print(a.env_parameter)
# print(a.host_name)