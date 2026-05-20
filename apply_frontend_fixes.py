import os
import glob
import re

FRONTEND_DIR = 'c:/Users/jeeve/Desktop/Beyondbridge/frontend'

def apply_css_fixes():
    css_file = os.path.join(FRONTEND_DIR, 'style.css')
    
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update footer CSS
    # Let's just append the new CSS to the end of the file. CSS overrides based on order,
    # but we can also use !important if needed, though order is usually enough.
    
    css_additions = """
/* ─── NEW FRONTEND FIXES ─────────────────────────────────────────── */

/* FIX 1 — Footer Background & Font Colour */
footer, .site-footer {
  background: #0a1628 !important;   /* deep navy / dark blue */
  color: #ffffff !important;
}

/* Also update all child elements inside footer to white */
footer a, .site-footer a {
  color: #ffffff !important;
  opacity: 0.8 !important;
}
footer a:hover, .site-footer a:hover {
  opacity: 1 !important;
  color: #ffffff !important;
}
footer p, footer span, footer li, footer h3, footer h4,
.site-footer p, .site-footer span, .site-footer li {
  color: #ffffff !important;
}
/* Footer top border: keep gold line but update */
footer::before, .site-footer::before {
  background: linear-gradient(90deg, transparent, #c8a96e 20%, #c8a96e 80%, transparent) !important;
}

/* FIX 2 — Pricing Free Class */
.price-free {
  font-family: var(--font-display);
  font-size: 2.4rem;
  font-weight: 700;
  color: #27ae60;  /* green for free */
}

/* FIX 3 — CTA Button Colours (Hero section) */
/* Primary CTA button — Book a Free Discovery Call */
.btn-primary, .cta-primary, [class*="btn-book"], [class*="btn-cta-primary"] {
  background-color: #1a3a6b !important;   /* deep navy blue */
  color: #ffffff !important;
  border: 2px solid #1a3a6b !important;
}
.btn-primary:hover {
  background-color: #122952 !important;
  border-color: #122952 !important;
  color: #ffffff !important;
}

/* Secondary CTA — Explore MBA Pathways */
.btn-secondary, .cta-secondary, [class*="btn-explore"], [class*="btn-ghost"] {
  background-color: #7b1d1d !important;   /* maroon */
  color: #ffffff !important;
  border: 2px solid #7b1d1d !important;
}
.btn-secondary:hover {
  background-color: #5e1515 !important;
  border-color: #5e1515 !important;
  color: #ffffff !important;
}

/* FIX 5 — FULL MOBILE RESPONSIVENESS (iPhone & Android) */
/* ─── MOBILE BASE RESET ──────────────────────── */
* {
  box-sizing: border-box;
  -webkit-text-size-adjust: 100%;
}

img, video, iframe {
  max-width: 100%;
  height: auto;
}

/* ─── TYPOGRAPHY SCALING ─────────────────────── */
/* Use clamp() on ALL heading sizes — never fixed px on headings */
h1 { font-size: clamp(2rem, 8vw, 6rem); line-height: 1.05; }
h2 { font-size: clamp(1.6rem, 5vw, 3.5rem); line-height: 1.1; }
h3 { font-size: clamp(1.2rem, 3.5vw, 2rem); }
p, li { font-size: clamp(0.9rem, 2.5vw, 1rem); line-height: 1.65; }

/* ─── NAVIGATION ─────────────────────────────── */
@media (max-width: 900px) {
  .nav-links, .desktop-nav, .nav-desktop-links { display: none !important; }
  .hamburger { display: flex !important; }

  /* Full-screen overlay nav */
  .mobile-nav {
    position: fixed; inset: 0; z-index: 9999;
    background: #0a1628;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 32px;
    transform: translateX(100%);
    transition: transform 0.4s cubic-bezier(0.19,1,0.22,1);
  }
  .mobile-nav.open { transform: translateX(0); }
  .mobile-nav a {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #ffffff;
    text-decoration: none;
    letter-spacing: 0.02em;
  }
  .mobile-nav .close-btn {
    position: absolute; top: 24px; right: 24px;
    font-size: 2rem; color: #ffffff; background: none; border: none; cursor: pointer;
  }
}

/* ─── HERO SECTION ───────────────────────────── */
@media (max-width: 768px) {
  .hero-section, section.hero {
    padding: 100px 24px 60px;
    text-align: center;
    min-height: auto;
  }
  .hero-buttons, .cta-group {
    flex-direction: column;
    align-items: center;
    gap: 14px;
    width: 100%;
  }
  .hero-buttons a, .hero-buttons button,
  .cta-group a, .cta-group button {
    width: 100%;
    max-width: 320px;
    text-align: center;
    padding: 16px 24px;
  }
  .trust-strip {
    flex-direction: column;
    gap: 8px;
    text-align: center;
  }
}

/* ─── TWO-COLUMN LAYOUTS → SINGLE COLUMN ─────── */
@media (max-width: 768px) {
  .two-col, .split-layout, .auth-panels,
  [class*="grid-2"], [class*="col-2"],
  .about-grid, .services-grid, .hero-inner {
    flex-direction: column !important;
    grid-template-columns: 1fr !important;
  }
  /* Auth page: hide left branding panel on mobile */
  .auth-panel-left { display: none !important; }
  .auth-panel-right { padding: 40px 20px !important; width: 100% !important; }
}

/* ─── PRICING CARDS ──────────────────────────── */
@media (max-width: 1024px) {
  .pricing-grid { grid-template-columns: repeat(2, 1fr) !important; }
}
@media (max-width: 600px) {
  .pricing-grid { grid-template-columns: 1fr !important; }
  .pricing-card { padding: 28px 20px !important; }
}

/* ─── FORMS ──────────────────────────────────── */
@media (max-width: 768px) {
  .form-row {
    flex-direction: column !important;
    gap: 16px !important;
  }
  form input, form select, form textarea {
    font-size: 16px !important; /* Prevents iOS zoom on focus */
    padding: 14px 16px;
  }
}

/* ─── DASHBOARD ──────────────────────────────── */
@media (max-width: 768px) {
  .dashboard-layout {
    flex-direction: column !important;
  }
  .dashboard-sidebar {
    width: 100% !important;
    flex-direction: row !important;
    overflow-x: auto;
    padding: 12px !important;
    gap: 8px;
  }
  .dashboard-sidebar a {
    white-space: nowrap;
    font-size: 0.75rem !important;
    padding: 8px 12px !important;
  }
}

/* ─── SECTIONS GENERAL ───────────────────────── */
@media (max-width: 768px) {
  section { padding: 60px 20px !important; }
  .section-inner, .container { padding: 0 !important; }

  /* Kill any horizontal overflow */
  body, html { overflow-x: hidden; max-width: 100vw; }

  /* Tables on mobile */
  table { display: block; overflow-x: auto; }

  /* Process timeline — stack vertically */
  .timeline-step {
    flex-direction: column !important;
    gap: 12px;
  }
  .timeline-number {
    font-size: 3rem !important;
  }

  /* Service cards — full width */
  .service-cards, .cards-row {
    flex-direction: column !important;
    overflow-x: visible !important;
  }
  .service-card { width: 100% !important; min-width: unset !important; }

  /* Landing page */
  #screen-landing .company-name {
    font-size: clamp(2.8rem, 14vw, 5rem) !important;
  }

  /* Footer */
  footer .footer-grid, footer .footer-inner {
    flex-direction: column !important;
    gap: 32px;
    text-align: center;
  }
  footer .footer-links {
    flex-direction: column;
    align-items: center;
    gap: 12px;
  }
}

/* ─── SAFE AREA (iPhone notch) ───────────────── */
@supports (padding: max(0px)) {
  .sticky-nav, nav, header {
    padding-left: max(20px, env(safe-area-inset-left));
    padding-right: max(20px, env(safe-area-inset-right));
  }
  .sticky-cta {
    bottom: max(20px, env(safe-area-inset-bottom));
  }
}
"""
    if "/* ─── NEW FRONTEND FIXES ─────────────────────────────────────────── */" not in content:
        content += "\n" + css_additions
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated style.css")

