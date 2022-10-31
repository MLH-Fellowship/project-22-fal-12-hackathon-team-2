#!/bin/bash

curl --request GET http://localhost:5234/api/timeline_post

curl --request POST http://localhost:5234/api/timeline_post -d 'name=Alexis&email=alexis.gray623@gmail.com&content=Just Added Database to my portfolio site!'

curl http://localhost:5234/api/timeline_post