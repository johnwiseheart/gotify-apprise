# gotify-apprise

A tool to forward messages from Gotify to Apprise! This allows notification exfiltration for tools which are only set up to send to Gotify, such as Proxmox.

## Getting started

### Create an Apprise Config

Create an [Apprise config file](https://github.com/caronc/apprise/wiki/config) for use with the tool. You can customize many aspects of the apprise config, including the assets.

The file should be called `apprise.yaml` - its location can either be configured using the `APPRISE_CONFIG` environment variable, or using docker volume mounts.

Example:

```yaml
version: 1

asset:
  app_id: Gotify
  app_desc: Notifications forwarded from Gotify
  app_url: http://gotify.myserver.com

urls:
  - discord://<webhook_id>/<webhook_token>/?format=markdown
```

### Run the forwarding server

Either build and run yourself, or use it as a docker image. To provide config, you can pass environment variables:

- `GOTIFY_HOST` is the `IP[:PORT]` of your Gotify server.
- `GOTIFY_TOKEN` is a token created from the `client` section of Gotify.
- `APPRISE_CONFIG` (optional) is a file path to your [Apprise config file](https://github.com/caronc/apprise/wiki/config) if you wish to change the path from its default. This can be helpful if you're not using the docker image.

Using `docker compose`:

```yaml
version: "3"
services:
  gotify-apprise:
    image: ghcr.io/johnwiseheart/gotify-apprise:latest
    container_name: gotify-apprise
    environment:
      - GOTIFY_HOST=<hostname>
      - GOTIFY_TOKEN=<token>
    volumes:
      - ./config:/config
    restart: unless-stopped
```

## Build it yourself

Pretty typical python package. Use a virtual environment, install dependencies, and then run `proxy.py`, ensuring that the required environment variables are provided.
