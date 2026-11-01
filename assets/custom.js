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
                    });
                }
                this.classList.add('active');

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
});
