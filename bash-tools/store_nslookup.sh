#!/bin/bash

while true; do
    echo "Enter domain (or 'quit' to exit):"
    read domain

    [ "$domain" = "quit" ] && break 

    if [ -z "$domain" ]; then
        echo "Please enter a domain first."
    else
        echo "=== $(date) | $domain ===" >> recon_log.txt
		nslookup "$domain" >> recon_log.txt
        echo "Recon complete for: $domain"
    fi
done

echo "Goodbye. Results saved to recon_log.txt"