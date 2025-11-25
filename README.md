# Editing Text on the Website - User Manual

**UbuntuSelect Content Management System**

---

## Overview

The **Edit Website Text** feature allows administrators to edit text content on public pages (Home, About, Contact, Services), email templates, and approval workflows.

**User Stories:** US 12.01, US 12.02  
**Developed By:** Ankriti, Kanishk

---

## Quick Start

1. Log in as administrator
2. Go to Admin Dashboard → Click **"Manage Content"**
3. Select **"Pages"** tab → Choose a page (Home/About/Contact/Services)
4. Click **"Edit"** on any content item
5. Modify text → Click **"Save"**
6. Verify changes on the public website

---

## Step-by-Step Guide

### 1. Accessing Manage Content

#### Step 1: Log in and Navigate to Dashboard

1. Log in to UbuntuSelect with your administrator credentials
2. You'll be redirected to the Admin Dashboard
3. Locate the **"Manage Content"** card
4. Click on it to open the Manage Content page

**[IMAGE PLACEHOLDER 1: Admin Dashboard showing "Manage Content" card]**
- *Screenshot: Admin Dashboard with multiple management cards. "Manage Content" card should be visible and clearly labeled.*

#### Step 2: Understand the Interface

The Manage Content page has three tabs:
- **Pages** - Edit public page content (default)
- **Approvals** - Manage approval workflows
- **Email Templates** - Edit email templates

**[IMAGE PLACEHOLDER 2: Manage Content page showing three tabs]**
- *Screenshot: Top of Manage Content page showing hero section with title "Manage Content" and three tab buttons (Pages, Approvals, Email Templates) with "Pages" active.*

---

### 2. Editing Page Content

#### Step 1: Select a Page

1. Ensure **"Pages"** tab is selected
2. Below, you'll see filter pills: **Home**, **About**, **Contact**, **Services**
3. Click the page you want to edit (e.g., "Home")
4. The selected pill will be highlighted

**[IMAGE PLACEHOLDER 3: Page selection with filter pills]**
- *Screenshot: "Select Page" section showing four filter pills (Home, About, Contact, Services) arranged horizontally. One pill (e.g., "Home") should be highlighted/active.*

#### Step 2: View Content Items

After selecting a page, content items appear as cards showing:
- **Label** - Content name (e.g., "Hero Title")
- **Current Content** - Preview of existing text
- **Edit Button** - To start editing

**[IMAGE PLACEHOLDER 4: Content cards in view mode]**
- *Screenshot: Multiple content cards displayed vertically. Each card shows a label at top, preview box with text content, and "Edit" button at bottom. Show 2-3 cards to demonstrate the list structure.*

#### Step 3: Edit Content

1. Click **"Edit"** on the content card you want to modify
2. The card expands to show:
   - A **textarea** with current content
   - **Cancel** button (to discard)
   - **Save** button (to save changes)
3. Modify the text in the textarea
4. Click **"Save"** when done

**[IMAGE PLACEHOLDER 5: Content card in edit mode]**
- *Screenshot: Single content card in edit mode showing label at top, large textarea field with text, and "Cancel" and "Save" buttons at bottom. The Save button should be yellow/highlighted.*

#### Step 4: Verify Changes

After saving, the card returns to view mode showing your updated content.

**[IMAGE PLACEHOLDER 6: Content card showing updated content]**
- *Screenshot: Content card back in view mode displaying the updated text in the preview box. The text should be different from the original shown in image 4.*

---

### 3. Editing About Page Content

The About page has special section organization:

1. **Our Mission** - Mission-related content
2. **Our Core Values** - Displayed in a grid layout
3. **Let's Work Together** - Call-to-action content
4. **Other** - Additional content

**[IMAGE PLACEHOLDER 7: About page with organized sections]**
- *Screenshot: About page content showing organized sections. "Our Mission" section with cards in list, "Our Core Values" section with cards in grid layout (2-3 columns), and "Let's Work Together" section. The grid layout for Core Values should be clearly visible.*

Editing works the same way - click "Edit" on any card, modify text, and click "Save".

---

