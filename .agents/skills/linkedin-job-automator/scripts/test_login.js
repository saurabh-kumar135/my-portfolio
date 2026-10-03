const puppeteer = require('/home/saurabh-kumar123/Desktop/Desktop/express/AutoApply/node_modules/puppeteer-extra');
const StealthPlugin = require('/home/saurabh-kumar123/Desktop/Desktop/express/AutoApply/node_modules/puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

async function tryLogin() {
  const browser = await puppeteer.launch({
    headless: 'new',
    userDataDir: '/home/saurabh-kumar123/Desktop/Desktop/express/AutoApply/linkedin-profile',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-blink-features=AutomationControlled']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto('https://www.linkedin.com/login', { waitUntil: 'networkidle2', timeout: 35000 });

  console.log('Initial URL:', page.url());
  const userInput = await page.$('input[type="email"]');
  const passInput = await page.$('input[type="password"]');
  const submitBtn = await page.$('button[type="submit"]');

  console.log('userInput found:', !!userInput);
  console.log('passInput found:', !!passInput);
  console.log('submitBtn found:', !!submitBtn);

  if (!submitBtn) {
    const allBtns = await page.evaluate(() => Array.from(document.querySelectorAll('button')).map(b => ({ text: b.innerText, type: b.type, id: b.id, cls: b.className })));
    console.log('Buttons on page:', allBtns);
  }

  if (userInput && passInput) {
    console.log('Entering credentials for saurabhrajput.25072005@gmail.com...');
    await userInput.type('saurabhrajput.25072005@gmail.com', { delay: 60 });
    await passInput.type('crudAbc@123', { delay: 60 });

    console.log('Submitting login form via DOM form submission...');
    await page.evaluate(() => {
      const form = document.querySelector('form');
      if (form) {
        form.requestSubmit ? form.requestSubmit() : form.submit();
      }
    });

    await new Promise(r => setTimeout(r, 10000));
    console.log('Resulting URL:', page.url());
    console.log('Page Title:', await page.title());

    if (page.url().includes('feed')) {
      console.log('🎉 SUCCESS: Logged in and reached LinkedIn feed!');
    } else if (page.url().includes('checkpoint') || page.url().includes('challenge') || page.url().includes('captcha')) {
      console.log('⚠️ Verification Challenge / CAPTCHA encountered!');
      await page.screenshot({ path: '/tmp/linkedin_checkpoint.png' });
      console.log('Screenshot saved to: /tmp/linkedin_checkpoint.png');
    } else {
      const pageText = await page.evaluate(() => document.body.innerText.slice(0, 300));
      console.log('Current URL after submit attempt:', page.url());
      console.log('Page Snippet:', pageText.replace(/\n+/g, ' '));
      await page.screenshot({ path: '/tmp/after_login.png' });
    }
  } else {
    console.log('No login inputs found. Current URL:', page.url());
  }
  await browser.close();
}

tryLogin().catch(err => console.error('Error:', err.message));
