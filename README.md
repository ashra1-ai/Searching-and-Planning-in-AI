# Client Testimonials - User Manual

**UbuntuSelect Client Testimonial Submission**

---

## Overview

The **Client Testimonials** feature allows clients to submit reviews/testimonials for artists they've worked with. Testimonials are displayed on the artist's profile and the artist receives a notification when a new testimonial is submitted.

**User Story:** US 9.01  
**Developed By:** Ankriti, Kanishk

---

## Quick Start

1. Log in as a client
2. Navigate to an artist's profile page
3. Click the **"Reviews"** tab
4. Click **"Write a Testimonial"** button
5. Fill in your name/organization and testimonial text
6. Click **"Submit Testimonial"**

**[IMAGE PLACEHOLDER 0: Login page as client]**
- *Screenshot: Login page showing the login form. The user should be logging in with client credentials. The form should show email/password fields and a "Login" button.*

---

## Step-by-Step Guide

### 1. Accessing the Reviews Tab

#### Step 1: Navigate to Artist Profile

1. Log in to UbuntuSelect with your client account credentials
2. Navigate to an artist's profile page (e.g., `/artists/{artist-id}`)
3. You should see the artist's profile with tabs: About, Portfolio, Feed, Schedule, **Reviews**

**[IMAGE PLACEHOLDER 1: Artist profile page with Reviews tab visible]**
- *Screenshot: Artist profile page showing the tab navigation bar with "Reviews" tab clearly visible. The page should show the artist's banner, profile picture, and name. The user should be logged in as a client.*

**[IMAGE PLACEHOLDER 1A: Full artist profile view from client perspective]**
- *Screenshot: Complete artist profile page view showing the banner, profile picture, artist name, genres, location, and all tabs (About, Portfolio, Feed, Schedule, Reviews) in the navigation bar. This shows the full context before navigating to Reviews.*

#### Step 2: Open Reviews Tab

1. Click on the **"Reviews"** tab
2. The Reviews tab will open, showing existing testimonials (if any)
3. You'll see a **"Write a Testimonial"** button if you're logged in as a client

**[IMAGE PLACEHOLDER 2: Reviews tab with Write a Testimonial button]**
- *Screenshot: Reviews tab open showing the "Testimonials" heading, a "Write a Testimonial" button centered at the top, and any existing testimonials displayed below. The page should clearly indicate this is the Reviews/Testimonials section.*

**[IMAGE PLACEHOLDER 2A: Loading state in Reviews tab]**
- *Screenshot: Reviews tab showing "Loading testimonials..." message. This appears briefly while testimonials are being fetched from the server.*

---

### 2. Writing a Testimonial

#### Step 1: Click "Write a Testimonial"

1. Click the **"Write a Testimonial"** button
2. The form will expand below the button
3. The button will change to **"Cancel"** (you can click it to close the form)

**[IMAGE PLACEHOLDER 3: Testimonial form opened]**
- *Screenshot: Reviews tab showing the testimonial form expanded. The form should display "Share your experience" heading, an input field for "Your Name / Organization", a textarea for "Your Testimonial", and a "Submit Testimonial" button. The "Cancel" button should be visible above the form.*

**[IMAGE PLACEHOLDER 3A: Cancel button closing the form]**
- *Screenshot: Reviews tab showing the "Cancel" button being clicked or the form being closed. The form should collapse and the "Write a Testimonial" button should reappear. This demonstrates how to cancel without submitting.*

#### Step 2: Fill in Your Information

1. **Your Name / Organization** (Required)
   - Enter your name or organization name
   - Example: "John Doe" or "ABC Events"
   - **Note:** The author name displayed on the testimonial will be taken from your logged-in account name, not from this field

2. **Your Testimonial** (Required)
   - Enter your review/testimonial text
   - Share your experience working with the artist
   - Be honest and helpful for other clients

**[IMAGE PLACEHOLDER 4: Filled testimonial form]**
- *Screenshot: Testimonial form with sample data filled in. The "Your Name / Organization" field should show "John Doe" or similar, and the "Your Testimonial" textarea should contain sample testimonial text like "This artist was amazing! Highly professional and great performance." Both fields should be clearly visible and filled.*

#### Step 3: Submit Your Testimonial

1. Review your testimonial to ensure it's accurate and complete
2. Click the **"Submit Testimonial"** button
3. The form will close and your testimonial will appear in the list
4. The artist will receive a notification about your testimonial

**[IMAGE PLACEHOLDER 5: Testimonial submitted and displayed]**
- *Screenshot: Reviews tab after submission showing the new testimonial card displayed at the top of the testimonials list. The testimonial card should show the author name, date, and the testimonial text in quotes. The form should be closed and the "Write a Testimonial" button should be visible again.*

**[IMAGE PLACEHOLDER 5A: Submit button in loading state]**
- *Screenshot: Testimonial form showing the "Submit Testimonial" button in a disabled/loading state while the submission is being processed. This indicates the system is saving the testimonial.*

---

### 3. Viewing Testimonials

#### Step 1: See All Testimonials

1. All testimonials are displayed in the Reviews tab
2. Each testimonial shows:
   - **Author name** (or organization)
   - **Date** the testimonial was submitted
   - **Testimonial text** (in quotes)

