# Artist Profile Editing - User Manual

**UbuntuSelect Artist Profile Management**

---

## Overview

The **Artist Profile Editing** feature allows artists to edit and update their profile information, including biography, social media links, genres, location, and more.

**User Stories:** US 4.04, US 4.06, US 4.07, US 4.08  
**Developed By:** Kanishk

---

## Quick Start

1. Log in as an artist
2. Navigate to your artist profile page
3. Click **"Edit Profile"** button
4. Make your changes
5. Click **"Save"** to update or **"Cancel"** to discard

---

## Step-by-Step Guide

### 1. Accessing Your Profile

#### Step 1: Log in and Navigate to Your Profile

1. Log in to UbuntuSelect with your artist account credentials
2. Navigate to your artist profile page (e.g., `/artists/{your-artist-id}`)
3. You should see your profile with banner image, profile picture, and profile information
4. Look for the **"Edit Profile"** button in the header area

> **💡 Note:** The "Edit Profile" button only appears when you're viewing your own profile. If you're viewing another artist's profile, you'll see a "Follow" button instead.

**[IMAGE PLACEHOLDER 1: Artist profile page with "Edit Profile" button visible]**
- *Screenshot: Artist profile page showing the banner, profile picture, artist name, and the "Edit Profile" button clearly visible in the header actions area. The page should show "Viewing as: ARTIST" indicator (if in dev mode).*

---

### 2. Entering Edit Mode

#### Step 1: Click "Edit Profile"

1. Click the **"Edit Profile"** button
2. The page will enter edit mode
3. You'll see an **"EDITING MODE"** badge appear
4. Editable fields will change from display text to input fields

**[IMAGE PLACEHOLDER 2: Profile in edit mode showing editable fields]**
- *Screenshot: Artist profile page in edit mode. The "Edit Profile" button should be replaced with "Save" and "Cancel" buttons. An "EDITING MODE" badge should be visible. Input fields should be shown for Display Name, Stage Name, Genres, Medium, and Location in the header area.*

---

### 3. Editing Profile Information

#### Step 1: Edit Header Information

In the profile header, you can edit:

1. **Display Name** (Required)
   - This is your primary name shown on your profile
   - Field is marked with an asterisk or validation
   - Cannot be empty

2. **Stage Name** (Optional)
   - Your performance/stage name
   - Displayed in quotes below your display name
   - Can be left empty

3. **Genres** (Comma-separated)
   - Enter genres separated by commas (e.g., "Jazz, Rock, Blues")
   - Each genre will be displayed with bullet separators

4. **Medium/Instrument**
   - Your primary medium or instrument (e.g., "Vocals", "Guitar", "Band")

5. **Location**
   - Your city/location (e.g., "Toronto, ON")

**[IMAGE PLACEHOLDER 3: Header fields in edit mode]**
- *Screenshot: Close-up of the profile header showing all editable input fields: Display Name (with focus/active state), Stage Name, Genres (comma-separated input), Medium, and Location. The fields should be clearly labeled and visible.*

#### Step 2: Edit About/Biography

1. Navigate to the **"About"** tab (should be active by default)
2. Scroll to the "About {Your Name}" section
3. In edit mode, you'll see a large textarea instead of the biography text
4. Edit your biography/description
5. Add details about your artistic journey, style, and what makes your performances special

**[IMAGE PLACEHOLDER 4: Biography textarea in edit mode]**
- *Screenshot: About tab showing the biography section in edit mode. A large textarea should be visible with placeholder text like "Tell your story... share your journey as an artist...". Help text should be visible below explaining the purpose.*

#### Step 3: Add Social Media Links

1. Scroll to the **"Social Links"** section in the About tab
2. In edit mode, you'll see a textarea for social media links
3. Enter one link per line:
   ```
   instagram.com/yourpage
   facebook.com/yourpage
   twitter.com/yourpage
   yourwebsite.com
   ```
4. Links can be entered with or without `https://` - the system will add it automatically

**[IMAGE PLACEHOLDER 5: Social links textarea in edit mode]**
- *Screenshot: Social Links section in edit mode showing a textarea with placeholder text demonstrating the format (one link per line). Help text should explain the format. Sample links should be visible in the placeholder.*

#### Step 4: Add Spotify URL (Optional)

1. Scroll to the **"Music on Spotify"** section
2. In edit mode, you'll see an input field for Spotify Artist URL
3. Paste your Spotify artist profile URL (e.g., `https://open.spotify.com/artist/...`)
4. This enables music embedding on your profile

**[IMAGE PLACEHOLDER 6: Spotify URL input field]**
- *Screenshot: Music on Spotify section in edit mode showing an input field with placeholder "https://open.spotify.com/artist/...". Help text should explain how to get the URL.*

---

### 4. Saving Your Changes

#### Step 1: Review Your Changes

1. Review all the changes you've made
2. Ensure the **Display Name** field is not empty (required field)
3. Check that all information is correct

#### Step 2: Save or Cancel

1. **To Save:**
   - Click the **"Save"** button (typically green/accent colored)
   - Your changes will be saved to the server
   - The page will exit edit mode and show your updated profile

2. **To Cancel:**
   - Click the **"Cancel"** button (typically red/danger colored)
   - All changes will be discarded
   - The page will return to view mode with original content