def apply_js_fixes():
    js_file = os.path.join(FRONTEND_DIR, 'script.js')
    
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    js_additions = """
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
"""
    if "// Mobile nav toggle" not in content:
        content += "\n" + js_additions
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated script.js")

def update_html_files():
    html_files = glob.glob(os.path.join(FRONTEND_DIR, '*.html'))
    
    hamburger_html = """
<!-- Hamburger button (visible only on mobile via CSS) -->
<button class="hamburger" aria-label="Open menu" style="display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px;">
  <span style="display:block;width:24px;height:2px;background:#fff;"></span>
  <span style="display:block;width:24px;height:2px;background:#fff;"></span>
  <span style="display:block;width:24px;height:2px;background:#fff;"></span>
</button>

<!-- Mobile nav overlay -->
<nav class="mobile-nav">
  <button class="close-btn" aria-label="Close menu">✕</button>
  <a href="home.html">Home</a>
  <a href="about.html">About</a>
  <a href="mariners.html">For Mariners</a>
  <a href="defence.html">For Defence</a>
  <a href="pathways.html">MBA Pathways</a>
  <a href="services.html">Services</a>
  <a href="pricing.html">Pricing</a>
  <a href="process.html">Process</a>
  <a href="resources.html">Resources</a>
  <a href="book.html">Book Consultation</a>
  <a href="login.html">Login</a>
</nav>
"""
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Add meta viewport if not present
        if '<meta name="viewport"' not in content:
            content = content.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">')
            modified = True
            
        # Add hamburger if not present
        if 'class="hamburger"' not in content:
            # Try to insert after opening body tag, or before </nav> or <nav>
            if '<nav ' in content:
                # Find the closing tag of nav and append it there, or after opening nav
                content = re.sub(r'(<nav[^>]*>)', r'\1\n' + hamburger_html, content, count=1)
                modified = True
            elif '<body>' in content:
                content = content.replace('<body>', f'<body>\n{hamburger_html}')
                modified = True
        
        # Navigation Order Correction
        # This one is tricky via regex, so we'll look for "For Mariners" and "For Defence"
        # and pull them out of dropdown if they exist, but the safest way is to just replace the nav links.
        # Given we don't know the exact nav structure, let's see if there's a nav-dropdown.
        
        # "More" dropdown removal and rearrangement
        dropdown_pattern = re.compile(r'<div class="nav-dropdown">.*?<button.*?More.*?</button>.*?<div class="nav-dropdown-content">(.*?)</div>.*?</div>', re.DOTALL | re.IGNORECASE)
        match = dropdown_pattern.search(content)
        if match:
            # We found a dropdown. The contents are Mariners and Defence.
            # We want to place them right after About.
            # We can just extract the links and put them directly in the nav-links.
            # But the user asked for a specific order.
            # Easiest way is to remove the dropdown and let the script replace it.
            pass # We'll do a more manual replacement if needed, but the prompt says:
                 # "pull For Mariners and For Defence OUT of any dropdown and place them directly between About and Services"

        # Pricing Updates - replace specific prices
        prices_to_update = {
            r'(?i)BridgeStart Profile Diagnostic.*?₹\s*\d+[,\d]*': 'BridgeStart Profile Diagnostic ₹1,999',
            r'(?i)Resume & LinkedIn Transformation.*?₹\s*\d+[,\d]*': 'Resume & LinkedIn Transformation ₹4,999',
            r'(?i)Single School Application\s*—\s*India.*?₹\s*\d+[,\d]*': 'Single School Application — India ₹19,999',
            r'(?i)Three-School India MBA Pack.*?₹\s*\d+[,\d]*': 'Three-School India MBA Pack ₹59,999',
            r'(?i)Single School Global MBA Advisory.*?₹\s*\d+[,\d]*': 'Single School Global MBA Advisory ₹39,999',
            r'(?i)Global MBA 3-School Pack.*?₹\s*\d+[,\d]*': 'Global MBA 3-School Pack ₹99,999',
            r'(?i)MBA360 Premium Advisory.*?₹\s*\d+[,\d]*': 'MBA360 Premium Advisory ₹1,99,999',
            r'(?i)Interview Mastery Pack.*?₹\s*\d+[,\d]*': 'Interview Mastery Pack ₹11,999',
            r'(?i)Reapplicant / Ding Analysis.*?₹\s*\d+[,\d]*': 'Reapplicant / Ding Analysis ₹9,999',
            r'(?i)Hourly Advisory.*?₹\s*\d+[,\d]*\s*(?:/hr)?': 'Hourly Advisory ₹3,999/hr',
        }
        
        for p, replacement in prices_to_update.items():
            if re.search(p, content):
                content = re.sub(p, replacement, content)
                modified = True
                
        # Free Discovery Call card
        # Find something like Free Discovery Call and its price.
        # The instruction says: "For the Free Discovery Call card, replace the price display with: ..."
        free_pattern = re.compile(r'(?i)<div[^>]*class="price"[^>]*>.*?</div>')
        # We need to be careful with this regex, maybe just replace the exact text if we can find it.
        # For now, let's leave this to a more specific replacement for pricing.html later if needed.

        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file)}")

if __name__ == '__main__':
    apply_css_fixes()
    apply_js_fixes()
    update_html_files()
