#!/bin/bash

set -eo pipefail

UA="github.com/mattbillenstein/horse/dl.sh"

D="2025-12-30"
TODAY="$(date +'%Y-%m-%d')"

while true; do
  if [ ! -e puzzles/${D}.json ]; then
    echo "Fetching $D ..."
    curl -s --header "User-Agent: $UA" https://enclose.horse/api/daily/$D | jq -r > puzzles/$D.json
  fi

  if [ $D == $TODAY ]; then
    break
  fi

  D=$(date -d "$D + 1 day" +"%Y-%m-%d")
done
