# http-server
Simple Http Server

## How to initiate de server
```
$ python main.py
```

### Optional arguments
--dir=/ # absolute path

--port=8080

--secure=yes

### How to create a self-signed PEM file
```
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
```

### How to create a PEM file from existing certificate files that form a chain
(optional) Remove the password from the Private Key by following the steps listed below:
```
$ openssl rsa -in server.key -out nopassword.key
```
Note: Enter the pass phrase of the Private Key.

### Combine the private key, public certificate and any 3rd party intermediate certificate files:
```
$ cat nopassword.key > server.pem
$ cat server.crt >> server.pem
```

Note: Repeat this step as needed for third-party certificate chain files, bundles, etc:
```
$ cat intermediate.crt >> server.pem
```