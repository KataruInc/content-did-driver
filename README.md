# content-did-driver

## Build & Run
```shell
$ docker build -t content-did-resolver .
$ docker run -p 8888:8888 content-did-resolver
```

## Testing 
```shell
$ cd src
$ pip install -r requirements.txt
$ python app.py 
and 
$ curl localhost:8888/1.0/identifiers/did:content:3SqTXtoMpiPeNo5vEP2p7yNGQUeCGjqW1wnctv8yaCWXojD29GYcUEo | jq
{
  "didDocument": {
    "context": [
      "https://www.w3.org/ns/did/v1",
      "https://did.kataru.io/did/v1",
      "https://w3id.org/security/suites/secp256k1recovery-2020/v2"
    ],
    "controller": [
      "did:key:z6MkvHhk3Zcw1du2wZritamA4WbM4AgkeRaM6EQhMHVn1Wtw#author"
    ],
    "id": "did:content:3SqTXtoMpiPeNo5vEP2p7yNGQUeCGjqW1wnctv8yaCWXojD29GYcUEo",
    "proof": {},
    "service": [
      {
        "id": "#kataru",
        "serviceEndpoint": "https://kataru.io/content/did:content:3SqTXtoMpiPeNo5vEP2p7yNGQUeCGjqW1wnctv8yaCWXojD29GYcUEo",
        "type": "kataru"
      }
    ],
    "verificationMethod": [
      {
        "controller": "did:key:z6MkvHhk3Zcw1du2wZritamA4WbM4AgkeRaM6EQhMHVn1Wtw",
        "id": "did:key:z6MkvHhk3Zcw1du2wZritamA4WbM4AgkeRaM6EQhMHVn1Wtw#controller",
        "type": "Ed25519VerificationKey2020"
      }
    ]
  }
}
```