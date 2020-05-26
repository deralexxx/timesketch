# Timesketch API

## API client

Timesketch has a dedicated API client that can be installed with
```
pip install timesketch-api-client
```

## Modifying the API client

To modify the API client e.g. introducing new methods or improving already
existing methods, change the files under:
```
/api_client
```

## Interaction with ElasticSearch

Timesketch is built on top of ElasticSearch (ES),
the ES APi is encapsulted by the Timesketch API.
That means not every ES API endpoint is available in TS API and or TS api-client.

And attempt to access an ES API endpoint without using the TS API will most
likely end with an HTTP Error message:

```
[405] METHOD NOT ALLOWED The method is not allowed for the requested URL
``` 

### Introducing new TS API routes

To tackle that, a new route is needed in the TS API.
The code for that is at:
```
/timesketch/api
```


