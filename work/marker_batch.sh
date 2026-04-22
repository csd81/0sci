#!/usr/bin/env bash
set -u
cd /home/rama/Desktop/0sci
source marker-env/bin/activate
export TORCH_DEVICE=cpu

BATCH_LOG=work/marker_batch.log
: > "$BATCH_LOG"

# Wait for the currently-running ch4 marker to finish (if any)
echo "[$(date +%F\ %T)] waiting for existing marker process to finish…" | tee -a "$BATCH_LOG"
while pgrep -fx "/home/rama/Desktop/0sci/marker-env/bin/python3 /home/rama/Desktop/0sci/marker-env/bin/marker_single chapter_pdfs/04-eigenvalue-problems.pdf --output_format markdown --output_dir chapters_md" >/dev/null 2>&1; do
  sleep 60
done
echo "[$(date +%F\ %T)] ch4 marker done, starting batch 05-13" | tee -a "$BATCH_LOG"

for num in 05 06 07 08 09 10 11 12 13; do
  pdf=$(ls chapter_pdfs/${num}-*.pdf 2>/dev/null | head -1)
  if [ -z "$pdf" ]; then
    echo "[$(date +%F\ %T)] SKIP: no PDF for chapter ${num}" | tee -a "$BATCH_LOG"
    continue
  fi
  chlog=work/marker_ch${num}.log
  echo "[$(date +%F\ %T)] starting ch${num}: $pdf" | tee -a "$BATCH_LOG"
  : > "$chlog"
  echo "[$(date +%F\ %T)] starting ch${num}" >> "$chlog"
  marker_single "$pdf" --output_format markdown --output_dir chapters_md >> "$chlog" 2>&1
  rc=$?
  echo "[$(date +%F\ %T)] finished ch${num} (rc=$rc)" | tee -a "$BATCH_LOG"
  echo "[$(date +%F\ %T)] done ch${num} (rc=$rc)" >> "$chlog"
done
echo "[$(date +%F\ %T)] batch complete (chapters 05-13)" | tee -a "$BATCH_LOG"
