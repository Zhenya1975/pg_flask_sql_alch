#!/bin/bash
# rm -r migrations
# flask db init
flask db migrate -m 'init'
flask db upgrade
