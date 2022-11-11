# Fee Calculator  

Fee Calculator is a microservice that calculates the fee to transport a package to the desired destination.  
The microservice is written in Python.  
The service is addressable via remote procedure calls (RPC), more specifically gRPC.

## Requirements  

Make sure you have **Python 3.5**, but preferably the latest version, installed.  
For the package manager is **pip 9.0.1** or higher required.

## Run the microservice  

Virtual environments are used to manage dependencies for projects in Python, they are independent groups of Python libraries.  
This helps manage packages and their version to ensure compatibility and isolation.  


### Virtual environment  

#### Creation  

```
cd my_project  
python -m venv venv  
```

#### Activation  

##### Windows  

```
.\venv\Scripts\activate  
```

##### Unix  

```
./venv/bin/activate  
```

### Dependencies  

The depedencies are listed in requirements.txt and can be installed in the virtual environment using the following command:  

```
pip install -r requirements.txt  
```

### Run the server  

To run the server and start using it, execute the Python file:  

```
server.py 
```

## Client  

When creating a client to consume the microservice it is important to make use of the same Protocol Buffers.  
These can be found in the protobufs directory.  

For testing and demonstration purposes a Python implemtation for a client has been provided.  
To run the client, execute the Python file.  

```
client.py
```
