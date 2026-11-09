# Spectrum IT Solutions Ltd. — Website

Static website for [Spectrum IT Solutions Ltd.](https://spectrum.com.bd/), Dhaka. Plain HTML, CSS and JavaScript with Bootstrap 5. No build step.

## Pages

| Page | File |
|---|---|
| Home | `index.html` |
| About Us | `about-us.html` |
| Services | `services.html` |
| Products | `products.html` |
| Projects | `projects.html` |
| Case Studies | `case-study.html` |
| Contact | `contact.html` |
| Digital Identity and Security | `digital-identity-security.html` |
| Smart Card Technologies | `smart-card-technologies.html` |
| Artificial Intelligence | `artificial-intelligence.html` |
| Blockchain Technology | `blockchain-technology.html` |
| Anti-Counterfeit Solutions | `anti-counterfeit.html` |
| Brand Protection | `brand-protection.html` |
| Business Automation | `business-automation.html` |
| AI Contact Center | `ai-contact-center.html` |
| Upokari (product family) | `upokari.html` |
| Mobile Apps | `mobile-apps.html` |
| Case study: TCB Smart Family Card | `case-study-tcb.html` |
| Case study: Industrial e-Court (hidden: ecourt.gov.bd is offline; page kept, not linked, noindex) | `case-study-e-court.html` |
| Case study: National e-Licensing | `case-study-e-licensing.html` |
| Case study: Smart Card Issuance | `case-study-smart-card.html` |
| Case study: Officers’ Club Dhaka (ocd.org.bd) | `case-study-ocd.html` |
| Case study: TCB AI Contact Center | `case-study-tcb-contact-center.html` |
| Case study: Novotheatre eTicket | `case-study-novotheatre.html` |
| Case study: Gazipur City Corporation e-Revenue | `case-study-gcc.html` |
| Case study: Automated Presence & Feedback | `case-study-apfs.html` |
| Not found | `404.html` |

The eight service pages follow the same layout: a plain-language article first (with contents, FAQ and Article/FAQ structured data), then the Spectrum service section. Each case study page has a facts box, the problem, what was built, how it works, results and the technology in plain words.

The small files with old names (`dis.html`, `sct.html`, `ai.html`, `About Us.html`, `Digital_Identity_&_Security.html` and so on) are redirects from the previous site's addresses. Keep them so old links and search results still work.

## Folders

- `assets/css/` — `bootstrap.min.css`, the theme (`style.min.css`), site fixes (`responsive-fixes.css` and its minified copy), and `fontawesome-subset.min.css`.
- `assets/webfonts/` — Font Awesome subset fonts (only the icons the site uses).
- `assets/js/` — Bootstrap bundle and `custom.js`.
- `assets/img/` — images. `apps/` holds app icons and app screenshots taken from the Google Play and App Store listings; `projects/` holds screenshots of client web portals. `og/` holds the 1200×630 social share images, `pages/` the service page visuals, `digital-identity/` the Digital Identity page images.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `.well-known/ard.json` — search and AI discovery files.

## Run locally

```bash
python3 -m http.server 5000 --bind 127.0.0.1
```

Then open http://127.0.0.1:5000/.

## Editing conventions

- **CSS changes** go in both `assets/css/responsive-fixes.css` (readable) and `assets/css/responsive-fixes.min.css` (loaded by the pages). After a change, bump the `?v=` version on `responsive-fixes.min.css` in every page so browsers fetch the new file.
- The theme forces `font-size: 18px !important` on `p`, `li` and `div`. Overrides need a more specific selector with `!important`.
- **Images:** add a `.webp` next to each `.jpg`/`.png` and use `<picture>` with the WebP as the first source. Always set `width` and `height`.
- **New icons:** the site loads a Font Awesome 5.15.4 subset. If you use an icon that is not in `assets/css/fontawesome-subset.min.css`, add its rule and rebuild the subset fonts, or it will show as a blank square.
- **New page:** copy the head, header and footer from an existing page, add it to `sitemap.xml`, `llms.txt` and the footer Quick Links, and create a share image in `assets/img/og/`.
- Phone numbers are shown as `+880 1615-900004`; `tel:` links use `+8801615900004`.

## Deploy

The site is served as static files (currently GitHub Pages). Canonical URLs, the sitemap and structured data already point to `https://spectrum.com.bd/`.

## Hidden content

Content for projects whose websites are offline is hidden, not deleted. Each hidden block has the Bootstrap class `d-none` and a comment starting with "Hidden while". To show it again, remove `d-none` and add the page back to `sitemap.xml` and `llms.txt`. Currently hidden: Industrial e-Court (ecourt.gov.bd).
