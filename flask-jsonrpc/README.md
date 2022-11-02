# Fee Calculator  

Fee Calculator is a microservice that calculates the fee to transport a package to the desired destination.  
The microservice is written in Python and makes use of the micro web framework Flask.  
The service is addressable via remote procedure calls (RPC) over HTTP, more specifically JSON-RPC.

## Requirements  

Make sure you have **Python 3.7**, but preferably the latest version, installed.  

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

### Run the project  

To run the project and start using it, issue the following command:  

```
flask run  
```
