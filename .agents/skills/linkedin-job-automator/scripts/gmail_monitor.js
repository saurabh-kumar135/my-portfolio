const fs = require('fs');
const path = require('path');
const https = require('https');
const tracker = require('./tracker_manager');

// Load environment variables from StudyMate/.env or fallback paths
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
    throw new Error('Missing GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, or GMAIL_REFRESH_TOKEN in environment.');
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

function makeGmailApiRequest(endpoint, accessToken) {
  return new Promise((resolve, reject) => {
    const req = https.request(`https://gmail.googleapis.com/gmail/v1/users/me/${endpoint}`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Accept': 'application/json'
      }
    }, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const body = JSON.parse(data);
          resolve(body);
        } catch (e) {
          reject(new Error(`Failed to parse response: ${data.slice(0, 200)}`));
        }
      });
    });

    req.on('error', reject);
    req.end();
  });
}

function classifyEmailContent(subject, snippet) {
  const text = `${subject} ${snippet}`.toLowerCase();

  if (text.includes('interview') || text.includes('schedule a call') || text.includes('screening call') || text.includes('conversation with the team') || text.includes('shortlisted')) {
    return 'INTERVIEW_INVITATION';
  }
  if (text.includes('assessment') || text.includes('coding challenge') || text.includes('test link') || text.includes('hackerrank') || text.includes('codility')) {
    return 'CODING_ASSESSMENT';
  }
  if (text.includes('unfortunately') || text.includes('not moving forward') || text.includes('other candidates') || text.includes('pursuing other')) {
    return 'NOT_SELECTED';
  }
  if (text.includes('application was sent') || text.includes('application to') || text.includes('application received') || text.includes('thank you for applying') || text.includes('application confirmation')) {
    return 'APPLICATION_CONFIRMED';
  }
  if (text.includes('status update') || text.includes('next steps') || text.includes('offer')) {
    return 'STATUS_UPDATE';
  }
  return 'GENERAL_RECRUITER_INQUIRY';
}

async function checkJobResponses(options = {}) {
  const maxResults = options.limit || 20;
  console.log('📬 [Gmail Monitor] Checking inbox for recruiter responses & job leads...');

  try {
    const accessToken = await getAccessToken();
    const query = encodeURIComponent('subject:(interview OR application OR recruiter OR "status update" OR assessment OR shortlisted OR "next steps") newer_than:5d');
    const listRes = await makeGmailApiRequest(`messages?q=${query}&maxResults=${maxResults}`, accessToken);

    const messages = listRes.messages || [];
    console.log(`[Gmail Monitor] Found ${messages.length} recent candidate email threads.`);

    const newLeads = [];

    for (const item of messages) {
      const msg = await makeGmailApiRequest(`messages/${item.id}?format=metadata&metadataHeaders=Subject&metadataHeaders=From&metadataHeaders=Date`, accessToken);
      
      const headers = msg.payload?.headers || [];
      const getHeader = (name) => {
        const found = headers.find(h => h.name.toLowerCase() === name.toLowerCase());
        return found ? found.value : '';
      };

      const subject = getHeader('Subject');
      const from = getHeader('From');
      const date = getHeader('Date');
      const snippet = msg.snippet || '';

      const leadType = classifyEmailContent(subject, snippet);

      const leadRecord = {
        messageId: item.id,
        threadId: item.threadId,
        from,
        subject,
        date,
        snippet,
        leadType,
        detectedAt: new Date().toISOString()
      };

      tracker.recordEmailLead(leadRecord);
      newLeads.push(leadRecord);
    }

    if (options.output) {
      fs.writeFileSync(options.output, JSON.stringify(newLeads, null, 2), 'utf-8');
      console.log(`[Gmail Monitor] Lead data saved to: ${options.output}`);
    }

    const priorityLeads = newLeads.filter(l => l.leadType === 'INTERVIEW_INVITATION' || l.leadType === 'CODING_ASSESSMENT');
    if (priorityLeads.length > 0) {
      console.log(`\n🎉 [ALERT] ${priorityLeads.length} HIGH-PRIORITY JOB LEADS FOUND:`);
      priorityLeads.forEach((lead, i) => {
        console.log(`  ${i + 1}. [${lead.leadType}] ${lead.subject} | From: ${lead.from}`);
      });
    }

    return newLeads;
  } catch (err) {
    console.error('❌ [Gmail Monitor] Error checking job emails:', err.message);
    return [];
  }
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const outIdx = args.indexOf('--output');
  const outputPath = outIdx !== -1 ? args[outIdx + 1] : null;

  checkJobResponses({ output: outputPath }).then(leads => {
    console.log(`✅ Checked ${leads.length} email threads successfully.`);
    process.exit(0);
  }).catch(() => process.exit(1));
}

module.exports = { checkJobResponses };
