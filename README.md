# Jumble Words API

## Application

API server built in Python that takes a word and re-arranges the characters randomly

[`app/`](app/)

- [Build](app/README.md#build)
- [Run](app/README.md#run)
- [Usage](app/README.md#usage)

## Deployemnt

Installation instructions for running [application](#application) on Kubernetes

[`deploy/`](deploy/)

- [Helm](deploy/charts/jumble-api/README.md)
- [Manifests](deploy/manifests/README.md)

## Basic Usage

to scramble a word:

```bash
curl -X POST -H "Content-Type: application/json" http://127.0.0.1/jumble -d '{"word":"<some_word>"}' -H "Authorization: Bearer <token>"
```

To get the last api requests:

```bash
curl -s "http://127.0.0.1/audit"
```

More detalaid usage and configuration [here](app/README.md)

## Author

- **Marcos Rocha** - _Initial work_ - [mmurilo](https://github.com/mmurilo)

See also the list of [contributors](https://github.com/mmurilo/scramble-words/contributors) who
participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
