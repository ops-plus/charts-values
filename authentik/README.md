# authentik

```bash
# Run the following command in the folder where main.py is located
helm repo add authentik https://charts.goauthentik.io
helm repo update
# edit you .env file
python main.py render authentik
helm upgrade --install authentik authentik/authentik -f values/authentik/values.yaml
```
