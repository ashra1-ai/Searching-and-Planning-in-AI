# Forgot Password Feature - User Manual

## Overview

The Forgot Password feature allows users (artists, clients, and admins) to reset their password if they have forgotten it. The system sends a secure reset link to the user's registered email address, which they can use to create a new password.

**User Stories:**
- **US 3.02** - Artist reset password
- **US 8.03** - Client reset password

---

## Table of Contents

1. [Requesting a Password Reset](#1-requesting-a-password-reset)
2. [Receiving the Reset Email](#2-receiving-the-reset-email)
3. [Resetting Your Password](#3-resetting-your-password)
4. [Handling Invalid or Expired Tokens](#4-handling-invalid-or-expired-tokens)
5. [Technical Details](#5-technical-details)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Requesting a Password Reset

### Step 1: Navigate to Login Page

1. Open your web browser and navigate to the UbuntuSelect login page.
2. You will see the login form with fields for Username and Password.

**[IMAGE PLACEHOLDER 1: Login page showing the login form with "Forgot password?" link]**

### Step 2: Click "Forgot password?"

1. On the login page, locate the "Forgot password?" link next to the Password field.
2. Click the "Forgot password?" button.

**[IMAGE PLACEHOLDER 2: Close-up of the "Forgot password?" button/link on the login page]**

### Step 3: Enter Your Email Address

1. A modal dialog will appear with the title "Reset Password".
2. Enter the email address associated with your UbuntuSelect account in the Email field.
3. Click the "Send Link" button.

**[IMAGE PLACEHOLDER 3: Reset Password modal showing the email input field and Send Link button]**

### Step 4: Confirmation Message

1. After clicking "Send Link", you will see a confirmation message:
   - **Success**: "If the email exists, a reset link was sent."
   - **Error**: "Unable to request reset right now."

2. **Note**: For security reasons, the system will show the same success message whether the email exists or not. This prevents attackers from discovering which email addresses are registered.

**[IMAGE PLACEHOLDER 4: Reset Password modal showing the success confirmation message]**

### Step 5: Close the Modal (Optional)

- Click the "Cancel" button or press the **Escape** key to close the modal and return to the login page.

---

## 2. Receiving the Reset Email

### Step 1: Check Your Email Inbox

1. Open your email application or webmail service.
2. Look for an email from UbuntuSelect with the subject: **"UbuntuSelect — Password Reset Request"**
3. The email may take a few minutes to arrive. Check your spam/junk folder if you don't see it.

**[IMAGE PLACEHOLDER 5: Email inbox showing the password reset email from UbuntuSelect]**

### Step 2: Open the Reset Email

1. Open the password reset email.
2. The email will contain:
   - A greeting with your username
   - Instructions about the password reset request
   - A reset link (URL) that looks like: `http://localhost:5173/password-reset/reset/{tokenId}`

**[IMAGE PLACEHOLDER 6: Password reset email content showing the reset link]**

### Step 3: Click the Reset Link

1. Click on the reset link provided in the email.
2. This will open your web browser and navigate to the password reset page.

**Important Security Notes:**
- The reset link is valid for **24 hours** from the time it was created.
- Each reset link can only be used **once**.
- If you request multiple password resets, only the most recent link will be valid (previous links are automatically revoked).

---

## 3. Resetting Your Password

### Step 1: Token Validation

1. After clicking the reset link, the system will automatically validate the token.
2. You will see a "Validating token..." message while the system checks if the link is valid.

**[IMAGE PLACEHOLDER 7: Password reset page showing "Validating token..." message]**

### Step 2: Enter New Password

1. If the token is valid, you will see a form titled "Create a New Password".
2. Enter your new password in the "New password" field.
   - **Requirements**: Password must be at least 8 characters long.
   - The field shows a placeholder: "Minimum 8 characters"

**[IMAGE PLACEHOLDER 8: Password reset form showing the "New password" input field]**

### Step 3: Confirm New Password

1. Re-enter your new password in the "Confirm password" field to verify it matches.
   - The field shows a placeholder: "Re-enter password"
2. The system will validate that both passwords match before allowing submission.

**[IMAGE PLACEHOLDER 9: Password reset form showing both password fields filled in]**

### Step 4: Submit New Password

1. Click the "Set New Password" button.
2. The button will show "Submitting..." while the request is being processed.

**[IMAGE PLACEHOLDER 10: Password reset form with "Set New Password" button highlighted]**

### Step 5: Success and Redirect

1. Upon successful password reset, you will see a success message:
   - "Password successfully changed. Redirecting to login..."
2. After approximately 1.4 seconds, you will be automatically redirected to the login page.
3. You can now log in with your new password.

**[IMAGE PLACEHOLDER 11: Success message on password reset page showing "Password successfully changed. Redirecting to login..."]**

---

## 4. Handling Invalid or Expired Tokens

### Scenario 1: Expired Token

If your reset link has expired (older than 24 hours), you will see:

1. An error message: "This reset link is invalid or expired."
2. A form to request a new reset link.

**[IMAGE PLACEHOLDER 12: Password reset page showing expired token error message]**

### Scenario 2: Already Used Token

If you try to use a reset link that has already been used, you will see:

1. An error message indicating the token has already been used.
2. A form to request a new reset link.

**[IMAGE PLACEHOLDER 13: Password reset page showing "token already used" error message]**

### Scenario 3: Invalid Token

If the token in the URL is malformed or doesn't exist, you will see:

1. An error message: "This reset link is invalid or expired."
2. A form to request a new reset link.

### Requesting a New Reset Link

1. When you see an error message, you can request a new reset link directly from the same page.
2. Enter your email address in the provided form.
3. Click "Send Link" to receive a new reset email.
4. You can also click "Cancel" to return to the login page.

**[IMAGE PLACEHOLDER 14: Password reset page showing the form to request a new reset link after token error]**

---

## 5. Technical Details

### Password Requirements

- **Minimum Length**: 8 characters
- **Validation**: Passwords must match in both "New password" and "Confirm password" fields

### Token Security

- **Token Format**: UUID (Universally Unique Identifier)
- **Expiration**: 24 hours from creation
- **Single Use**: Each token can only be used once
- **Automatic Revocation**: When a new reset is requested, all previous unused tokens for that user are automatically revoked

### API Endpoints

The forgot password feature uses the following backend API endpoints:

1. **Request Password Reset**
   - `POST /auth/password-reset/request/`
   - Body: `{ "email": "user@example.com" }`

2. **Validate Reset Token**
   - `GET /auth/password-reset/validate/{tokenId}/`
   - Returns: `{ "valid": true/false, "username": "...", "email": "..." }`

3. **Complete Password Reset**
   - `POST /auth/password-reset/reset/{tokenId}/`
   - Body: `{ "password": "newpassword", "confirm_password": "newpassword" }`

### Frontend Routes

- **Login Page**: `/login`
- **Password Reset Page**: `/password-reset/reset/{tokenId}`

### Email Configuration

The system uses Django's email backend to send password reset emails. The email includes:
- Subject: "UbuntuSelect — Password Reset Request"
- Recipient: The email address associated with the account
- Content: A personalized message with the reset link

---

## 6. Troubleshooting

### Problem: I didn't receive the reset email

**Solutions:**
1. Check your spam/junk folder - the email may have been filtered.
2. Wait a few minutes - email delivery can sometimes be delayed.
3. Verify you're using the correct email address associated with your account.
4. Check if your email provider is blocking emails from the UbuntuSelect domain.
5. Try requesting a new reset link.

**[IMAGE PLACEHOLDER 15: Troubleshooting section visual - email not received]**

### Problem: The reset link says "Invalid or expired token"

**Solutions:**
1. The link may have expired (valid for 24 hours only).
2. The link may have already been used (each link can only be used once).
3. You may have requested a new reset link, which automatically invalidated the old one.
4. **Solution**: Request a new reset link using the form on the error page.

**[IMAGE PLACEHOLDER 16: Troubleshooting section visual - invalid token]**

### Problem: "Passwords do not match" error

**Solutions:**
1. Ensure both password fields contain exactly the same text.
2. Check for extra spaces before or after the password.
3. Make sure your password is at least 8 characters long.

**[IMAGE PLACEHOLDER 17: Troubleshooting section visual - password mismatch error]**

### Problem: "Password must be at least 8 characters" error

**Solutions:**
1. Your new password must be at least 8 characters long.
2. Count the characters in your password to ensure it meets the requirement.
3. Consider using a combination of letters, numbers, and special characters for better security.

**[IMAGE PLACEHOLDER 18: Troubleshooting section visual - password too short error]**

### Problem: "Unable to request reset right now" error

**Solutions:**
1. Check your internet connection.
2. The server may be temporarily unavailable - try again in a few minutes.
3. Contact support if the problem persists.

### Problem: I'm stuck on "Validating token..." screen

**Solutions:**
1. Check your internet connection.
2. Refresh the page.
3. The token may be invalid - try requesting a new reset link.
4. Clear your browser cache and cookies, then try again.

---

## Security Best Practices

1. **Never share your reset link** - Reset links are personal and should not be shared with anyone.
2. **Use the link promptly** - Reset links expire after 24 hours for security reasons.
3. **Choose a strong password** - Use a combination of uppercase, lowercase, numbers, and special characters.
4. **Don't reuse passwords** - Use a unique password for your UbuntuSelect account.
5. **Check the URL** - Ensure you're on the official UbuntuSelect domain before entering your new password.

---

## Summary

The Forgot Password feature provides a secure way to reset your account password:

1. ✅ Click "Forgot password?" on the login page
2. ✅ Enter your email address
3. ✅ Check your email for the reset link
4. ✅ Click the link (valid for 24 hours)
5. ✅ Enter and confirm your new password
6. ✅ Log in with your new password

If you encounter any issues, you can always request a new reset link from the error page or contact support for assistance.

---

## Additional Notes

- The feature works for all user types: Artists, Clients, and Admins
- The system does not reveal whether an email address is registered (security feature)
- All password resets are logged for security auditing
- Multiple reset requests will invalidate previous unused tokens

---

**Last Updated**: [Date]
**Version**: 1.0
**Documentation Maintained By**: UbuntuSelect Development Team

