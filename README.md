# BuzzHire Exercise 2

The purpose of this exercice is to write an API to record and deliver events.

An event is an object with a start and end times, plus additional informations :
```
    {
        id: 243,
        start: "2016-20-01T10:00:00Z"
        end: "2016-20-01T15:00:00Z"
        label: "Event one"
        category: "blue"
    }
```
## Tests

Run the tests the usual way

```
python3 manage.py tests
```

## URLs

This Django module has the following URLs.

```
    GET /api/events/
```
Returns the list of events stored in the system.

```
    GET /api/events/:id/
```
Returns a particular event from the system given its ID

```
    POST /api/events/
```
Allows to create a new event, by specifying its start and end datetimes, 
plus any other information.

```
    /download/:id/
```
Downloads the particular event in ics format.