#!/usr/bin/env bash
curl --user 81304b67631759c78b65b4c073bb179f9c165eb3: \
    --request POST \
    --form config=@config.yml \
    --form notify=false \
        https://circleci.com/api/v1.1/project/github/deepan10/jxctl/tree/develop

    # --form revision=<commit hash>\