**[IMAGE PLACEHOLDER 7: Save and Cancel buttons]**
- *Screenshot: Profile header showing "Save" and "Cancel" buttons side by side. The Save button should be highlighted/accent colored, and Cancel should be danger/red colored. The buttons should be clearly visible and clickable.*

#### Step 3: Validation Errors

If you try to save without a Display Name:
- An error message will appear: "Display Name is required."
- The Display Name field will be highlighted
- The cursor will automatically focus on the Display Name field
- You must enter a Display Name before saving

**[IMAGE PLACEHOLDER 8: Validation error for Display Name]**
- *Screenshot: Profile in edit mode showing a validation error message "Display Name is required." below the Display Name input field. The field should be highlighted in red or have an error border. The error message should be clearly visible.*

---

### 5. Viewing Your Updated Profile

#### Step 1: Verify Changes

1. After saving, the page automatically exits edit mode
2. Your updated information will be displayed
3. Check that:
   - Display name is updated
   - Biography shows your new text
   - Social links are displayed as clickable links
   - Genres, medium, and location are correct

**[IMAGE PLACEHOLDER 9: Updated profile in view mode]**
- *Screenshot: Artist profile page back in view mode showing all the updated information. The Display Name should show the new value, biography should display the updated text, and social links should be visible as clickable links. The profile should look complete and professional.*

#### Step 2: Check Public View

1. Open your profile in an incognito/private window or log out
2. Navigate to your artist profile as a visitor
3. Verify that all changes are visible to the public
4. Test that social media links work correctly

**[IMAGE PLACEHOLDER 10: Public view of updated profile]**
- *Screenshot: Artist profile viewed as a visitor (not logged in or different account). The profile should show all updated information. Social links should be visible and the biography should display the updated text. This demonstrates how clients/visitors see the profile.*

---

## Editing Different Sections

### About Tab
- **Biography** - Edit your story and artistic journey
- **Social Links** - Add Instagram, Facebook, Twitter, website links
- **Spotify URL** - Link your Spotify artist profile

### Other Tabs (Not Editable in This Feature)
- **Portfolio** - Media uploads (separate feature)
- **Feed** - Posts and updates (separate feature)
- **Schedule** - Calendar and events (separate feature)
- **Reviews** - Client testimonials (read-only for artists)

---

## Troubleshooting

### "Edit Profile" button not visible?
- **Solution:** Ensure you're logged in as an artist and viewing your own profile (not another artist's profile)
- Check that your user role is "artist"
- Verify you're on the correct profile URL

### Changes not saving?
- **Check Display Name:** Ensure the Display Name field is not empty (required field)
- **Check Internet:** Verify you have a stable internet connection
- **Try Again:** Click "Save" again - the button may show a loading state
- **Check Console:** Open browser developer tools (F12) to check for errors

### Social links not displaying?
- **Format:** Ensure each link is on a separate line in the textarea
- **Valid URLs:** Make sure links are in a valid format
- **Save First:** Remember to click "Save" after adding links

### Biography text not updating?
- **Verify Tab:** Make sure you're editing in the "About" tab
- **Check Save:** Ensure you clicked "Save" (not just closed edit mode)
- **Refresh:** Try refreshing the page to see updates

**[IMAGE PLACEHOLDER 11: Browser console showing errors]**
- *Screenshot: Browser developer tools (F12) open showing the Console tab with error messages. This helps users identify API or network issues when saves fail.*

---

## Best Practices

✅ **Keep Display Name Professional** - This is the primary name clients see  
✅ **Write a Compelling Biography** - Share your story and what makes you unique  
✅ **Add All Social Links** - Help clients find you on different platforms  
✅ **Use Accurate Genres** - Helps clients find you in searches  
✅ **Update Location** - Important for local bookings  
✅ **Save Frequently** - Don't lose your work if the page refreshes  
✅ **Preview Before Publishing** - Check how your profile looks to visitors  

---

## Technical Details

### Editable Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Display Name** | Text | ✅ Yes | Primary name shown on profile |
| **Stage Name** | Text | ❌ No | Performance/stage name |
| **Genres** | Array | ❌ No | Comma-separated list of genres |
| **Medium** | Text | ❌ No | Primary medium or instrument |
| **Location** | Text | ❌ No | City/location |
| **About/Biography** | Text | ❌ No | Artist story and description |
| **Social Links** | Array | ❌ No | One link per line |
| **Spotify URL** | URL | ❌ No | Spotify artist profile URL |

### API Endpoint

- **Update Profile:** `PATCH /api/artist/artist/{id}/`
- **Allowed Fields:** `stage_name`, `about`, `genres`, `medium`, `location`, `social_links`, `spotify_url`

### Permissions

- Only the artist who owns the profile can edit it
- Artists cannot edit other artists' profiles
- Changes are immediately visible to all visitors

---

## Summary

The Artist Profile Editing feature provides a simple interface to manage your profile:

1. ✅ Click "Edit Profile" on your artist profile
2. ✅ Edit Display Name, Biography, Social Links, and more
3. ✅ Ensure Display Name is filled (required)
4. ✅ Click "Save" to update or "Cancel" to discard
5. ✅ Verify changes are visible on your public profile

---

**Last Updated:** [Date]  
**Version:** 1.0  
**Developed By:** Kanishk

