# Florida Gulf Coast Guide

Guy Golan's monthly web edition (one guide, published monthly). Plain HTML and CSS, so the site can be opened directly or hosted later on GitHub Pages. GitHub Pages is not turned on. Nothing here is published until a reviewed pull request is merged.

The first issue is the October 2026 edition (Oct 23, 2026). It follows the approved v8 print design: navy plates, gold rules, Cinzel headings, a gold page frame, one star fixed at the top center of interior pages, gold-bordered photos, and a zigzag photo layout on the feature pages.

## Preview

Open `index.html` in a browser, or from this folder run:

```bash
python3 -m http.server
```

Then visit the local address it prints. Check a narrow window (phone) and a wide one (desktop). Each issue is one scrolling page of magazine plates.

## Layout

```
index.html                  Front door: latest issue and the archive
css/guide.css               Shared styles for every issue
fonts/                      Cinzel and Gelasio (SIL Open Font License)
assets/a_wordmark.png       Wordmark used on the front door
issues/2026-10-23/          This month's issue
  index.html
  images/                   Only the photos this issue actually uses
tools/build_v8.py           Designer's print generator, kept for reference
tools/magazine_layout_notes.md
tools/weekly_guide_2026-10-23_v8.html
```

`tools/build_v8.py` is the script that produced the approved print file. It is not the web publisher, and it still expects the old print paths. Build each web issue by copying the previous month's HTML.

## Add next month's issue

1. Copy `issues/2026-10-23` to `issues/YYYY-MM-DD`.
2. In the new `images/` folder, keep photos you are reusing (the wordmark and headshot usually stay) and replace the story photos. Use only real photos supplied for that month. Do not add stock or AI images. If a photo is not ready, leave a labeled placeholder the way the happy-hour page does.
3. Edit `issues/YYYY-MM-DD/index.html`. Change the date, issue number, sections, charts, and source lines. Keep the plate structure:
   - Double gold frame and corner marks on every plate.
   - One gold star, top center, on interior plates only. The cover has no frame star, because the star already lives in the wordmark.
   - Photos get a gold border and stay inside the frame, with space between the photo and the frame. Nothing bleeds to the frame or the page edge.
   - Feature stories (community focus, social minute) stay open: drop cap, captions, no box around the body. Alternate which side the large photo sits on from one feature to the next.
   - Data pages keep the gold outline panels for rates, tables, hours, and prices.
   - Leave gold tags on anything still unverified (`Data pending`, `Confirm before print`, `Guy to write`).
4. Edit the root `index.html`. Point the latest-issue date, summary, cover photos, and "Read this issue" link at the new folder. Add a new row at the top of the archive list.
5. Read it at phone width and desktop width. Confirm the star is still top center, the wordmark is the only star on the cover, and no photo crosses the gold frame.
6. Commit on a branch and open a pull request. Do not enable GitHub Pages, and do not merge to `main`, until Guy has reviewed it.

The pages send `noindex` while the issue is still a draft. Remove that meta tag when an issue is actually meant to be public.

## Brand notes from the approved v8 file

The print file uses interior navy `#001B35`, cover navy `#0E1F41`, and gold `#D4AF37`. Those are the colors on the plates. Cinzel is used for headings, kickers, labels, and big numbers. Gelasio is the body text. Both fonts are licensed under the SIL Open Font License; see `fonts/OFL-Cinzel.txt` and `fonts/OFL-Gelasio.txt`.
