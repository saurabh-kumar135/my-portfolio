const fs = require('fs');
const path = require('path');

const TRACKER_PATH = path.join(__dirname, '../data/linkedin_tracker.json');

class TrackerManager {
  constructor(filePath = TRACKER_PATH) {
    this.filePath = filePath;
    this.data = this.load();
  }

  load() {
    try {
      if (fs.existsSync(this.filePath)) {
        const raw = fs.readFileSync(this.filePath, 'utf-8');
        return JSON.parse(raw);
      }
    } catch (err) {
      console.error('[Tracker] Error loading tracker file:', err.message);
    }
    return {
      last_run: null,
      total_runs: 0,
      posts_inspected: 0,
      jobs_found: 0,
      applications_submitted: 0,
      recruiters_contacted: 0,
      history: [],
      applications: {},
      recruiters: {},
      email_leads: [],
      processed_post_ids: [],
      processed_notifications: []
    };
  }

  save() {
    try {
      const dir = path.dirname(this.filePath);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      fs.writeFileSync(this.filePath, JSON.stringify(this.data, null, 2), 'utf-8');
    } catch (err) {
      console.error('[Tracker] Error saving tracker file:', err.message);
    }
  }

  isPostProcessed(postId) {
    if (!postId) return false;
    return (this.data.processed_post_ids || []).includes(postId);
  }

  recordPostId(postId) {
    if (!postId) return;
    if (!this.data.processed_post_ids) this.data.processed_post_ids = [];
    if (!this.data.processed_post_ids.includes(postId)) {
      this.data.processed_post_ids.push(postId);
      this.data.posts_inspected = (this.data.posts_inspected || 0) + 1;
      this.save();
    }
  }

  isJobApplied(jobUrl) {
    if (!jobUrl) return false;
    const cleanUrl = jobUrl.split('?')[0];
    const app = this.data.applications[cleanUrl];
    return !!app && app.status === 'submitted';
  }

  recordApplication(app) {
    const key = (app.jobUrl || app.postUrl || '').split('?')[0];
    if (!key) return;

    this.data.applications[key] = {
      title: app.title || 'Software Opportunity',
      company: app.company || 'Unknown',
      jobUrl: app.jobUrl || app.postUrl,
      appliedAt: new Date().toISOString(),
      status: app.status || 'applied',
      resumeUsed: app.resumeUsed || 'saurabh_resume.pdf',
      recruiter: app.recruiter || null,
      notes: app.notes || ''
    };

    this.data.applications_submitted = Object.keys(this.data.applications).length;
    this.save();
  }

  isRecruiterContacted(recruiterKey, role = '') {
    if (!recruiterKey) return false;
    const key = recruiterKey.trim().toLowerCase();
    const entry = this.data.recruiters[key];
    if (!entry) return false;
    if (role && entry.role && entry.role.toLowerCase() === role.toLowerCase()) {
      return true;
    }
    return true; // Already messaged this recruiter
  }

  recordRecruiterContact(contact) {
    const key = (contact.profileUrl || contact.email || contact.name || '').trim().toLowerCase();
    if (!key) return;

    this.data.recruiters[key] = {
      name: contact.name,
      profileUrl: contact.profileUrl || null,
      email: contact.email || null,
      company: contact.company || null,
      role: contact.jobTitle || null,
      channel: contact.channel || 'linkedin_dm',
      contactedAt: new Date().toISOString(),
      status: 'sent'
    };

    this.data.recruiters_contacted = Object.keys(this.data.recruiters).length;
    this.save();
  }

  recordEmailLead(lead) {
    if (!this.data.email_leads) this.data.email_leads = [];
    const exists = this.data.email_leads.some(l => l.messageId === lead.messageId);
    if (!exists) {
      this.data.email_leads.push({
        ...lead,
        recordedAt: new Date().toISOString()
      });
      this.save();
    }
  }

  recordRun(runSummary) {
    this.data.last_run = new Date().toISOString();
    this.data.total_runs = (this.data.total_runs || 0) + 1;
    if (!this.data.history) this.data.history = [];
    this.data.history.unshift({
      timestamp: this.data.last_run,
      ...runSummary
    });
    // Keep last 50 run logs
    if (this.data.history.length > 50) {
      this.data.history = this.data.history.slice(0, 50);
    }
    this.save();
  }

  getStats() {
    return {
      lastRun: this.data.last_run,
      totalRuns: this.data.total_runs || 0,
      postsInspected: this.data.processed_post_ids ? this.data.processed_post_ids.length : 0,
      applicationsCount: Object.keys(this.data.applications || {}).length,
      recruitersCount: Object.keys(this.data.recruiters || {}).length,
      emailLeadsCount: (this.data.email_leads || []).length
    };
  }
}

module.exports = new TrackerManager();
