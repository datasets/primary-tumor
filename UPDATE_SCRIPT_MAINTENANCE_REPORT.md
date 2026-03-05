## Update Script Maintenance Report

Date: 2026-03-04

- Ran updater: `python scripts/main.py`.
- Root cause: source retrieval intermittently failed with upstream HTTP errors.
- Fixes made:
  - Added source fallback order (OpenML primary, UCI fallback) in updater.
  - Added first monthly + manual workflow with `contents: write`.
- Validation summary: updater runs successfully after fallback hardening and refreshes `data/primary-tumor.csv`.
