# Jumble-api

Api server built in Python takes a word and re-arranges the characters randomly.

## Getting Started

These instructions will cover usage information and for build the docker container

## Prerequisities

In order to run this container you'll need docker installed.

- [Windows](https://docs.docker.com/windows/started)
- [OS X](https://docs.docker.com/mac/started/)
- [Linux](https://docs.docker.com/linux/started/)

## Build

To build the container, clone this repo

```bash
docker build -t <container_name>:<tag> app/.
```

## Run

```bash
docker run -d -p 80:80 --name my-container <container_name>:<tag>
```

This will start the FastAPI application in a Docker container, mapping port 80 on the host machine to port 80 in the container. You can then access the "jumble" API endpoint at <http://localhost/jumble>, and the "audit" API endpoint at <http://localhost/audit>.

### Persist data

You can persist the database mapping the `api_calls.db` as a [volume](https://docs.docker.com/storage/volumes/).

```bash
touch $(pwd)/api_calls.db
nerdctl run --rm -p 8080:80 -v "$(pwd)/api_calls.db:/app/api_calls.db" --name <some_name> <container_name>:<tag>
```

### Environment Variables

The container can be configured using the following environment variables:

| Variable       | Description                                      | Default      |
| -------------- | ------------------------------------------------ | ------------ |
| `DB_PATH`      | Set the full path and file name for sqlite3 data | api_calls.db |
| `MAX_CALLS`    | Maximun number of calls to be stored             | 100          |
| `RETURN_LIMIT` | Number of api calls return by `audit`            | 10           |
| `AUTH_TOKEN`   | Authorization token to access endpoints          | mysecretkey  |

## Usage

### Authentication

All endpoints are protected by a Bearer token set durig startup. and all resquest need to include the http header `-H "Authorization: Bearer <token_value>"

### Jumble Words

This is the main container entrypoint. It takes any word or string and re-arranges the characters randomly with an json output.
Reqtests need to be done in `json` format, wit the key par `word:value`

```bash
curl -X POST -H "Content-Type: application/json" http://localhost/jumble -d '{"word":"magic"}' -H "Authorization: Bearer <token>"
```

### Audit

Returns the last calls made to the server.

- What API was called.
- What payload was given.

Number of request returned can be controlled by envireomnt variable `RETURN_LIMIT` or by http query `?limit=`.

```bash
curl -s "http://127.0.0.1/audit?limit=50"
```

<!-- ## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us. -->

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the
[tags on this repository](https://github.com/your/repository/tags).

## Author

- **Marcos Rocha** - _Initial work_ - [mmurilo](https://github.com/mmurilo)

See also the list of [contributors](https://github.com/mmurilo/scramble-words/contributors) who
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](../LICENSE.md) file for details.
