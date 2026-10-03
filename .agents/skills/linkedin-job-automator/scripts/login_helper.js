#!/usr/bin/env node
/**
 * LinkedIn Session Login & Refresh Helper
 * Opens the browser in visible mode with the persistent profile to authenticate
 * or refresh the LinkedIn session.
 */

const puppeteer = require('/home/saurabh-kumar123/Desktop/Desktop/express/AutoApply/node_modules/puppeteer-extra');
const StealthPlugin = require('/home/saurabh-kumar123/Desktop/Desktop/express/AutoApply/node_modules/puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

const USER_DATA_DIR = '/home/saurabh-kumar123/Desktop/Desktop/express/AutoApply/linkedin-profile';

async function setupSession() {
  console.log('🌐 Opening browser with persistent profile at:', USER_DATA_DIR);
  console.log('👉 Please log in to LinkedIn in the browser window.');

  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: USER_DATA_DIR,
    defaultViewport: null, // Full-screen: ensures browser occupies the entire desktop screen
    args: [
      '--start-maximized',
      '--window-size=1920,1080',
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-blink-features=AutomationControlled'
    ]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto('https://www.linkedin.com/feed/', { waitUntil: 'networkidle2', timeout: 60000 });

  console.log('\n======================================================');
  console.log('Checking current LinkedIn session status...');
  console.log('Current URL:', page.url());

  if (page.url().includes('/feed')) {
    console.log('✅ Session active and authenticated! You can now run headless scans.');
  } else {
    console.log('⚠️ Please complete login/verification in the opened window.');
    console.log('Waiting for you to reach the LinkedIn feed...');

    try {
      await page.waitForFunction(() => window.location.href.includes('/feed'), { timeout: 180000 });
      console.log('🎉 Login detected! Session saved to profile.');
    } catch (e) {
      console.log('Timed out waiting for login.');
    }
  }

  await browser.close();
  console.log('Browser closed. Profile updated successfully.');
}

if (require.main === module) {
  setupSession().catch(err => console.error('Error:', err.message));
}

module.exports = { setupSession };
