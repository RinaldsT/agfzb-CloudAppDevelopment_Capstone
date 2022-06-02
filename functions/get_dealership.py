#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
def main(params):
    try:
        client = Cloudant.iam(params['USER'], params['API'], connect=True)
        dbs = client.all_dbs()
        dealerdb = client[dbs[0]]
        dealerlist = []
        stid = (params['state'])
        for dealer in dealerdb:
            if dealer['st'] == stid:
                dealerlist.append(dealer)

        print(dbs)
        
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}
    
    return {"Output": dealerlist}