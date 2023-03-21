## Author: Lucas Scheffel

## API Overview
This REST API works with graphs and its edges in JSON data format, providing basic CRUD functionalities and other features such as:
  - Get all the routes from a source to a target, considering the sent parameters, through the use of a search method (BFS)
  - Get the minimum distance between two points in the graph

## Content
  - API (In Progress).
  - API Dockerfile (Done).
  - Docker-compose with all the necessary services (Done).
  - Automated tests (In Progress).

## Functional specifications
### Create Graph
* Endpoint: `http://localhost:8000/graph`
* HTTP Method: POST
* HTTP Success Response Code: CREATED (201)

This endpoint receives the following data (fields) of a graph and saves it to an SQLite database:
  - Description of the graph
  - The graphs' edges

# Edge JSON representation:
```javascript
{​
  "source": "A",
  "target": "B",
  "distance": 5
}​
```

# Endpoint Contract:
  * Request payload:
```javascript
{
  "description": "Example",
  "data": [
    {
      "source": "A", 
      "target": "B", 
      "distance": 6
    },
    {
      "source": "A", 
      "target": "E", 
      "distance": 4
    },
    {
      "source": "B", 
      "target": "A", 
      "distance": 6
    },
    {
      "source": "B", 
      "target": "C", 
      "distance": 2
    },
    {
      "source": "B", 
      "target": "D", 
      "distance": 4
    },
    {
      "source": "C", 
      "target": "B", 
      "distance": 3
    },
    {
      "source": "C", 
      "target": "D",
      "distance": 1
    },
    {
      "source": "C", 
      "target": "E", 
      "distance": 7
    },
    {
      "source": "D", 
      "target": "B", 
      "distance": 8
    },
    {
      "source": "E", 
      "target": "B", 
      "distance": 5
    },
    {
      "source": "E", 
      "target": "D", 
      "distance": 7
    }
  ]
}​
```

  * Response payload:
```javascript
{​
  "id" : 1,
  "description": "Example",
  "data":[
    {​
      "source": "A", "target": "B", "distance":6
    }​,
    {​
      "source": "A", "target": "E", "distance":4
    }​,
    {​
      "source": "B", "target": "A", "distance":6
    }​,
    {​
      "source": "B", "target": "C", "distance":2
    }​,
    {​
      "source": "B", "target": "D", "distance":4
    }​,
    {​
      "source": "C", "target": "B", "distance":3
    }​,
    {​
      "source": "C", "target": "D", "distance":1
    }​,
    {​
      "source": "C", "target": "E", "distance":7
    }​,
    {​
      "source": "D", "target": "B", "distance":8
    }​,
    {​
      "source": "E",  "target": "B", "distance":5
    }​,
    {​
      "source": "E", "target": "D", "distance":7
    }​
  ]
}​
```

### Retrieve Graph
* Endpoint: `http://localhost:8000/graph/<graphId>`
* HTTP Method: GET
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)

This endpoint returns a graph previously created in the database. If the graph doesn't exist, returns a HTTP NOT FOUND status.

# Contract:
  * Response payload:
```javascript
{​
  "id" : 1,
  "description": "Example",
  "data":[
    {​
      "source": "A", "target": "B", "distance": 6
    }​,
    {​
      "source": "A", "target": "E", "distance": 4
    }​,
    {​
      "source": "B", "target": "A", "distance": 6
    }​,
    {​
      "source": "B", "target": "C", "distance": 2
    }​,
    {​
      "source": "B", "target": "D", "distance": 4
    }​,
    {​
      "source": "C", "target": "B", "distance": 3
    }​,
    {​
      "source": "C", "target": "D", "distance": 1
    }​,
    {​
      "source": "C", "target": "E", "distance": 7
    }​,
    {​
      "source": "D", "target": "B", "distance": 8
    }​,
    {​
      "source": "E", "target": "B", "distance": 5
    }​,
    {​
      "source": "E", "target": "D", "distance": 7
    }​
  ]
}​
```

### List Graphs
* Endpoint: `http://localhost:8000/graph/`
* HTTP Method: GET
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)

