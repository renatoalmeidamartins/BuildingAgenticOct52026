from bedrock_agentcore.services.identity import IdentityClient

identity_client = IdentityClient("us-east-1")

github_provider = identity_client.create_oauth2_credential_provider({
    "name": "github-provider",
    "credentialProviderVendor": "GithubOauth2",
    "oauth2ProviderConfigInput": {
        "githubOauth2ProviderConfig": {
            "clientId": "your-github-client-id",
            "clientSecret": "your-github-client-secret"
        }
    }
})
