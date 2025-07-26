# SPARC Framework Documentation Site

This directory contains the GitHub Pages documentation site for the SPARC Framework, built with Jekyll and optimized for SEO.

<!-- Force rebuild for premium design deployment -->

## 🚀 Quick Setup

### For Repository Maintainers

1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch  
   - Branch: `main`
   - Folder: `/ (root)` - GitHub Actions will handle the docs-site folder
   - Or set up GitHub Actions workflow (recommended)

2. **Configure Custom Domain (Optional):**
   - Add your custom domain in Settings → Pages
   - Update `_config.yml` with your domain

### For Local Development

1. **Prerequisites:**
   ```bash
   # Install Ruby and Bundler
   gem install bundler
   ```

2. **Setup:**
   ```bash
   cd docs-site
   bundle install
   ```

3. **Local Development:**
   ```bash
   bundle exec jekyll serve
   # Site will be available at http://localhost:4000
   ```

4. **Build for Production:**
   ```bash
   bundle exec jekyll build
   ```

## 📁 Structure

```
docs-site/
├── _config.yml           # Jekyll configuration with SEO
├── _includes/
│   └── head.html         # SEO-optimized head with structured data
├── _layouts/             # Page layouts
├── _sass/               # SCSS stylesheets
├── assets/              # Images, CSS, JS
├── _posts/              # Blog posts (if needed)
├── _agents/             # Agent documentation
├── _guides/             # Guide documentation
├── index.md             # Homepage with SEO optimization
├── sitemap.xml          # XML sitemap for search engines
├── robots.txt           # Search engine directives
├── Gemfile             # Ruby dependencies
└── .github/workflows/   # GitHub Actions for deployment
```

## 🔍 SEO Features

### Built-in Optimizations
- **Meta Tags:** Comprehensive Open Graph and Twitter Card support
- **Structured Data:** Schema.org JSON-LD for software application and organization
- **Sitemap:** Automatic XML sitemap generation
- **Robots.txt:** Search engine crawling directives
- **Performance:** Preconnected fonts and optimized loading

### Plugins Included
- `jekyll-seo-tag` - Automatic SEO tag generation
- `jekyll-sitemap` - XML sitemap generation
- `jekyll-feed` - RSS feed generation
- `jekyll-redirect-from` - URL redirection support

### Page-Level SEO
Each page can include:
```yaml
---
title: "Page Title"
description: "Page description for search engines"
keywords: "keyword1, keyword2, keyword3"
image: "/path/to/social-image.png"
canonical_url: "https://example.com/canonical"
---
```

## 🎨 Customization

### Brand Colors (ProductFoundry.ai)
- Primary: `#667eea` (Blue gradient start)
- Secondary: `#764ba2` (Blue gradient end)  
- Accent: `#28a745` (Success green)
- Community: `#f093fb` to `#f5576c` (Pink gradient)

### Typography
- Font Family: Inter (Google Fonts)
- Weights: 300, 400, 500, 600, 700

### Layout Components
- Hero section with gradient background
- Feature cards with hover effects
- Agent grid with color coding
- Responsive design for all devices

## 📊 Analytics & Monitoring

To add analytics:

1. **Google Analytics:**
   ```yaml
   # _config.yml
   google_analytics: UA-XXXXXXXX-X
   ```

2. **Google Search Console:**
   - Add site verification meta tag
   - Submit sitemap.xml

3. **Social Media:**
   - Update social media handles in `_config.yml`
   - Add social media verification tags

## 🚀 Deployment

### GitHub Actions (Recommended)
The included workflow (`.github/workflows/jekyll.yml`) automatically:
- Builds the site on pushes to `main` branch affecting `docs-site/`
- Deploys to GitHub Pages
- Handles Ruby and Jekyll setup

### Manual Deployment
1. Build locally: `bundle exec jekyll build`
2. Upload `_site/` contents to web server

## 🔗 Custom Domain Setup

1. **Add CNAME:**
   ```bash
   echo "yourdomain.com" > docs-site/CNAME
   ```

2. **Update Config:**
   ```yaml
   # _config.yml
   url: "https://yourdomain.com"
   baseurl: ""
   ```

3. **DNS Configuration:**
   - Add CNAME record: `www` → `username.github.io`
   - Add A records for apex domain:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`

## 📝 Content Management

### Adding New Pages
1. Create markdown file in appropriate directory
2. Add front matter with SEO fields
3. Link from navigation or other pages

### Adding Blog Posts
1. Create file in `_posts/` with format: `YYYY-MM-DD-title.md`
2. Add front matter
3. Posts automatically appear in feed

### Updating Agent Documentation
1. Add/edit files in `_agents/` collection
2. Use agent layout for consistent formatting

## 🛠️ Troubleshooting

### Common Issues

1. **Jekyll Build Fails:**
   ```bash
   bundle update
   bundle exec jekyll doctor
   ```

2. **GitHub Pages Not Updating:**
   - Check Actions tab for build errors
   - Verify file paths are correct
   - Check Jekyll version compatibility

3. **SEO Issues:**
   - Validate structured data with Google's Rich Results Test
   - Check meta tags with social media debugging tools
   - Verify sitemap accessibility

### Performance Optimization
- Optimize images (use WebP when possible)
- Minimize CSS/JS
- Enable GitHub Pages compression
- Use CDN for assets if needed

## 📄 License

Same as parent project: Creative Commons BY-NC 4.0

---

Built with ❤️ by the ProductFoundry.ai community