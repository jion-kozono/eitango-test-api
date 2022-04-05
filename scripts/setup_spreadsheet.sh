#!/bin/sh

touch client_secret.json

SECRETS_JSON=$(cat <<-END
  {
		"type": "service_account",
		"project_id": "$PROJECT_ID",
		"private_key_id": "$PRIVATE_KEY_ID",
		"private_key": "$PRIVATE_KEY",
		"client_email": "$CLIENT_EMAIL",
		"client_id": "$CLIENT_ID",
		"auth_uri": "https://accounts.google.com/o/oauth2/auth",
		"token_uri": "https://oauth2.googleapis.com/token",
		"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
		"client_x509_cert_url": "$CLIENT_X599_CERT_URL"
	}
END
)

echo $SECRETS_JSON > client_secret.json