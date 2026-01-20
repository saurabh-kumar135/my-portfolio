# Sourabh Kumar - Portfolio Website

A modern, responsive portfolio website showcasing your skills, experience, education, and projects.

## 🚀 Quick Start

1. Open `index.html` in your browser to view the portfolio
2. Edit the HTML file to add your content
3. Customize colors in `style.css` if needed

## 📝 How to Add Content

### 1. **Update Personal Information**

In `index.html`, find the Hero section and update:

- Your GitHub URL: Replace `https://github.com/yourusername`
- Your LinkedIn URL: Replace `https://linkedin.com/in/yourusername`
- Your Resume link: Replace `#` with your resume PDF link
- Your Email: Replace `your.email@example.com` in the Contact section

### 2. **Add Your Profile Picture**

- Save your profile picture as `profile.jpg` in the portfolio folder
- Or update the image path in line 48: `<img src="profile.jpg" alt="Sourabh Kumar">`

### 3. **Edit About Me Section**

Find the `<!-- About Me Section -->` and:

- Replace the placeholder text with your own description
- Update the research topics in the `topics-grid`

### 4. **Add Experience**

To add a new job/internship:

```html
<div class="timeline-item">
  <div class="timeline-header">
    <h3 class="job-title">Software Developer - ABC Company</h3>
    <span class="job-duration">Jan 2024 - Present</span>
  </div>
  <p class="job-description">
    Developed full-stack web applications using MERN stack. Implemented RESTful
    APIs and improved application performance by 40%.
  </p>
  <div class="job-tags">
    <span class="tag">React</span>
    <span class="tag">Node.js</span>
    <span class="tag">MongoDB</span>
    <span class="tag">Express</span>
  </div>
</div>
```

**Steps:**

1. Find the `<!-- Experience Section -->` in `index.html`
2. Copy the `timeline-item` block (lines 105-120)
3. Paste it above or below existing items
4. Update the job title, company, duration, description, and tags
5. Remove the empty-state div when you add real experiences

### 5. **Add Education**

Your B.Tech is already added. To add more (12th, 10th):

```html
<div class="education-card">
  <div class="education-header">
    <h3>Senior Secondary (XII)</h3>
    <span class="education-year">2019 - 2021</span>
  </div>
  <p class="institution">Your School Name</p>
  <p class="affiliation">CBSE Board</p>
  <div class="education-details">
    <p><strong>Stream:</strong> Science (PCM)</p>
    <p><strong>Percentage:</strong> 95%</p>
  </div>
</div>
```

**Steps:**

1. Find the `<!-- Education Section -->` in `index.html`
2. Copy the `education-card` block (lines 158-169)
3. Paste it in the `education-grid`
4. Update school name, year, board, and percentage

### 6. **Add Projects**

To add a new project:

```html
<div class="project-card">
  <div class="project-image">
    <img src="project-studymate.jpg" alt="StudyMate" />
  </div>
  <div class="project-content">
    <div class="project-tags">
      <span class="tag">React</span>
      <span class="tag">Node.js</span>
      <span class="tag">MongoDB</span>
      <span class="tag">Gemini AI</span>
    </div>
    <h3 class="project-title">StudyMate - AI Learning Platform</h3>
    <p class="project-description">
      An AI-powered study platform with features like AI tutor, quiz generation,
      and document summarization using Gemini API.
    </p>
    <div class="project-links">
      <a
        href="https://github.com/yourusername/studymate"
        class="project-link"
        target="_blank"
      >
        <i class="fab fa-github"></i> Code
      </a>
      <a href="https://studymate-demo.com" class="project-link" target="_blank">
        <i class="fas fa-external-link-alt"></i> Live Demo
      </a>
    </div>
  </div>
</div>
```

**Steps:**

1. Find the `<!-- Projects Section -->` in `index.html`
2. Copy the `project-card` block (lines 186-209)
3. Paste it in the `projects-grid`
4. Add project image to the portfolio folder
5. Update project name, description, tags, and links
6. Remove the empty-state div when you add real projects

### 7. **Add Project Images**

- Save project screenshots/images in the portfolio folder
- Name them descriptively (e.g., `project-studymate.jpg`, `project-ecommerce.jpg`)
- Update the `src` attribute in the project card

## 🎨 Customization

### Change Colors

Edit `style.css` and modify the CSS variables:

```css
:root {
  --primary-color: #e91e63; /* Pink */
  --secondary-color: #9c27b0; /* Purple */
  --bg-dark: #0a0a0a; /* Background */
  --bg-card: #1a1a1a; /* Card background */
}
```

### Change Fonts

Add Google Fonts in `index.html` `<head>`:

```html
<link
  href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap"
  rel="stylesheet"
/>
```

Then update in `style.css`:

```css
body {
  font-family: "Poppins", sans-serif;
}
```

## 📱 Responsive Design

The portfolio is fully responsive and works on:

- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (< 768px)

## 🌐 Deployment

### Option 1: GitHub Pages

1. Create a GitHub repository
2. Push your portfolio files
3. Go to Settings → Pages
4. Select main branch and save
5. Your site will be live at `https://yourusername.github.io/portfolio`

### Option 2: Netlify

1. Sign up at netlify.com
2. Drag and drop your portfolio folder
3. Your site will be live instantly

### Option 3: Vercel

1. Sign up at vercel.com
2. Import your GitHub repository
3. Deploy with one click

## 📋 Checklist

Before publishing, make sure to:

- [ ] Add your profile picture
- [ ] Update all social media links
- [ ] Add your resume PDF
- [ ] Fill in About Me section
- [ ] Add at least 2-3 experiences
- [ ] Add education details (12th, 10th)
- [ ] Add at least 3-5 projects with images
- [ ] Update contact email
- [ ] Test on mobile devices
- [ ] Check all links work
- [ ] Optimize images (compress them)

## 🛠️ Technologies Used

- HTML5
- CSS3 (with CSS Grid and Flexbox)
- JavaScript (ES6+)
- Font Awesome Icons

## 📞 Need Help?

If you need help adding content or customizing the portfolio:

1. Check the HTML comments (marked with `<!-- EDIT THIS -->`)
2. Follow the examples provided in each section
3. Test changes by refreshing your browser

## 📄 License

Feel free to use this template for your personal portfolio!

---

**Created for Sourabh Kumar** | Full Stack Web Developer & ML Engineer
