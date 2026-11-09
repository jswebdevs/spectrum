/**
 * Spectrum IT Solutions Ltd. - Custom Interactive Enhancements
 * - Interactive Category Filter (Products & Projects pages)
 * - Zero-Dependency Scroll-Reveal Animations (IntersectionObserver)
 */

document.addEventListener('DOMContentLoaded', function () {
    // -------------------------------------------------------------------------
    // 1. Interactive Category Filter (Products & Projects)
    // -------------------------------------------------------------------------
    const filterButtons = document.querySelectorAll('.filter-btn');
    if (filterButtons.length > 0) {
        filterButtons.forEach(function (button) {
            button.addEventListener('click', function (e) {
                e.preventDefault();
                const targetFilter = this.getAttribute('data-filter');
                const container = this.closest('.container') || document;

                // Update active state among siblings in the same filter-nav-wrap
                const groupWrap = this.closest('.filter-nav-wrap');
                if (groupWrap) {
                    groupWrap.querySelectorAll('.filter-btn').forEach(function (btn) {
                        btn.classList.remove('active');
                        if (btn.hasAttribute('aria-pressed')) btn.setAttribute('aria-pressed', 'false');
                    });
                }
                this.classList.add('active');
                if (this.hasAttribute('aria-pressed')) this.setAttribute('aria-pressed', 'true');

                // Filter items across page
                const filterItems = document.querySelectorAll('.filter-item');
                filterItems.forEach(function (item) {
                    const category = item.getAttribute('data-category');
                    if (targetFilter === 'all' || category === targetFilter) {
                        item.classList.remove('filter-item-hidden');
                        // Re-trigger reveal animation smoothly
                        item.classList.remove('is-revealed');
                        void item.offsetWidth; // force reflow
                        item.classList.add('is-revealed');
                    } else {
                        item.classList.add('filter-item-hidden');
                    }
                });

                // Automatically toggle section containers if all items within are hidden
                document.querySelectorAll('.filter-section').forEach(function (sec) {
                    // Safety check: Never hide a container that contains the filter navigation buttons
                    if (sec.querySelector('.filter-nav-wrap')) return;
                    const visibleItems = sec.querySelectorAll('.filter-item:not(.filter-item-hidden)');
                    if (visibleItems.length === 0) {
                        sec.classList.add('filter-item-hidden');
                    } else {
                        sec.classList.remove('filter-item-hidden');
                    }
                });
            });
        });
    }

    // -------------------------------------------------------------------------
    // 2. Scroll Reveal Animations (Zero-dependency IntersectionObserver)
    // -------------------------------------------------------------------------
    const revealElements = document.querySelectorAll('.reveal-on-scroll');
    if (revealElements.length > 0) {
        // If reduced motion is preferred or IntersectionObserver unsupported, reveal instantly
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
            revealElements.forEach(function (el) {
                el.classList.add('is-revealed');
            });
        } else {
            const revealObserver = new IntersectionObserver(function (entries, observer) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                root: null,
                rootMargin: '0px 0px -40px 0px',
                threshold: 0.12
            });

            revealElements.forEach(function (el) {
                revealObserver.observe(el);
            });
        }
    }

    // -------------------------------------------------------------------------
    // 3. Mobile Navigation Fullscreen Lock & Scroll Management
    // -------------------------------------------------------------------------
    const mainNav = document.getElementById('templatemo_main_nav');
    const navbar = document.querySelector('nav.navbar');

    function updateNavBottom() {
        if (navbar) {
            const rect = navbar.getBoundingClientRect();
            document.documentElement.style.setProperty('--navbar-bottom', Math.round(rect.bottom) + 'px');
        }
    }

    if (mainNav) {
        // When mobile menu begins opening
        mainNav.addEventListener('show.bs.collapse', function () {
            updateNavBottom();
            document.body.classList.add('mobile-menu-open');
            mainNav.style.removeProperty('height');
        });

        mainNav.addEventListener('shown.bs.collapse', function () {
            mainNav.style.removeProperty('height');
        });

        // When mobile menu begins closing
        mainNav.addEventListener('hide.bs.collapse', function () {
            document.body.classList.remove('mobile-menu-open');
        });

        // Ensure closed state cleanup
        mainNav.addEventListener('hidden.bs.collapse', function () {
            document.body.classList.remove('mobile-menu-open');
        });

        // Close mobile menu on regular navigation link click
        mainNav.querySelectorAll('.nav-link:not(.dropdown-toggle), .dropdown-item').forEach(function (link) {
            link.addEventListener('click', function () {
                if (window.innerWidth < 992) {
                    if (typeof bootstrap !== 'undefined' && bootstrap.Collapse) {
                        const bsCollapse = bootstrap.Collapse.getInstance(mainNav);
                        if (bsCollapse) {
                            bsCollapse.hide();
                        }
                    }
                }
            });
        });
    }

    // Clean up if resized to desktop or rotated
    window.addEventListener('resize', function () {
        if (window.innerWidth >= 992) {
            document.body.classList.remove('mobile-menu-open');
            if (mainNav && mainNav.classList.contains('show')) {
                if (typeof bootstrap !== 'undefined' && bootstrap.Collapse) {
                    const bsCollapse = bootstrap.Collapse.getInstance(mainNav);
                    if (bsCollapse) {
                        bsCollapse.hide();
                    }
                }
            }
        } else {
            updateNavBottom();
        }
    });

    window.addEventListener('orientationchange', function () {
        setTimeout(updateNavBottom, 150);
    });
});

