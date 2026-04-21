#!/usr/bin/env bash
set -u
export TORCH_DEVICE=cpu
MARKER=/home/rama/Desktop/0sci/marker-env/bin/marker_single
SRC_DIR=/home/rama/Desktop/0sci/chapter_pdfs
OUT_DIR=/home/rama/Desktop/0sci/chapters_md
LOG=/home/rama/Desktop/0sci/work/marker.log
mkdir -p "$OUT_DIR"

: > "$LOG"
echo "[$(date +%T)] starting marker batch; device=$TORCH_DEVICE" | tee -a "$LOG"

for pdf in "$SRC_DIR"/*.pdf; do
  name=$(basename "$pdf" .pdf)
  echo "[$(date +%T)] --- $name ---" | tee -a "$LOG"
  t0=$(date +%s)
  "$MARKER" "$pdf" \
      --output_format markdown \
      --output_dir "$OUT_DIR" \
      >> "$LOG" 2>&1
  rc=$?
  t1=$(date +%s)
  dur=$((t1-t0))
  if [ $rc -eq 0 ]; then
    echo "[$(date +%T)] ok  $name  ${dur}s" | tee -a "$LOG"
  else
    echo "[$(date +%T)] FAIL $name (rc=$rc) ${dur}s" | tee -a "$LOG"
  fi
done
echo "[$(date +%T)] batch done" | tee -a "$LOG"