### 4. Editing Email Templates

#### Step 1: Select Email Templates Tab

1. Click the **"Email Templates"** tab
2. A list of email templates will load

**[IMAGE PLACEHOLDER 8: Email Templates tab]**
- *Screenshot: Email Templates tab active, showing list of email template cards. Each card shows template name (e.g., "Password Reset Email") and preview of email content.*

#### Step 2: Edit Template

1. Click **"Edit"** on the template you want to modify
2. Edit the text in the textarea
3. Click **"Save"** to update

> **⚠️ Important:** Some templates use variables like `{username}`, `{reset_link}` - don't remove these!

**[IMAGE PLACEHOLDER 9: Email template in edit mode]**
- *Screenshot: Email template card in edit mode showing textarea with email content. The content should show variables like `{username}` or `{reset_link}` highlighted or annotated to emphasize their importance.*

---

### 5. Managing Approvals

1. Click the **"Approvals"** tab
2. View approval-related content items
3. Edit using the same process: Click "Edit" → Modify → "Save"

**[IMAGE PLACEHOLDER 10: Approvals tab]**
- *Screenshot: Approvals tab active showing approval-related content cards (e.g., "Approval Pending Message", "Approval Rejected Notification").*

---

### 6. Viewing Your Changes

1. After saving, open the public website in a new tab
2. Navigate to the page you edited:
   - Home: `/`
   - About: `/about`
   - Contact: `/contact`
   - Services: `/services`
3. Verify your changes appear correctly
4. If not visible, refresh the page (F5 or Ctrl+R)

**[IMAGE PLACEHOLDER 11: Public page showing updated content]**
- *Screenshot: Public-facing website page (e.g., About page) displaying the updated content that was edited in the admin interface. Should show UbuntuSelect public website styling.*

---

## Troubleshooting

### Changes not saving?
- Check internet connection
- Verify you clicked "Save" (not "Cancel")
- Check browser console for errors (F12)
- Ensure you have admin/manager permissions

### Content not appearing on public page?
- Refresh the page (F5 or Ctrl+Shift+R for hard refresh)
- Clear browser cache
- Verify you edited the correct content item
- Check that page selection matches (e.g., "home" content shows on homepage)

### "Loading..." stuck?
- Check internet connection
- Verify backend API is running
- Check browser console for errors
- Try refreshing the page

### Can't find content item?
- Verify correct page is selected
- Scroll down to see more items
- Use browser search (Ctrl+F) to find specific text

**[IMAGE PLACEHOLDER 12: Browser console with error messages]**
- *Screenshot: Browser developer tools (F12) open showing Console tab with error messages. Helps users identify API or network issues.*

---

## Best Practices

✅ **Preview before publishing** - Review changes in admin interface first  
✅ **Test on public pages** - Always verify changes appear correctly  
✅ **Backup important content** - Copy original text before major changes  
✅ **Preserve email variables** - Don't remove `{username}`, `{reset_link}`, etc.  
✅ **Maintain consistency** - Keep tone and style consistent across pages  
✅ **Save frequently** - Don't leave edit mode open for long periods  

---

## Technical Details

### Supported Pages
- **Home** (`home`) - Homepage content
- **About** (`about`) - About page with section grouping
- **Contact** (`contact`) - Contact page content
- **Services** (`services`) - Services page content

### API Endpoints
- **Get Content:** `GET /api/site-texts/?page={pageName}`
- **Update Content:** `PATCH /api/site-texts/{id}/` with `{ "content": "new text" }`

### Permissions
- **Admin** and **Manager** roles can edit content
- **Public viewing** requires no authentication

### Content Formatting
- Line breaks are preserved
- Multiple spaces are maintained
- Content is stored as plain text (no HTML)

---

## Summary

The Edit Website Text feature provides a simple interface to manage website content:

1. ✅ Access Manage Content from Admin Dashboard
2. ✅ Select page and content item to edit
3. ✅ Modify text in textarea
4. ✅ Save changes
5. ✅ Verify on public website

---

**Last Updated:** [Date]  
**Version:** 1.0  
**Developed By:** Ankriti, Kanishk
