# Maintaining the cover gallery

The source of the gallery is `manifest.json` plus the cropped images in `covers/`. Full phone screenshots are intentionally excluded.

For a new publication, add its cover and a manifest entry with the exact repository-relative PDF path. Use `status: "available"` only after checking the title and volume against that PDF. Use `missing` for an advertised publication without a confirmed PDF; reference graphics use `reference-image`. Do not link a missing book to a related title. If the PDF has a redesigned cover, verify the title and volume and add a note.

Run `python3 "00. find pdf/render_gallery.py"` from the repository root to rebuild the gallery README and unavailable-title list together. The renderer uses only the Python standard library. Keep three cells per row and wrap available cover images in links to their exact PDFs. Validate every image path, PDF link, and missing-item anchor before committing. Keep collection counts out of the root README.
