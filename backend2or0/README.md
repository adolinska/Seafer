# pcss' app

#### How to run this app. 
To deploy the app, execute this command in root directory of this project:

`sudo docker compose up --build`




#### How it works?
Every single connection to this app, is registering in database, and it's saving a date (day, month, year) and hours and IP address of client.

This app require a Content-Type in header, in another case you will not see response of this server.

#### You can test this app by curl:

text/html:   
`curl -X POST -H "Content-Type: text/html" http://172.28.0.22:5000/`

text/yaml:   
`curl -X POST -H "Content-Type: text/yaml" http://172.28.0.22:5000/`

text/xml:   
`curl -X POST -H "Content-Type: text/xml" http://172.28.0.22:5000/`

text/xml (with send file as content): 
`curl -X POST -H "Content-Type: text/xml" -d @xmltest.xml http://172.28.0.22:5000/`

text/plain:   
`curl -X POST -H "Content-Type: text/plain" http://172.28.0.22:5000/`

You can list all address of client by open this address in your browser:   
`http://172.28.0.22:5000/list`

