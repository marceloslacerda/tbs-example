#!/usr/bin/env sh
json_output=True

service="https://picsum.photos/200/300/?image=935"

data=$(wget -q "$service" -O - | base64 -w 0)
echo '{"type": "image", "content": "'"$data"'"}'