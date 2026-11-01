# Spectrum Plain HTML & CSS Website (`plain-html/`)

A 100% pure, framework-free implementation of the **Spectrum IT Solutions Ltd.** website. Built with native HTML5, CSS3, and standard Bootstrap styling matching the original site's layout, colors, and structure.

---

## Zero Framework & Zero Dependencies
- No Node.js, React, Next.js, or build tools required.
- Double-click any `.html` file or deploy directly to any web server (cPanel, Apache, Nginx, or GitHub Pages).

---

## Fixes & Updates Implemented

1. **Digital Identity Priority (#1 at first):**
   - In [`services.html`](services.html): **Digital Identity & Security** is displayed as Card #1 at the top-left of the services grid.
   - In [`projects.html`](projects.html): **TCB Smart Family Card (Digital Identity)** is displayed as Project #1 at the top-left.
   - In [`dis.html`](dis.html): Added the **"Upokari"** sub-service block with a `Coming Soon` badge, ready for the upcoming content.

2. **Case Studies in Main Menu Bar:**
   - Added **Case Studies** as a standard navigation item across all pages:
     `About Us` | `Services` | `Products` | `Projects` | `Case Studies` | `Contact`
   - In [`case-study.html`](case-study.html): Fixed the previous incorrect title and replaced duplicate products with real enterprise case studies (TCB Smart Family Card, Industrial e-Court BD, National e-Licensing, OCD Portal).

3. **Responsive Bug Fixes (No Layout or Color Changes):**
   - [`assets/css/responsive-fixes.css`](assets/css/responsive-fixes.css): Eliminates the 400px header padding horizontal overflow on laptops and optimizes mobile header height.
   - Fixed mobile menu tap sizing.

4. **Contact Form Fixed:**
   - In [`contact.html`](contact.html): Replaced the non-functional `<a>` tag with `<button type="submit">`, changed phone input to `type="tel"` (preserving `+880`), and added a submission confirmation notice.

5. **Header & Footer Polish:**
   - Wrapped header phone numbers in `<a href="tel:+8801615900004">` so visitors can tap to call.
   - Fixed footer typo ("home & aboard" $\to$ "home & abroad") and updated copyright year to 2026.

---

## File Directory

- [`index.html`](index.html) — Homepage with Hero Banner & Services
- [`services.html`](services.html) — Services with Digital Identity #1
- [`projects.html`](projects.html) — Projects with Digital Identity #1
- [`case-study.html`](case-study.html) — Case Studies (linked from menu bar)
- [`dis.html`](dis.html) — Digital Identity & Security (featuring **Upokari**)
- [`about_us.html`](about_us.html) — About Us
- [`products.html`](products.html) — Products
- [`contact.html`](contact.html) — Contact form (repaired)
- [`ai.html`](ai.html) — Artificial Intelligence
- [`sct.html`](sct.html) — Smart Card Technologies
- [`assets/css/style.css`](assets/css/style.css) — Original site styles & colors
- [`assets/css/responsive-fixes.css`](assets/css/responsive-fixes.css) — Responsive bug fixes

# spectrum
