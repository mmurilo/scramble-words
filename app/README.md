# Randomize

## Build

```bash
docker build -t my-fastapi-app .
```

## test

```bash
docker run -d -p 80:80 --name my-container my-fastapi-app
```

This will start the FastAPI application in a Docker container, mapping port 80 on the host machine to port 80 in the container. You can then access the "jumble" API endpoint at <http://localhost/jumble>, and the "audit" API endpoint at <http://localhost/audit>.

```bash
nerdctl run --rm -p 8080:80 -v "$(pwd)/api_calls.db:/app/api_calls.db" --name test-api jumble:0.0.2
```

```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/jumble -d '{"word":"folha"}'
```


curl -s "http://127.0.0.1:8080/audit?limit=50" |jq '.api_calls | length'

nerdctl run --rm -p 8080:80 -v "$(pwd)/api_calls.db:/app/api_calls.db" -e MAX_CALLS=100 -e RETURN_LIMIT=6 --name test-api jumble:0.0.3