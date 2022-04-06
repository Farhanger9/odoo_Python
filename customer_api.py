import xmlrpc.client as xmlrpclib
import psycopg2
import csv
from datetime import date, datetime
 

def main():
    server = ''
    db = ''
    port = ''
    user = ''
    password = ''
     
    serv_str = 'http://' + str(server) + ':' + str(port) + '/xmlrpc/2/object'
    sock = xmlrpclib.ServerProxy(serv_str)
    lst=[]
    tag_id = sock.execute_kw(str(db), 2
                    , str(password)
                    , 'res.partner.category'
                    , 'search',
                    [[['name', '=', 'prospect']]], {'limit': 1})
    print("tag_id,,,,,,,,", tag_id)
    
    partner_id = sock.execute_kw(str(db), 2
                    , str(password)
                    , 'res.partner'
                    , 'search_read',
                    [[['create_date', '>=', '2021-01-31 23:59:59'], ['tag_ids', '=', tag_id[0]]]],
                     {'fields': ['name'], 'limit': 5})
    print("partner_id,,,,,,,,,,", partner_id)
    
if __name__ == '__main__':
    main()
