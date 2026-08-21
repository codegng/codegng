from components import Heading, Value, TimeElapsed, Separator, WorkingOn, CommitGraph, GithubStats, Last24Hr, CurrentDate

# Layout configuration for your profile README neofetch layout

Heading("Axxo@GitHub", CurrentDate())
Value("OS", "Windows 11, Linux (Kali)")
TimeElapsed("Uptime", 2008, 11, 9) # Customize or keep as a baseline
Value("IDE", "VSCode, Neovim, Alight Motion")
Value("Status", "Learning & Building")
Separator()
WorkingOn()
Separator()
Value("Languages.Programming", "Python, Bash, JavaScript")
Value("Languages.Real", "English, Sinhala")
Separator()
Value("Hobbies.Software", "Cybersecurity, Video Editing, Web-Dev")
Value("Hobbies.Hardware", "PC Troubleshooting, Networking")
Separator()
Heading("Contact")
Value("Email", "your.email@gmail.com")
Value("GitHub", "github.com/codegng")
Separator()
GithubStats("Repos", "Stars", "Commits", "Followers", "Pull.Requests", "Lines.of.Code")
Separator()
CommitGraph()
Last24Hr("Pushes", "Pull.Requests", "Issues", "Starred", "Forked", "Releases", "Reviewed", "Comments")
