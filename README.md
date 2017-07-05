# keyword-mining-ui
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

UI of the keyword mining tool https://github.com/AnthonySigogne/keyword-mining

## DEMO
A demo can be found here : http://keywordmining.byprog.com/  

## INSTALL AND RUN

### REQUIREMENTS
This tool requires *Python3+* and the keyword mining API (see link above).

### WITH PIP
```
git clone https://github.com/AnthonySigogne/keyword-mining-ui.git
cd keyword-mining-ui
pip install -r requirements.txt
```

Then, run the tool :
```
FLASK_APP=index.py HOST=<ip> PORT=<port> flask run --port 80
```
Where :
* `ip` + `port` : route to keyword mining API

To run in debug mode, prepend `FLASK_DEBUG=1` to the command :
```
FLASK_DEBUG=1 ... flask run --port 80
```

### WITH DOCKER
To run the tool with Docker, you can use my DockerHub image :
https://hub.docker.com/r/anthonysigogne/keyword-mining-ui/
```
docker run -p 80:5000 \
-e "HOST=<ip>" \
-e "PORT=<port>" \
anthonysigogne/keyword-mining-ui
```
Where :
* `ip` + `port` : route to keyword mining API

Or, build yourself a Docker image :
```
git clone https://github.com/AnthonySigogne/keyword-mining-ui.git
cd keyword-mining-ui
docker build -t keyword-mining-ui .
```

## USAGE AND EXAMPLES
To use the keyword mining tool, just type this endpoint in your web browser : http://localhost/

![Keyword mining tool](images/keyword-mining.png?raw=true "Keyword Mining tool" )

## LICENCE
MIT
