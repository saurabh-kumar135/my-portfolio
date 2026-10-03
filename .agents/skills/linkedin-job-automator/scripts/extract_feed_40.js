const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const OUTPUT_PATH = '/home/saurabh-kumar123/.gemini/config/skills/linkedin-job-automator/data/feed_posts_40.json';
const SCREENSHOT_PATH = '/home/saurabh-kumar123/.gemini/antigravity-ide/brain/a2506832-b3e4-448d-b13b-5505e82b95c7/linkedin_feed_40_posts.jpg';

async function extract40Posts() {
  console.log('🔗 Connecting to Chrome browser on port 9222...');
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222' });
  const pages = await browser.pages();
  
  // Find or use the primary LinkedIn tab
  let page = pages.find(p => p.url().includes('linkedin.com'));
  if (!page) {
    page = await browser.newPage();
  }
  await page.bringToFront();
  await page.setViewport({ width: 1920, height: 1080 });

  console.log('🧭 Navigating to https://www.linkedin.com/feed/ ...');
  await page.goto('https://www.linkedin.com/feed/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await new Promise(r => setTimeout(r, 4000));

  console.log('📜 Scrolling and extracting strictly 40 feed posts...');
  
  const postsMap = new Map();
  let scrollAttempts = 0;
  const maxScrollAttempts = 35;

  while (postsMap.size < 40 && scrollAttempts < maxScrollAttempts) {
    scrollAttempts++;
    
    const extractedBatch = await page.evaluate(() => {
      // LinkedIn feed posts have data-urn or class containing feed-shared-update-v2
      const postElements = Array.from(document.querySelectorAll('div[data-urn], div.feed-shared-update-v2, div[data-id]'));
      
      const results = [];
      postElements.forEach(el => {
        const urn = el.getAttribute('data-urn') || el.getAttribute('data-id') || '';
        // Look for author
        const authorEl = el.querySelector('.update-components-actor__name, .feed-shared-actor__name, span.visually-hidden');
        const headlineEl = el.querySelector('.update-components-actor__description, .feed-shared-actor__description');
        const textEl = el.querySelector('.feed-shared-update-v2__description, .update-components-text, div.update-components-update-v2__commentary');
        
        // Links inside the post
        const links = Array.from(el.querySelectorAll('a[href]')).map(a => a.href).filter(h => !h.includes('/in/') && !h.includes('/company/') && !h.includes('linkedin.com/feed'));

        const fullText = (textEl ? textEl.innerText : el.innerText || '').trim();
        const author = authorEl ? authorEl.innerText.trim() : 'Unknown';
        const headline = headlineEl ? headlineEl.innerText.trim() : '';

        if (fullText.length > 30) {
          results.push({
            urn: urn || fullText.substring(0, 50),
            author,
            headline,
            text: fullText,
            links: Array.from(new Set(links))
          });
        }
      });
      return results;
    });

    extractedBatch.forEach(p => {
      if (!postsMap.has(p.urn) && postsMap.size < 40) {
        postsMap.set(p.urn, p);
      }
    });

    console.log(`  [Batch ${scrollAttempts}] Collected ${postsMap.size}/40 unique posts...`);

    if (postsMap.size >= 40) break;

    // Scroll down smoothly
    await page.evaluate(() => window.scrollBy(0, 1200));
    await new Promise(r => setTimeout(r, 2000));
  }

  const posts = Array.from(postsMap.values()).slice(0, 40).map((p, idx) => {
    // Basic keyword analysis
    const lower = p.text.toLowerCase();
    const isJobRelated = lower.includes('hiring') || lower.includes('opening') || lower.includes('job') || 
                         lower.includes('apply') || lower.includes('opportunity') || lower.includes('intern') ||
                         lower.includes('developer') || lower.includes('engineer') || lower.includes('fullstack') ||
                         lower.includes('full-stack') || lower.includes('backend') || lower.includes('frontend') ||
                         lower.includes('software');
    
    return {
      index: idx + 1,
      author: p.author,
      headline: p.headline,
      links: p.links,
      isJobRelated,
      textSnippet: p.text.substring(0, 300) + (p.text.length > 300 ? '...' : ''),
      fullText: p.text
    };
  });

  console.log(`\n✅ Successfully extracted strictly ${posts.length} feed posts!`);
  
  // Save to JSON
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify({ extractedAt: new Date().toISOString(), totalPosts: posts.length, posts }, null, 2));
  console.log(`💾 Saved 40 posts to ${OUTPUT_PATH}`);

  // Capture screenshot of feed
  await page.screenshot({ path: SCREENSHOT_PATH, type: 'jpeg', quality: 80 });
  console.log(`📸 Full-screen desktop screenshot saved to ${SCREENSHOT_PATH}`);

  const relevantPosts = posts.filter(p => p.isJobRelated);
  console.log(`\n🎯 Relevant Job/Hiring Posts Identified in Feed: ${relevantPosts.length}`);
  relevantPosts.forEach(p => {
    console.log(`\n--- [Post #${p.index}] ${p.author} (${p.headline}) ---`);
    console.log(p.textSnippet);
    if (p.links.length > 0) console.log('Links:', p.links);
  });

  await browser.disconnect();
}

extract40Posts().catch(err => {
  console.error('Fatal error during feed extraction:', err);
  process.exit(1);
});
