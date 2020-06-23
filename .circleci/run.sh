#!/usr/bin/env bash
curl --user c7c8d2532707aaec6f686eaab4fc833883caa548: \
    --request POST \
    --form config=@config.yml \
    --form notify=false \
        https://circleci.com/api/v1.1/project/github/deepan10/jxctl/tree/develop

    # --form revision=<commit hash>\