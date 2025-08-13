- app.py is the webserver.
- We assume the agent has run and we have produce a list of thing to post.
- we are assuming the agent has produced a list for things to post:
```json
[
  {
    "submission_url": "https://www.reddit.com/r/example/comments/12345/",
    "comment_to_place": "This is the first comment to be posted. It's insightful and adds value."
  },
  {
    "submission_url": "https://www.reddit.com/r/another/comments/67890/",
    "comment_to_place": "Here is a second comment. It is also very helpful."
  },
  {
    "submission_url": "https://www.reddit.com/r/testing/comments/abcde/",
    "comment_to_place": "And a third one for good measure."
  }
]
```
This will be in queue, lets call it `queue.json`