This endpoint returns all the graphs in the database considering the given parameters which include:
  - pageSize: The number of graphs per page
  - page: The number of the desired page
  - description: A string contained in the description field of the graph

# Contract:
  * Response payload:
```javascript
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {​
      "id" : 1,
      "description": "Example",
      "data": [
        {​
          "source": "A", "target": "B", "distance": 6
        }​,
        {​
          "source": "A", "target": "E", "distance": 4
        }​,
        {​
          "source": "B", "target": "A", "distance": 6
        }​,
        {​
          "source": "B", "target": "C", "distance": 2
        }​,
        {​
          "source": "B", "target": "D", "distance": 4
        }​,
        {​
          "source": "C", "target": "B", "distance": 3
        }​,
        {​
          "source": "C", "target": "D", "distance": 1
        }​,
        {​
          "source": "C", "target": "E", "distance": 7
        }​,
        {​
          "source": "D", "target": "B", "distance": 8
        }​,
        {​
          "source": "E", "target": "B", "distance": 5
        }​,
        {​
          "source": "E", "target": "D", "distance": 7
        }​
      ]
    }
  ]
}
```

### Update Graph
* Endpoint: `http://localhost:8000/graph/<graphId>`
* HTTP Method: PUT
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)

# Contract:
  * Request payload:
```javascript 
{
  "description": "Updated Description"
}
```

  * Response payload:
```javascript
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {​
      "id" : 1,
      "description": "Updated Description",
      "data": [
        {​
          "source": "A", "target": "B", "distance": 6
        }​,
        {​
          "source": "A", "target": "E", "distance": 4
        }​,
        {​
          "source": "B", "target": "A", "distance": 6
        }​,
        {​
          "source": "B", "target": "C", "distance": 2
        }​,
        {​
          "source": "B", "target": "D", "distance": 4
        }​,
        {​
          "source": "C", "target": "B", "distance": 3
        }​,
        {​
          "source": "C", "target": "D", "distance": 1
        }​,
        {​
          "source": "C", "target": "E", "distance": 7
        }​,
        {​
          "source": "D", "target": "B", "distance": 8
        }​,
        {​
          "source": "E", "target": "B", "distance": 5
        }​,
        {​
          "source": "E", "target": "D", "distance": 7
        }​
      ]
    }
  ]
}
```

### Remove Graph
* Endpoint: `http://localhost:8000/graph/<graphId>`
* HTTP Method: DELETE
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)

### Find all routes from a source city to a target city in a previously created graph
This endpoint finds all the possible routes from one city to another, considering a given number of maximum stops. If there are no possible routes, it returns an empty list. If the "maxStops" parameter is not sent, all the possible routes will be returned. If the graph doesn't exist, returns HTTP NOT FOUND.
Example: Considering graph (AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7), the possible routes from "A" to "C" with "maxStops" = 3 would be: ["ABC", "ADC", "AEBC"]

* Endpoint: `http://localhost:8080/routes/<graphId>/from/<town1>/to/<town2>?maxStops=<maxStops>`
* HTTP Method: GET
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)
* Contract:
  * Response payload:
```javascript
{​
  "routes": [
    {​
      "route": "ABC",
      "stops": 2
    }​,
    {​
      "route": "ADC",
      "stops": 2
    }​,
    {​
      "route": "AEBC",
      "stops": 3
    }​
  ]
}​
```

### Find the minimal distance between two cities in the graph
This endpoint calculates the shortest possible route between two cities. If both the source and target are equal, the result is going to be 0. If there are no routes connecting the two cities, then the result will be -1. If the graph doesn't exist, returns HTTP NOT FOUND.

* Endpoint: `http://localhost:8080/distance/<graphId>/from/<town1>/to/<town2>`
* HTTP Method: GET
* HTTP Success Response Code: OK (200)
* HTTP Error Response Code: NOT FOUND (404)
* Contract:
  * Response payload:
```javascript
{​
  "distance" : 8,
  "path" : ["A", "B", "C"]
}​
```

## Author: Lucas Scheffel
