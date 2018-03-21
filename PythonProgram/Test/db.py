import json
import MySQLdb
from autotest.config.logger import Logging
logger=Logging()

class UpdateUtid():
    def __init__(self,merchant_name,user,password,host,database):
        self.merchant_name = merchant_name
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.utid = ""


    def open_conection(self):
        try:
            self.cnx =  MySQLdb.connect(self.host, self.user, self.password, self.database)
            self.cnx.autocommit(on=True)
            self.cursor = self.cnx.cursor()
        except:
            logger.debug("Error in connecting with database")
            exit(1)


    def get_utid(self):
        form_query = "select unipay_terminal_lookup.utid from merchant inner join chain_type on merchant.mer_id=chain_type.mer_id\
        inner join store on chain_type.chain_id=store.chain_id inner join unipay_terminal_lookup on chain_type.chain_id=unipay_terminal_lookup.chain_id \
        inner join cfg_bank_terminal on  unipay_terminal_lookup.utid=cfg_bank_terminal.utid where mer_name =" + self.merchant_name + "limit 1"";"


        query = (form_query)
        self.cursor.execute(query)
        result_set = self.cursor.fetchall()
        self.utid = result_set[0][0]

    def update_utid(self):
        with open('constants_auto.json', 'r+') as f:
            data = json.load(f)
            data['terminal']['tid'] = self.utid
            f.seek(0)
            json.dump(data, f, indent=4)



if __name__ == "__main__":
    utid = UpdateUtid("\'MerchantWithoutRule\'","qa","password","192.168.0.79","portal_configuration_new")
    utid.open_conection()
    utid.get_utid()
    utid.update_utid()

