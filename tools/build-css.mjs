// Builds assets/css/site.min.css: fonts + Font Awesome subset + Bootstrap + theme +
// responsive fixes in one file, with rules no page or script uses removed.
// One render-blocking request instead of four, and ~70% less CSS.
//
// Run after changing any HTML, assets/js/*.js or source CSS:
//   npx -y -p purgecss@7 node tools/build-css.mjs      (or set PURGECSS=/path/to/purgecss)
// Edit the source CSS files listed below, never site.min.css.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const { PurgeCSS } = await import(process.env.PURGECSS ? pathToFileURL(process.env.PURGECSS).href : 'purgecss');

const sources = [
  'assets/css/fonts.css',
  'assets/css/fontawesome-subset.min.css',
  'assets/css/bootstrap.min.css',
  'assets/css/style.min.css',
  'assets/css/responsive-fixes.min.css',
];
const combined = sources
  .map((f) => fs.readFileSync(path.join(root, f), 'utf8').replace(/\/\*# sourceMappingURL=[^*]*\*\//g, ''))
  .join('\n');

const [result] = await new PurgeCSS().purge({
  // Every page and the site's own scripts. Bootstrap's bundle is not scanned (it names
  // every Bootstrap class); the classes its JS adds at runtime are safelisted below.
  content: [
    path.join(root, '*.html'),
    ...fs.readdirSync(path.join(root, 'assets/js'))
      .filter((f) => f.endsWith('.js') && !f.startsWith('bootstrap'))
      .map((f) => path.join(root, 'assets/js', f)),
  ],
  css: [{ raw: combined }],
  defaultExtractor: (text) => text.match(/[A-Za-z0-9_-]+/g) || [],
  // Classes added at runtime by the Bootstrap features the site uses
  // (carousel, collapse, dropdown, modal) and by custom.js.
  safelist: {
    standard: [
      /^show$/, /^showing$/, /^hiding$/, /^active$/, /^fade$/, /^slide$/, /^pointer-event$/,
      /^collapse$/, /^collapsing$/, /^collapsed$/, /^collapse-horizontal$/,
      /^carousel-item-(next|prev|start|end)$/,
      /^modal/, /^dropdown-menu-(start|end)$/, /^drop(up|down|start|end)/,
      /^is-/, /^was-validated$/,
    ],
    greedy: [/data-bs-popper/],
  },
  keyframes: false,
  fontFace: false,
  variables: false,
});

const css = result.css
  // Icon fonts: show content while the font loads (Lighthouse "Font display").
  .replace(/(font-family:"Font Awesome 5 Brands";[^}]*?)font-display:block/, '$1font-display:swap')
  .replace(/(font-family:"Font Awesome 5 Free";[^}]*?)font-display:block/, '$1font-display:fallback');

fs.writeFileSync(path.join(root, 'assets/css/site.min.css'), '/* Built by tools/build-css.mjs. Do not edit. */\n' + css);
const kb = (s) => (Buffer.byteLength(s) / 1024).toFixed(1) + ' KB';
console.log(`site.min.css: ${kb(combined)} -> ${kb(css)}`);
