# Overview

The api_client is part of timesketch package and can be used to interact with the API of timesketch.

The examples listed will run against the demo page of timesketch.

# Authentication

It is always needed to first do authentication against your timesktch instance

Initializes the TimesketchApi object.

    Args:
        host_uri: URI to the Timesketch server (https://<server>/).
        username: User username.
        password: User password.
        verify: Verify server SSL certificate.
        auth_mode: The authentication mode to use. Defaults to 'timesketch'
            Supported values are 'timesketch' (Timesketch login form) and
            'http-basic' (HTTP Basic authentication).



## Example

```python
from api_client.python.timesketch_api_client.client import TimesketchApi

client = TimesketchApi(u'https://demo.timesketch.org', u'demo',u'demo')
```

# Sketch

## get

Get a sketch.

    Args:
        sketch_id: Primary key ID of the sketch.

    Returns:
        Instance of a Sketch object.

Example:

```python
client = TimesketchApi(u'https://demo.timesketch.org', u'demo',u'demo')
sketch = client.get_sketch(238)
print(sketch.name)

```
Will give you:
```
The Greendale incident - 2019
```

## create

Create a new sketch.

    Args:
        name: Name of the sketch.
        description: Description of the sketch.

    Returns:
        Instance of a Sketch object.

Example:
```python
from api_client.python.timesketch_api_client.client import TimesketchApi
from prettytable import PrettyTable

client = TimesketchApi(u'https://demo.timesketch.org',u'demo',u'demo')
client.create_sketch("This is a test")
sketches = client.list_sketches()
t = PrettyTable(['id', 'Name'])
for current_sketch in sketches:
    t.add_row([current_sketch.id, current_sketch.name])
print(t)
```

Will give you:
```
+-----+-------------------------------+
|  id |              Name             |
+-----+-------------------------------+
| 353 |         This is a test        |
| 285 |          MUSCTF 2019          |
| 238 | The Greendale incident - 2019 |
| 130 |      test1Untitled sketch     |
|  3  |  The Greendale investigation  |
+-----+-------------------------------+
```

## explore

To search in a sketch.

Example:
```python
client = TimesketchApi(u'https://demo.timesketch.org', u'demo',u'demo',verify=False)

from prettytable import PrettyTable
sketch = client.get_sketch(238)

search_results = sketch.explore("about.com")
t = PrettyTable(['datetime', 'message','labels','_id', "_index"])
for current_sketch in search_results['objects']:
        source = current_sketch.get('_source')
        t.add_row([source.get('datetime'), source.get('message'), ('[%s]' % ', '.join(map(str, source.get('label')))),current_sketch.get("_id"), current_sketch.get("_index")])
print(t)
```

Will give you
```
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+----------------------+----------------------------------+
|          datetime         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | labels |         _id          |              _index              |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+----------------------+----------------------------------+
| 1970-01-01T00:00:00+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Location: http://about.com/nl/us.htm?nl=fashion&e=bperry@student.greendale.xyz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   []   | AV1hg89zkUoaSru3tUSV | afe699a2219e49db91b781a490a2e7d8 |
| 1970-09-28T06:00:00+00:00 | Entry identifier: 673 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.pixel.parsely.com/plogger/?rand=1440504601135&idsite=about.com&url=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&urlref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&screen=1920x1037%7C1920x997%7C24&data=%7B%22parsely_uuid%22%3A%22398e74ae-8869-4200-8219-a3ad8e652d5c%22%2C%22parsely_site_uuid%22%3A%22599caa77-b3fc-42c1-8349-37fb13dd0ac3%22%7D&sid=1&surl=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&sref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&sts=1440504601130&slts=0&title=Importance+of+Feeding+Kitten+Food+to+Kittens&date=Tue+Aug+25+2015+12%3A10%3A01+GMT%2B0000+(Coordinated+Universal+Time)&action=pageview Access count: 1 Sync count: 0 Filename: plogger[1].gif Cached file size: 43 Response headers: HTTP/1.1 200 OKContent-Type: image/gifContent-Length: 43 |   []   | AV1hg89zkUoaSru3tUTF | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T11:10:01+00:00 |                                                                                                                                                                                                                                                                                                                                                            Entry identifier: 669 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.config.parsely.com/config/about.com Access count: 1 Sync count: 0 Filename: about[1].js Cached file size: 363 Response headers: HTTP/1.1 200 OKContent-Type: text/javascript; charset=utf-8ETag: W/"16b-JsNoVwE7NdU1wTDJ7xGghA"X-Powered-By: ExpressContent-Length: 363                                                                                                                                                                                                                                                                                                                                                            |   []   | AV1hje3ekUoaSru3vGnx | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:00+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                     [HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\LowRegistry\DOMStorage\about.com] (default): [REG_DWORD_LE] 63 NumberOfSubdomains: [REG_DWORD_LE] 1 Total: [REG_DWORD_LE] 191                                                                                                                                                                                                                                                                                                                                                                                                                                                      |   []   | AV1hjsNXkUoaSru3vRQk | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:01+00:00 |                                                                                                                                                                                                                                                                                                                                                            Entry identifier: 669 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.config.parsely.com/config/about.com Access count: 1 Sync count: 0 Filename: about[1].js Cached file size: 363 Response headers: HTTP/1.1 200 OKContent-Type: text/javascript; charset=utf-8ETag: W/"16b-JsNoVwE7NdU1wTDJ7xGghA"X-Powered-By: ExpressContent-Length: 363                                                                                                                                                                                                                                                                                                                                                            |   []   | AV1hjsi1kUoaSru3vRRc | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:01+00:00 |                                                                                                                                                                                                                                                                                                                                                            Entry identifier: 669 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.config.parsely.com/config/about.com Access count: 1 Sync count: 0 Filename: about[1].js Cached file size: 363 Response headers: HTTP/1.1 200 OKContent-Type: text/javascript; charset=utf-8ETag: W/"16b-JsNoVwE7NdU1wTDJ7xGghA"X-Powered-By: ExpressContent-Length: 363                                                                                                                                                                                                                                                                                                                                                            |   []   | AV1hjsi1kUoaSru3vRRd | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:01+00:00 | Entry identifier: 673 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.pixel.parsely.com/plogger/?rand=1440504601135&idsite=about.com&url=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&urlref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&screen=1920x1037%7C1920x997%7C24&data=%7B%22parsely_uuid%22%3A%22398e74ae-8869-4200-8219-a3ad8e652d5c%22%2C%22parsely_site_uuid%22%3A%22599caa77-b3fc-42c1-8349-37fb13dd0ac3%22%7D&sid=1&surl=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&sref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&sts=1440504601130&slts=0&title=Importance+of+Feeding+Kitten+Food+to+Kittens&date=Tue+Aug+25+2015+12%3A10%3A01+GMT%2B0000+(Coordinated+Universal+Time)&action=pageview Access count: 1 Sync count: 0 Filename: plogger[1].gif Cached file size: 43 Response headers: HTTP/1.1 200 OKContent-Type: image/gifContent-Length: 43 |   []   | AV1hjsi1kUoaSru3vRRn | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:01+00:00 | Entry identifier: 673 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.pixel.parsely.com/plogger/?rand=1440504601135&idsite=about.com&url=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&urlref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&screen=1920x1037%7C1920x997%7C24&data=%7B%22parsely_uuid%22%3A%22398e74ae-8869-4200-8219-a3ad8e652d5c%22%2C%22parsely_site_uuid%22%3A%22599caa77-b3fc-42c1-8349-37fb13dd0ac3%22%7D&sid=1&surl=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&sref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&sts=1440504601130&slts=0&title=Importance+of+Feeding+Kitten+Food+to+Kittens&date=Tue+Aug+25+2015+12%3A10%3A01+GMT%2B0000+(Coordinated+Universal+Time)&action=pageview Access count: 1 Sync count: 0 Filename: plogger[1].gif Cached file size: 43 Response headers: HTTP/1.1 200 OKContent-Type: image/gifContent-Length: 43 |   []   | AV1hjsi1kUoaSru3vRRm | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:01+00:00 |                                                                                                                                                                                                                                                                                                                                                            Entry identifier: 669 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.config.parsely.com/config/about.com Access count: 1 Sync count: 0 Filename: about[1].js Cached file size: 363 Response headers: HTTP/1.1 200 OKContent-Type: text/javascript; charset=utf-8ETag: W/"16b-JsNoVwE7NdU1wTDJ7xGghA"X-Powered-By: ExpressContent-Length: 363                                                                                                                                                                                                                                                                                                                                                            |   []   | AV1hjsi1kUoaSru3vRRe | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-25T12:10:01+00:00 | Entry identifier: 673 Container identifier: 16 Cache identifier: 0 URL: http://srv-2015-08-25-12.pixel.parsely.com/plogger/?rand=1440504601135&idsite=about.com&url=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&urlref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&screen=1920x1037%7C1920x997%7C24&data=%7B%22parsely_uuid%22%3A%22398e74ae-8869-4200-8219-a3ad8e652d5c%22%2C%22parsely_site_uuid%22%3A%22599caa77-b3fc-42c1-8349-37fb13dd0ac3%22%7D&sid=1&surl=http%3A%2F%2Fcats.about.com%2Fcs%2Fkittencare%2Fa%2Fkitten_food.htm&sref=http%3A%2F%2Fwebmail.student.greendale.xyz%2Fsrc%2Fread_body.php%3Fmailbox%3DINBOX%26passed_id%3D6%26startMessage%3D1&sts=1440504601130&slts=0&title=Importance+of+Feeding+Kitten+Food+to+Kittens&date=Tue+Aug+25+2015+12%3A10%3A01+GMT%2B0000+(Coordinated+Universal+Time)&action=pageview Access count: 1 Sync count: 0 Filename: plogger[1].gif Cached file size: 43 Response headers: HTTP/1.1 200 OKContent-Type: image/gifContent-Length: 43 |   []   | AV1hjsi1kUoaSru3vRRo | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T12:58:45+00:00 |                                                                                                                                                                                                                                                                                                              Entry identifier: 2307 Container identifier: 16 Cache identifier: 0 URL: http://about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyz Access count: 1 Sync count: 0 Filename: us[1].htm Cached file size: 203 Response headers: HTTP/1.1 301 Moved PermanentlyContent-Type: text/htmlTransfer-Encoding: chunkedKeep-Alive: timeout=15Location: http://www.about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyzP3P: CP="IDC DSP COR DEVa TAIa OUR BUS UNI"                                                                                                                                                                                                                                                                                                              |   []   | AV1hjwnQkUoaSru3vToM | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T12:58:45+00:00 |                                                                                                                                                                                                                                                                                                              Entry identifier: 2307 Container identifier: 16 Cache identifier: 0 URL: http://about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyz Access count: 1 Sync count: 0 Filename: us[1].htm Cached file size: 203 Response headers: HTTP/1.1 301 Moved PermanentlyContent-Type: text/htmlTransfer-Encoding: chunkedKeep-Alive: timeout=15Location: http://www.about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyzP3P: CP="IDC DSP COR DEVa TAIa OUR BUS UNI"                                                                                                                                                                                                                                                                                                              |   []   | AV1hjwnQkUoaSru3vToO | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T12:58:45+00:00 |                                                                                                                                                                                                                                                                                                              Entry identifier: 2307 Container identifier: 16 Cache identifier: 0 URL: http://about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyz Access count: 1 Sync count: 0 Filename: us[1].htm Cached file size: 203 Response headers: HTTP/1.1 301 Moved PermanentlyContent-Type: text/htmlTransfer-Encoding: chunkedKeep-Alive: timeout=15Location: http://www.about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyzP3P: CP="IDC DSP COR DEVa TAIa OUR BUS UNI"                                                                                                                                                                                                                                                                                                              |   []   | AV1hjwnQkUoaSru3vToL | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T13:04:23+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Entry identifier: 12 Container identifier: 3 Cache identifier: 0 URL: Cookie:bperry@about.com/ Access count: 38 Sync count: 0 Filename: YP8EE0GJ.txt Cached file size: 1613                                                                                                                                                                                                                                                                                                                                                                                                                                                           |   []   | AV1hjwnQkUoaSru3vTsM | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T13:04:23+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Entry identifier: 12 Container identifier: 3 Cache identifier: 0 URL: Cookie:bperry@about.com/ Access count: 38 Sync count: 0 Filename: YP8EE0GJ.txt Cached file size: 1613                                                                                                                                                                                                                                                                                                                                                                                                                                                           |   []   | AV1hjwnQkUoaSru3vTsS | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T13:04:23+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Entry identifier: 12 Container identifier: 3 Cache identifier: 0 URL: Cookie:bperry@about.com/ Access count: 38 Sync count: 0 Filename: YP8EE0GJ.txt Cached file size: 1613                                                                                                                                                                                                                                                                                                                                                                                                                                                           |   []   | AV1hjwnQkUoaSru3vTsR | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T13:04:23+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Entry identifier: 12 Container identifier: 3 Cache identifier: 0 URL: Cookie:bperry@about.com/ Access count: 38 Sync count: 0 Filename: YP8EE0GJ.txt Cached file size: 1613                                                                                                                                                                                                                                                                                                                                                                                                                                                           |   []   | AV1hjwnQkUoaSru3vTsT | afe699a2219e49db91b781a490a2e7d8 |
| 2015-08-29T13:58:45+00:00 |                                                                                                                                                                                                                                                                                                              Entry identifier: 2307 Container identifier: 16 Cache identifier: 0 URL: http://about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyz Access count: 1 Sync count: 0 Filename: us[1].htm Cached file size: 203 Response headers: HTTP/1.1 301 Moved PermanentlyContent-Type: text/htmlTransfer-Encoding: chunkedKeep-Alive: timeout=15Location: http://www.about.com/nl/us.htm?nl=cats&e=bperry@student.greendale.xyzP3P: CP="IDC DSP COR DEVa TAIa OUR BUS UNI"                                                                                                                                                                                                                                                                                                              |   []   | AV1hjzC9kUoaSru3vVJw | afe699a2219e49db91b781a490a2e7d8 |
| 2205-10-12T21:41:00+00:00 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Entry identifier: 12 Container identifier: 3 Cache identifier: 0 URL: Cookie:bperry@about.com/ Access count: 38 Sync count: 0 Filename: YP8EE0GJ.txt Cached file size: 1613                                                                                                                                                                                                                                                                                                                                                                                                                                                           |   []   | AV1hkew_kUoaSru3vpYu | afe699a2219e49db91b781a490a2e7d8 |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+----------------------+----------------------------------+


```

## list sketches

Get list of all open sketches that the user has access to.

    Returns:
        List of Sketch objects instances.

Example:

```python
client = TimesketchApi(u'https://demo.timesketch.org', u'demo',u'demo')
from prettytable import PrettyTable
sketches = client.list_sketches()
t = PrettyTable(['id', 'Name'])
for current_sketch in sketches:
    t.add_row([current_sketch.id, current_sketch.name])
print(t)
```

Will give you

```
+-----+-------------------------------+
|  id |              Name             |
+-----+-------------------------------+
| 285 |          MUSCTF 2019          |
| 238 | The Greendale incident - 2019 |
| 130 |      test1Untitled sketch     |
|  3  |  The Greendale investigation  |
+-----+-------------------------------+
```

## timelines

### get
```python
sketch = client.get_sketch(238)
print(sketch.name)
timelines_in_sketch = sketch.list_timelines()
t = PrettyTable(['id', 'Name'])
for current_timeline in timelines_in_sketch:
        t.add_row([current_timeline.id, current_timeline.name])
print(t)
```

will give you:
```
The Greendale incident - 2019
+-----+-------------+
|  id |     Name    |
+-----+-------------+
| 189 |  registrar  |
| 190 | student-pc1 |
| 198 |     dc1     |
+-----+-------------+
```

## searchindex

### get

Get a searchindex.

    Args:
        searchindex_id: Primary key ID of the searchindex.

    Returns:
        Instance of a SearchIndex object.

Example:

```python
from api_client.python.timesketch_api_client.client import TimesketchApi
from prettytable import PrettyTable

client = TimesketchApi(u'https://demo.timesketch.org',u'demo',u'demo')
search_index = client.get_searchindex(22)

t = PrettyTable(['id','name'])
t.add_row([search_index.id,search_index.name])

print(t)
```

Will give you:
```
+----+-------------+
| id |     name    |
+----+-------------+
| 22 | MUSCTF-2019 |
+----+-------------+
```

### get_or_create

Create a new searchindex.

    Args:
        searchindex_name: Name of the searchindex in Timesketch.
        es_index_name: Name of the index in Elasticsearch.
        public: Boolean indicating if the searchindex should be public.

    Returns:
        Instance of a SearchIndex object and a boolean indicating if the
        object was created.

Example:

### list

```python
from api_client.python.timesketch_api_client.client import TimesketchApi
from prettytable import PrettyTable

client = TimesketchApi(u'https://demo.timesketch.org',u'demo',u'demo')
search_indices = client.list_searchindices()

t = PrettyTable(['id','name'])
for current_search_index in search_indices:
    t.add_row([current_search_index.id,current_search_index.name])

print(t)
```

will give you
```
+----+-------------+
| id |     name    |
+----+-------------+
| 18 |     test    |
| 2  |     dc1     |
| 1  | student-pc1 |
| 3  |  registrar  |
| 22 | MUSCTF-2019 |
+----+-------------+
```

# views

Views are always defined per sketch.

## list
List all saved views for this sketch.

    Returns:
        List of views (instances of View objects)

Example:
```python
from api_client.python.timesketch_api_client.client import TimesketchApi
from prettytable import PrettyTable

client = TimesketchApi(u'https://demo.timesketch.org',u'demo',u'demo')
sketch = client.get_sketch(238)
views = sketch.list_views()

t = PrettyTable(['id','name'])
for current_view in views:
    t.add_row([current_view.id,current_view.name])

print(t)

```

Will give you:
```
+------+---------------------------------------------------+
|  id  |                        name                       |
+------+---------------------------------------------------+
| 2012 |  [phishy_domains] Phishy Domains, excl. whitelist |
| 2010 |          [browser_search] Browser Search          |
| 2011 |          [phishy_domains] Phishy Domains          |
| 2035 |               Windows network logins              |
| 2616 |                       Antti                       |
| 2185 |                  This is the view                 |
| 2214 |                 Windows Link Files                |
| 2213 |               Windows network logins              |
| 2293 |                         hh                        |
| 2344 |                        test                       |
| 2855 |               Windows network logins              |
| 2212 |               Windows network logins              |
| 2601 | An operation was attempted on a privileged object |
| 2603 | An operation was attempted on a privileged object |
| 2605 | An operation was attempted on a privileged object |
| 2602 | An operation was attempted on a privileged object |
| 2604 | An operation was attempted on a privileged object |
+------+---------------------------------------------------+

```
    
