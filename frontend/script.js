document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal implementation (Oliver Wyman style)
    const revealElements = document.querySelectorAll('h1, h2, h3, p, .card, li, .reveal-target');
    
    // Add the reveal class to all targeted elements if they don't already have an animation class
    revealElements.forEach(el => {
        // Skip specific landing page elements that have their own complex animations
        if (!el.classList.contains('landing-eyebrow') &&
            !el.classList.contains('company-name') &&
            !el.classList.contains('landing-tagline') &&
            !el.classList.contains('landing-cta') &&
            !el.closest('nav') && 
            !el.closest('footer') && 
            !el.closest('#screen-landing') &&
            !el.closest('#screen-auth')) {
            
            // Stagger words for pure text elements
            // To be safe and not break innerHTML (like <br> or <a>), we only stagger if it's pure text
            if (['H1', 'H2', 'H3', 'P', 'LI'].includes(el.tagName) && el.children.length === 0) {
                const words = el.textContent.split(/(\s+)/); // Preserve whitespace
                el.innerHTML = '';
                let wordCount = 0;
                
                words.forEach(word => {
                    if (word.trim().length > 0) {
                        const span = document.createElement('span');
                        span.textContent = word;
                        span.className = 'stagger-word';
                        span.style.transitionDelay = `${wordCount * 0.04}s`; // Stagger delay
                        el.appendChild(span);
                        wordCount++;
                    } else {
                        el.appendChild(document.createTextNode(word));
                    }
                });
                el.classList.add('reveal-stagger');
                el.classList.remove('fade-enter'); // Remove basic fade if it had it
            } else {
                // Regular fade up for cards and elements with HTML children
                el.classList.add('reveal-up');
            }
        }
    });

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px', // Trigger slightly before the element comes fully into view
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Stop observing once revealed
            }
        });
    }, observerOptions);

    // Observe all elements with the reveal-up or reveal-stagger class
    document.querySelectorAll('.reveal-up, .reveal-stagger').forEach(el => {
        revealObserver.observe(el);
    });
});


// Mobile nav toggle
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const mobileNav = document.querySelector('.mobile-nav');
    const closeBtn  = document.querySelector('.mobile-nav .close-btn');

    if (hamburger && mobileNav) {
      hamburger.addEventListener('click', () => {
        mobileNav.classList.add('open');
        document.body.style.overflow = 'hidden';
      });
    }
    if (closeBtn && mobileNav) {
      closeBtn.addEventListener('click', () => {
        mobileNav.classList.remove('open');
        document.body.style.overflow = '';
      });
    }
    // Close on link click
    if (mobileNav) {
        mobileNav.querySelectorAll('a').forEach(link => {
          link.addEventListener('click', () => {
            mobileNav.classList.remove('open');
            document.body.style.overflow = '';
          });
        });
    }
});
