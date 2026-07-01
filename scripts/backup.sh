#!/bin/bash
set -e

BACKUP_DIR="$HOME/backups"
TIMESTAMP=$(date +%F_%H-%M-%S)

mkdir -p "$BACKUP_DIR"

docker compose exec -T postgres \
pg_dump -U postgres appdb \
> "$BACKUP_DIR/appdb_$TIMESTAMP.sql"

echo "✅ Backup created: $BACKUP_DIR/appdb_$TIMESTAMP.sql"