2. Testimonials are displayed in reverse chronological order (newest first)

**[IMAGE PLACEHOLDER 6: Multiple testimonials displayed]**
- *Screenshot: Reviews tab showing multiple testimonial cards. Each card should display the author name, date, and testimonial text. The cards should be stacked vertically with clear separation. The newest testimonial should appear at the top.*

**[IMAGE PLACEHOLDER 6A: Single testimonial card close-up]**
- *Screenshot: Close-up view of a single testimonial card showing the structure: author name at the top, date on the right side, and the testimonial text in quotes below. This shows the detailed layout of each testimonial.*

#### Step 2: Empty State

If no testimonials exist yet:
- You'll see: **"No testimonials yet. Be the first to write one!"**
- This encourages clients to be the first to leave a review

**[IMAGE PLACEHOLDER 7: Empty testimonials section]**
- *Screenshot: Reviews tab with no testimonials showing the empty state message "No testimonials yet. Be the first to write one!" centered on the page. The "Write a Testimonial" button should still be visible.*

---

## Important Notes

### Who Can Submit Testimonials?

- ✅ **Clients** - Can submit testimonials when viewing any artist's profile
- ❌ **Artists** - Cannot submit testimonials (they can only view and delete their own testimonials)
- ❌ **Visitors** - Must log in as a client to submit testimonials

### Testimonial Display

- Testimonials are **public** - visible to all visitors, clients, and the artist
- Testimonials appear on the artist's profile in the **Reviews** tab
- The author name displayed is automatically taken from your logged-in account name (from your user profile)

### Artist Actions

- Artists can **delete** testimonials on their own profile
- Artists receive a **notification** when a new testimonial is submitted

**[IMAGE PLACEHOLDER 9: Artist view of testimonials with delete button]**
- *Screenshot: Reviews tab viewed by the artist (logged in as artist). Each testimonial card should show a "Delete" button at the bottom. This demonstrates that artists can manage testimonials on their profile.*

**[IMAGE PLACEHOLDER 10: Artist notification for new testimonial]**
- *Screenshot: Artist's notification panel or notification list showing a new notification with type "Testimonial", title "New Testimonial", and description "{Client Name} left you a testimonial". This shows how artists are notified when clients submit testimonials.*

---

## Troubleshooting

### "Write a Testimonial" button not visible?
- **Solution:** Ensure you're logged in as a client (not as an artist or visitor)
- Check that you're viewing the Reviews tab (not another tab)
- Refresh the page if the button doesn't appear

### Testimonial not submitting?
- **Check Required Fields:** Ensure both "Your Name / Organization" and "Your Testimonial" fields are filled
- **Check Internet:** Verify you have a stable internet connection
- **Try Again:** Click "Submit Testimonial" again - the button may show a loading state
- **Check Console:** Open browser developer tools (F12) to check for errors

**[IMAGE PLACEHOLDER 11: Error message in form]**
- *Screenshot: Testimonial form showing an error message, such as "Failed to submit testimonial" or validation errors. This helps users understand what went wrong when submission fails.*

### Testimonial not appearing after submission?
- **Wait a moment:** The page may need a moment to refresh
- **Refresh Page:** Try refreshing the page to see your testimonial
- **Check Tab:** Ensure you're still on the Reviews tab

### Can't see the Reviews tab?
- **Verify URL:** Make sure you're on an artist's profile page (not your own profile)
- **Check Navigation:** The Reviews tab should be in the tab navigation bar below the artist's header

**[IMAGE PLACEHOLDER 8: Browser console showing errors]**
- *Screenshot: Browser developer tools (F12) open showing the Console tab with error messages. This helps users identify API or network issues when testimonial submission fails.*

**[IMAGE PLACEHOLDER 12: Visitor view of testimonials (no submit button)]**
- *Screenshot: Reviews tab viewed by a visitor (not logged in). Testimonials should be visible, but the "Write a Testimonial" button should NOT be present. This shows that only logged-in clients can submit testimonials.*


---

## Technical Details

### Form Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Your Name / Organization** | Text | ✅ Yes | Form field (author name comes from logged-in account) |
| **Your Testimonial** | Text | ✅ Yes | Review/testimonial content |


### Permissions

- **Clients** - Can create testimonials for any artist
- **Artists** - Can view and delete testimonials on their own profile
- **Visitors** - Can view testimonials but cannot submit

### Notifications

- When a client submits a testimonial, the artist receives a notification
- Notification type: "Testimonial"
- Notification title: "New Testimonial"
- Notification description: "{Client Name} left you a testimonial"

---

## Summary

The Client Testimonials feature allows clients to:

1. ✅ Navigate to an artist's profile and open the Reviews tab
2. ✅ Click "Write a Testimonial" to open the form
3. ✅ Fill in name/organization and testimonial text
4. ✅ Click "Submit Testimonial" to publish
5. ✅ View all testimonials displayed on the artist's profile

The artist receives a notification when a new testimonial is submitted.

---

**Last Updated:** [Date]  
**Version:** 1.0  
**Developed By:** Ankriti, Kanishk

