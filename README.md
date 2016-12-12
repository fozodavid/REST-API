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

## Features

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

## Recommendations

This assignment includes several tasks, you can go as far as you can/like,
the amount of code won't be a criterion of evaluation. It is advised not
to spend more than 2 hours in total.

You must use Python to write your response, as well as any framework or tool 
of your choice. Using libraries to simplify the work is highly encouraged.
If you do so, please include a README with explanation. 
You can return your code directly by email, hosted on a repository, 
or deploy it using Heroku or any similar platform.Tasks

## 1. API basics

You will have to write the code to handle storage of the objects in the
database of your choice.

## 2. Additional feature

Create an additional endpoint to export an event at ICS format.

The ICS file should be returned as a downloadable attachment, and valid for 
import in any calendar software.

## 3. Going further

If you have time, feel free to improve the API and add more features :

* Write tests ;
* Proper validation of the new event posting (datetime format), make some 
* fields optional ;
* Prevent creation of new events overlapping existing ones ;
* Endpoint to modify or delete an event ;
* Filters events using a querystring parameter ;
* etc.
