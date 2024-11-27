# **Email Task Automation Project: User Guide**

This guide provides step-by-step instructions for setting up and running the **Email Task Automation** project. The system automatically reads emails, identifies specific requests, and performs actions like sending flight quotations or scheduling meetings using Google APIs.

## **Prerequisites**

1.  **Google Account**: Required for Gmail and Google Calendar access.
2.  **Python Installed**: Version 3.7 or later.
3.  **Google Cloud Console Access**: For API setup.
4.  **Dependencies Installed**: See instructions below.

## **Project Folder Structure**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`  bashCopy codeemail-task-automation/  │  ├── main.py               # Main script  ├── credentials.json      # OAuth2 credentials (from Google Cloud)  ├── token.json            # Generated token after authentication  ├── .env                  # Environment variables  ├── requirements.txt      # Dependencies  `

## **Setup Instructions**

### **1\. Clone the Project**

Download or clone the project repository to your local machine:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`  bashCopy codegit clone https://github.com/your-repository-url/email-task-automation.git  cd email-task-automation  `

### **2\. Enable Google APIs**

1.  Go to the Google Cloud Console.
2.  **Create a New Project** (or select an existing one).
3.  Enable the following APIs:

    - **Gmail API**
    - **Google Calendar API**

4.  **Create Credentials**:

    - Navigate to **APIs & Services > Credentials**.
    - Select **Create Credentials > OAuth 2.0 Client ID**.
    - Configure the consent screen and download the credentials.json file.
    - Place credentials.json in the project root folder.

### **3\. Configure Environment Variables**

1.  Create a .env file in the project folder.
2.  envCopy codeSENDER=specific-email@example.comFLIGHT_KEYWORD=quotation for flight ticketsMEETING_KEYWORD=schedule an online meeting

    - Replace specific-email@example.com with the sender’s email address you want to monitor.
    - Replace keywords as needed.

### **4\. Install Dependencies**

Install the required Python libraries using pip:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`  bashCopy codepip install -r requirements.txt  `

### **5\. Run the Script**

1.  bashCopy codepython main.py
2.  On the first run:

    - Authenticate your Google account in the browser.
    - Grant permissions for Gmail and Calendar access.

3.  Subsequent runs will use the stored token.json.

## **How It Works**

1.  **Email Monitoring**:

    - The script connects to Gmail and checks for emails from the specified sender.
    - If an email subject contains the flight quotation or meeting request keywords, the appropriate action is triggered.

2.  **Task Automation**:

    - **Flight Quotation**: Logs a dummy response. (You can integrate email-sending logic here.)
    - **Meeting Scheduling**: Creates a meeting in Google Calendar and sends an invite to the sender.

## **Logs**

- All actions are logged to the console for monitoring and debugging.
