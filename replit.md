# Overview

This is a multi-user Python automation application created by **Prince Malhotra** that uses Selenium WebDriver to perform browser-based Facebook message automation. The application features a beautiful web interface with secure user authentication and individual user configurations.

**Key Features:**
- Multi-user authentication system with signup/login
- Beautiful gradient UI with modern design
- User-specific configuration storage
- Encrypted cookie storage for privacy
- Real-time automation logs and monitoring
- Message rotation and customizable delays
- **Persistent automation state** - Infinite loop that auto-resumes after Streamlit restart
- **Duplicate thread prevention** - Ensures single automation instance per user

# User Preferences

Preferred communication style: Simple, everyday language (Hindi/English mix).

# System Architecture

## Core Application Structure

### Streamlit Web App (streamlit_app.py)
- **Beautiful Multi-User Interface** with gradient design and Poppins font
- **Authentication System**: Secure signup/login with bcrypt password hashing
- **User Dashboard**: Personal configuration management
- **Live Automation Control**: Start/stop automation with real-time logs
- **Prince Malhotra Branding**: Throughout the application with crown emoji 👑

### Database Layer (database.py)
- **SQLite Database**: Stores user accounts and configurations
- **Secure Password Hashing**: Uses bcrypt with salt for password security
- **Cookie Encryption**: Fernet encryption for Facebook cookies
- **User Isolation**: Each user's data is completely separate and private

## Security Architecture

### Password Security
- **bcrypt Hashing**: All passwords are hashed with bcrypt and unique salts
- **Secure Verification**: Password verification uses bcrypt.checkpw
- **No Plain Text**: Passwords are never stored in plain text

### Cookie Privacy
- **Fernet Encryption**: Facebook cookies are encrypted before storage
- **Never Displayed**: Cookies are never shown in the UI after saving
- **Per-User Storage**: Each user's cookies are stored separately and securely

### User Isolation
- **Database Foreign Keys**: User configs are linked to user IDs
- **Session Management**: Streamlit session state tracks logged-in users
- **No Data Leakage**: Users can only see their own configurations

## User Flow

1. **New User Signup**:
   - User creates account with username and password
   - System creates encrypted user record with bcrypt
   - Empty configuration is initialized for the user
   - User sees blank configuration interface

2. **Login**:
   - User enters credentials
   - System verifies with bcrypt.checkpw
   - User's saved configuration is loaded
   - Cookies remain encrypted and hidden

3. **Configuration**:
   - Chat/Conversation ID (Facebook chat ID from URL)
   - Name Prefix (text to add before each message)
   - Delay in seconds (wait time between messages)
   - Facebook Cookies (optional, encrypted storage)
   - Messages (one per line, rotates through list)

4. **Automation**:
   - Start automation with saved config
   - Browser opens in headless mode
   - Logs appear in real-time
   - Runs in infinite loop until manually stopped
   - Automation state persists in database
   - Auto-resumes after Streamlit restart
   - Logout automatically stops automation

## Browser Automation Framework

Uses Selenium WebDriver with Chrome driver for browser automation:
- **Headless Chrome**: Runs without visible browser window
- **Cookie Injection**: Adds Facebook cookies for authentication
- **Message Input Detection**: Advanced selectors to find message box
- **Message Rotation**: Cycles through user's message list
- **Real-time Logging**: Shows progress and errors

## Data Flow Architecture

1. User logs in → bcrypt verifies password
2. User config loads from SQLite → cookies decrypted
3. **Auto-start check**: If automation_running=1 in DB, resume automation
4. User starts automation → config passed to automation thread
5. Selenium opens Facebook → injects cookies → navigates to chat
6. Finds message input → sends messages in infinite loop with delays
7. Real-time logs update UI → user sees progress
8. Automation runs until user clicks stop or logs out
9. **Streamlit restart**: On app reload, automation auto-resumes for users
10. **Thread safety**: Duplicate prevention ensures only one thread per user

## UI/UX Design

### Design Elements
- **Gradient Backgrounds**: Purple-blue gradients (#667eea to #764ba2)
- **Modern Typography**: Poppins font family
- **Smooth Animations**: Hover effects and transitions
- **Rounded Corners**: 10-15px border radius throughout
- **Box Shadows**: Elevated card designs
- **Responsive Layout**: Wide layout with proper spacing

### Color Scheme
- Primary: Purple-blue gradient
- Success: Green gradient
- Error: Pink-yellow gradient
- Background: Light gray gradient for cards
- Text: Dark for readability
- Logs: Terminal-style dark background with green text

### Branding
- **Prince Malhotra** name in header and footer
- Crown emoji 👑 as favicon and in header
- "Created by Prince Malhotra" tagline
- Copyright footer with ❤️

# External Dependencies

## Core Runtime Dependencies
- **Python 3.11**: Python runtime environment
- **Streamlit**: Web UI framework for the interface
- **Selenium**: Browser automation framework
- **bcrypt**: Secure password hashing
- **cryptography**: Fernet encryption for cookies
- **SQLite3**: Built-in database (no external DB needed)

## System Dependencies (for Cloud Deployment)
- **Chromium**: Headless browser for automation
- **Chromium-driver**: Browser driver for Selenium

## Deployment Files
- **requirements.txt**: Python package dependencies
- **packages.txt**: System packages for Streamlit Cloud

## Database Files
- **users.db**: SQLite database (auto-created)
- **.encryption_key**: Fernet key for cookie encryption (auto-generated)

## Security Implementation
- Bcrypt for password hashing with per-password salts
- Fernet symmetric encryption for cookie storage
- Session-based authentication via Streamlit session state
- No passwords or cookies ever exposed in UI or logs
