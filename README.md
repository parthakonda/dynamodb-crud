# dynamodb-crud
Dynamo DB crud operations modules using boto3 and pynamodb


This is to demostration usage of pynamodb. The example is realtime (feeding notifications)


# Analysis

It is very to easy to just create the records. However, you need to understand the following things to design dynamodb table according to your needs.

## `scan()` vs `query()`

`scan()` will search through all records, which is heavy if you've large number of rows
`query()` you can query using hash_key(either indexes hash key)

## Pagination

In order to make use of the data for rest apis or for any other purpose where you'll be needing this pagination.
dynamod db does not provide pagination. However, only forward pagintion is possible by default.

### How?

```
results = Notification.query('UNREAD', limit=5)
print(results.last_evaluated_key) # Output: None
response = [item.attribute_values for item in results]

#
# Note: response.last_evaluated_key will be `None` if you access it before iterating the results.
#
last_evaluated_key = response.last_evaluated_key
print(last_evaluated_key) # Output: {'<hash_key>: {'<type>': '<value>'}, '<sort_key>': {'<type>': '<value>'}}
```

`response` is holding first 5 results of unsorted data.

And you can get next 5 elements by doing following

```
results = Notification.query('UNREAD', limit=5, last_evaluated_key=last_evaluated_key)
response = [item.attribute_values for item in results]
```

`response` is holding next 5 results of unsorted data.


## Searching
Searching is straight forwarded thing. You can do conditional search and multiple conditions also possible.

### How?
```
results = Notification.query('UNREAD', Notification.from_user == 'parthasaradhi1992@gmail.com', limit=5)
```


## Sorting
There you go. Sorting use case is common. Here you need to understand about Indexes. There are two types of indexes

1. Global Secondary Index
2. Local Secondary Index

I struggled lot of time to understand the above. But this link https://dzone.com/articles/indexing-in-dynamodb is very helpful to understand them.

So, sorting is required when you want to query the data accross the partitions. For this, you need to create a `Global Secondary Index` with your desired attributes (other than base table keys and keys are which are required to be searchable)

To create a Global Secondary Index you need to give `hash_key` and also `sort_key or range_key` can be provided. And the sorting(asc/desc) will be performed on the given `sort_key or range_key`.

## `save()` vs `update()`
`save()` will entirely put a new object.
`update()` will updated only the specified attribute.


Will keep update the analysis.