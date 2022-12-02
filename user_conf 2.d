server {
    listen 80;
    server_name ag-22-mlh-portfolio.duckdns.org;

    if ($host = ag-22-mlh-portfolio.duckdns.org) {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name ag-22-mlh-portfolio.duckdns.org;

    location / {
        proxy_pass http://myportfolio:5000/;
    }

    ssl_certificate /etc/letsencrypt/live/myportfolio/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myportfolio/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/myportfolio/chain.pem;
}