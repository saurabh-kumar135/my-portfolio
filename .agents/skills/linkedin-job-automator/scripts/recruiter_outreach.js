const fs = require('fs');
const path = require('path');
const https = require('https');
const tracker = require('./tracker_manager');

// Load environment variables
function loadEnv() {
  const envPaths = [
    '/home/saurabh-kumar123/Desktop/Desktop/express/StudyMate/.env',
    '/home/saurabh-kumar123/Desktop/Desktop/express/HavenTo/.env',
    '/home/saurabh-kumar123/Desktop/Desktop/express/.env',
    path.join(__dirname, '../.env')
  ];

  for (const envPath of envPaths) {
    if (fs.existsSync(envPath)) {
      const content = fs.readFileSync(envPath, 'utf-8');
      content.split('\n').forEach(line => {
        const trimmed = line.trim();
        if (trimmed && !trimmed.startsWith('#') && trimmed.includes('=')) {
          const [k, ...v] = trimmed.split('=');
          const key = k.trim();
          const val = v.join('=').trim().replace(/^['"]|['"]$/g, '');
          if (!process.env[key]) {
            process.env[key] = val;
          }
        }
      });
    }
  }
}

loadEnv();

async function getAccessToken() {
  const clientId = process.env.GMAIL_CLIENT_ID;
  const clientSecret = process.env.GMAIL_CLIENT_SECRET;
  const refreshToken = process.env.GMAIL_REFRESH_TOKEN;

  if (!clientId || !clientSecret || !refreshToken) {
    throw new Error('Missing GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, or GMAIL_REFRESH_TOKEN.');
  }

  const payload = new URLSearchParams({
    client_id: clientId,
    client_secret: clientSecret,
    refresh_token: refreshToken,
    grant_type: 'refresh_token'
  }).toString();

  return new Promise((resolve, reject) => {
    const req = https.request('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(payload)
      }
    }, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const body = JSON.parse(data);
          if (body.access_token) {
            resolve(body.access_token);
          } else {
            reject(new Error(`Failed to refresh token: ${data}`));
          }
        } catch (e) {
          reject(e);
        }
      });
    });

    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

/**
 * Creates RFC 2822 MIME message with optional PDF attachment
 */
function createMimeMessage({ to, subject, htmlBody, resumePath }) {
  const boundary = `====_BOUNDARY_${Date.now()}_====`;
  const senderEmail = 'saurabhrajput.25072005@gmail.com';

  let raw = '';
  raw += `From: "Saurabh Kumar" <${senderEmail}>\r\n`;
  raw += `To: ${to}\r\n`;
  raw += `Subject: ${subject}\r\n`;
  raw += `MIME-Version: 1.0\r\n`;
  raw += `Content-Type: multipart/mixed; boundary="${boundary}"\r\n\r\n`;

  // HTML Body Part
  raw += `--${boundary}\r\n`;
  raw += `Content-Type: text/html; charset=UTF-8\r\n`;
  raw += `Content-Transfer-Encoding: 7bit\r\n\r\n`;
  raw += `${htmlBody}\r\n\r\n`;

  // Resume Attachment Part
  if (resumePath && fs.existsSync(resumePath)) {
    const fileData = fs.readFileSync(resumePath).toString('base64');
    const fileName = path.basename(resumePath);
    raw += `--${boundary}\r\n`;
    raw += `Content-Type: application/pdf; name="${fileName}"\r\n`;
    raw += `Content-Disposition: attachment; filename="${fileName}"\r\n`;
    raw += `Content-Transfer-Encoding: base64\r\n\r\n`;
    raw += `${fileData}\r\n\r\n`;
  }

  raw += `--${boundary}--`;

  // Base64url encoding
  return Buffer.from(raw).toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
}

/**
 * Sends follow-up email via Gmail REST API
 */
async function sendEmailOutreach({ to, recruiterName, jobTitle, company, resumePath }) {
  if (tracker.isRecruiterContacted(to, jobTitle)) {
    console.log(`⏩ [Outreach] Skipping email to ${to} (Already contacted for ${jobTitle}).`);
    return { success: false, skipped: true, reason: 'Already contacted' };
  }

  const templatePath = path.join(__dirname, '../templates/recruiter_email.html');
  let html = fs.readFileSync(templatePath, 'utf-8');
  html = html
    .replace(/\{\{recruiter_name\}\}/g, recruiterName || 'Hiring Manager')
    .replace(/\{\{job_title\}\}/g, jobTitle || 'Software Engineer')
    .replace(/\{\{company\}\}/g, company || 'your company');

  const subject = `Application Follow-Up: ${jobTitle} – Saurabh Kumar`;
  const defaultResume = resumePath || '/home/saurabh-kumar123/Desktop/Desktop/express/saurabh_resume.pdf';

  const rawMessage = createMimeMessage({
    to,
    subject,
    htmlBody: html,
    resumePath: defaultResume
  });

  const accessToken = await getAccessToken();

  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ raw: rawMessage });
    const req = https.request('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const body = JSON.parse(data);
          if (body.id) {
            console.log(`✅ [Outreach] Email successfully sent to ${to} (Message ID: ${body.id})`);
            tracker.recordRecruiterContact({
              name: recruiterName,
              email: to,
              jobTitle,
              company,
              channel: 'gmail_rest_api'
            });
            resolve({ success: true, messageId: body.id });
          } else {
            console.error(`❌ [Outreach] Gmail send failed:`, data);
            resolve({ success: false, error: data });
          }
        } catch (e) {
          reject(e);
        }
      });
    });

    req.on('error', err => {
      console.error(`❌ [Outreach] Request error:`, err.message);
      resolve({ success: false, error: err.message });
    });

    req.write(postData);
    req.end();
  });
}

/**
 * Generates personalized InMail text for LinkedIn messaging
 */
function getPersonalizedInMail({ recruiterName, jobTitle, company }) {
  const templatePath = path.join(__dirname, '../templates/recruiter_inmail.txt');
  let text = fs.readFileSync(templatePath, 'utf-8');
  return text
    .replace(/\{\{recruiter_name\}\}/g, recruiterName || 'Hiring Manager')
    .replace(/\{\{job_title\}\}/g, jobTitle || 'Software Engineer')
    .replace(/\{\{company\}\}/g, company || 'your company');
}

module.exports = {
  sendEmailOutreach,
  getPersonalizedInMail
};