// -------------------------------------------------------------------------
// Hero slider: finger- and mouse-following swipe.
// The slide moves with the finger and can be held halfway. On release it
// moves on to the next/previous slide if dragged past half the width (or
// flicked quickly), otherwise it springs back.
// -------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.getElementById('template-mo-zay-hero-carousel');
    if (!carousel) return;
    const inner = carousel.querySelector('.carousel-inner');
    const items = Array.from(inner.querySelectorAll('.carousel-item'));
    const dots = Array.from(carousel.querySelectorAll('.carousel-indicators [data-bs-slide-to]'));
    if (items.length < 2) return;

    const DURATION = 350;
    let startX = 0, startY = 0, startT = 0, dx = 0;
    let pointerId = null, dragging = false, animating = false;
    let current = null, neighbour = null, dir = 0, width = 0;

    function idxOf(el) { return items.indexOf(el); }
    function neighbourFor(d) {
        const i = idxOf(current);
        return items[(i + (d > 0 ? -1 : 1) + items.length) % items.length];
    }
    function place(el, x, withTransition) {
        el.style.transition = withTransition ? 'transform ' + DURATION + 'ms ease-out' : 'none';
        el.style.transform = 'translateX(' + x + 'px)';
    }
    function showNeighbour(d) {
        if (neighbour && dir === d) return;
        if (neighbour) clearEl(neighbour);
        dir = d;
        neighbour = neighbourFor(d);
        neighbour.classList.add('sld-drag-peek');
    }
    function clearEl(el) {
        el.classList.remove('sld-drag-peek');
        el.style.transition = '';
        el.style.transform = '';
    }
    function setActive(next) {
        current.classList.remove('active');
        next.classList.add('active');
        const n = idxOf(next);
        dots.forEach(function (d, i) {
            d.classList.toggle('active', i === n);
            if (i === n) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current');
        });
    }

    inner.addEventListener('pointerdown', function (e) {
        if (animating || pointerId !== null) return;
        if (e.pointerType === 'mouse') {
            if (e.button !== 0) return;
            // No text selection while dragging with the mouse; links and buttons still get clicks.
            if (!e.target.closest('a, button, input, textarea, select')) e.preventDefault();
        }
        if (inner.querySelector('.carousel-item-next, .carousel-item-prev')) return; // Bootstrap is mid-slide
        pointerId = e.pointerId;
        startX = e.clientX; startY = e.clientY; startT = Date.now(); dx = 0;
        dragging = false; dir = 0; neighbour = null;
        current = inner.querySelector('.carousel-item.active');
        width = inner.clientWidth;
    });

    inner.addEventListener('pointermove', function (e) {
        if (e.pointerId !== pointerId) return;
        const mx = e.clientX - startX, my = e.clientY - startY;
        if (!dragging) {
            if (Math.abs(mx) < 8 || Math.abs(mx) < Math.abs(my)) return;
            dragging = true;
            carousel.classList.add('sld-dragging');
            try { inner.setPointerCapture(e.pointerId); } catch (err) {}
        }
        dx = Math.max(-width, Math.min(width, mx));
        if (dx === 0) return;
        showNeighbour(dx > 0 ? 1 : -1);
        place(current, dx, false);
        place(neighbour, dx - dir * width, false);
    });

    function finish(e) {
        if (e.pointerId !== pointerId) return;
        pointerId = null;
        carousel.classList.remove('sld-dragging');
        if (!dragging || !neighbour) { dragging = false; return; }
        dragging = false;
        const fast = Math.abs(dx) > 40 && Math.abs(dx) / Math.max(1, Date.now() - startT) > 0.5;
        const go = e.type !== 'pointercancel' && (Math.abs(dx) > width / 2 || fast);
        const cur = current, nb = neighbour, d = dir;
        animating = true;
        if (go) {
            place(cur, d * width, true);
            place(nb, 0, true);
        } else {
            place(cur, 0, true);
            place(nb, -d * width, true);
        }
        setTimeout(function () {
            if (go) setActive(nb);
            clearEl(cur); clearEl(nb);
            neighbour = null; animating = false;
        }, DURATION + 20);
    }
    inner.addEventListener('pointerup', finish);
    inner.addEventListener('pointercancel', finish);

    // Stop the browser's own image/link drag so the mouse can swipe slides.
    inner.addEventListener('dragstart', function (e) { e.preventDefault(); });

    // A drag should not count as a tap on a button or link inside the slide.
    inner.addEventListener('click', function (e) {
        if (Math.abs(dx) > 8) { e.preventDefault(); e.stopPropagation(); dx = 0; }
    }, true);
});
