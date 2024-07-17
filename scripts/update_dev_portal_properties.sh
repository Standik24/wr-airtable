#!/usr/bin/env bash

set -e

# Update properties in Keboola Developer Portal

echo "Updating config schema"
value=`cat configuration_schema.json`
echo "$value"
if [ ! -z "$value" ]
then
    /code/bin/cli update-app-property ${KBC_DEVELOPERPORTAL_VENDOR} ${KBC_DEVELOPERPORTAL_APP} configurationSchema --value="$value"
else
    echo "configurationSchema is empty!"
fi



