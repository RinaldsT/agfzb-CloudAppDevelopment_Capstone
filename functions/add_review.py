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
        client = Cloudant.iam("6f6ac427-e3b6-4d64-b356-7f445fe09768-bluemix", "kKPkmJ1jBgL15LjjFZflXHkmiBnINmEBsy3rRuaWfupD", connect=True)
        dbs = client.all_dbs()
        reviewdb = client[dbs[1]]

        new_document = reviewdb.create_document(params['review'])
        
        print(dbs)
        
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}
        
    return {"review": new_document}
  