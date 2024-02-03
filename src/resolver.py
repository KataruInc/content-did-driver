
from error import UnsupportedDID, InvalidDID, Internal
import requests

didMethod = 'content'
endpoint = 'https://api-stg.kataru.io/kataru.v1.DIDContentPublicService/ResolveDIDDoc'

def resolve(did):
  splitDID = did.split(':')
  if len(splitDID) != 3:
    raise InvalidDID()
  if splitDID[1] != didMethod:
    raise UnsupportedDID()
  
  resp = requests.post(endpoint, json={"did":did})
  if resp.status_code == 200:
    return resp.json()
  else:
    raise Internal()
