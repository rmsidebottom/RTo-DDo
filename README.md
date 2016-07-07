# aws-flask-agenda
Simple RESTful service developed using Python's flask to keep track of my assignments/tasks.

### Overview

This is a simple project I am working on to learn a little bit more about web and also use AWS 
for more than my personal website. The end result of this will be on AWS and I will include the
guide I used for that at the end of this. Feel free to use this yourself as it is a really cool 
and fun way to have an agenda. Also feel free to edit this and make it better because who doesn't
love better services???

The basic functionality of this will be to store assignments in an AWS database. The API will 
require sign in but will allow the user to add, view, modify, and delete assignments. Assignments
marked as complete or finished will be deleted. Each assignment will contain some brief 
information describing it so that the user can return at a later date and understand exactly 
what needs to be done. A sample assignment will look like this:

```python
assignment = {
	'id': 1,
	'source': 'math',
	'details': 'problems 2, 3, 4 p 390',
	'start': '7/7',
	'end': '7/9',
	'done': 'false'
}
```

In the sample assignment it is easy to determine where the assignment came from (`source`), 
what the actual assignment is (`details`), when the assignment was handed out (`start`), when
it is due (`end`), and whether it is complete or not (`done`). The `id` field is used for 
referencing since it allows the user to input one character to delete or finish an assignment.


### Resources
[Setting up RESTful API with flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

