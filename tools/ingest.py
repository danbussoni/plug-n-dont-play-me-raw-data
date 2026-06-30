import re
import urllib.request
import os

# Exact static Wayback Machine snapshot verified for Windows 11 Pro 23H2
url = "https://web.archive.org/web/20250918014956/https://www.winhelponline.com/blog/windows-11-default-services-configuration/"

print("Connecting to Wayback Machine snapshot via native urllib...")

# Inject browser headers to prevent Archive.org security blocks
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

try:
    with urllib.request.urlopen(req) as response:
        html_content = response.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching data from archive: {e}")
    exit(1)

# Regex engine optimized to catch the raw lower technical block sequence intact
pattern = re.compile(
    r"Service Name\s*:\s*(.*?)\s*\n"
    r"Display Name\s*:\s*(.*?)\s*\n"
    r"Image Path\s*:\s*(.*?)\s*\n"
    r"Startup Type\s*:\s*(.*?)\s*\n"
    r"Log On As\s*:\s*(.*?)\s*\n"
    r"Permissions\s*:\s*(.*?)\s*\n",
    re.MULTILINE
)

matches = pattern.findall(html_content)

# Agnostic Regex to match an underscore followed by any hexadecimal string at the end of the line
per_user_suffix_pattern = re.compile(r"_[a-fA-F0-9]+$")

# Define the file metadata, legal provenance anchors, and native taxonomy fields
header = (
    "; ============================================================================\n"
    "; Plug n dont Play me — Windows 11 Default Services Master Database\n"
    "; Source Provenance (Static Immutable Digital Archive):\n"
    "; https://web.archive.org/web/20250918014956/https://www.winhelponline.com/blog/windows-11-default-services-configuration/\n"
    "; WARNING: Per-User dynamic hex suffixes (e.g., _1768de) have been agnostically stripped.\n"
    "; ============================================================================\n"
    ";ServiceName|DisplayName|ImagePath|StartupType|LogOnAs|Permissions\n"
)

# ARCHITECTURE LAYER: Dynamically resolve repository root to enforce flat root CDN delivery
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
output_path = os.path.join(repo_root, "win_default_services_config.map")

# Populate the final flat database with cleaned names directly at the root
with open(output_path, "w", encoding="utf-8") as f:
    f.write(header)
    for match in matches:
        raw_service_name = match[0].strip()
        
        # Agnostically strip the dynamic session hex suffix if present
        clean_service_name = per_user_suffix_pattern.sub("", raw_service_name)
        
        display_name = match[1].strip()
        image_path = match[2].strip()
        startup_type = match[3].strip()
        log_on_as = match[4].strip()
        permissions = match[5].strip()
        
        # Write the row using the sanitized universal service name
        f.write(f"{clean_service_name}|{display_name}|{image_path}|{startup_type}|{log_on_as}|{permissions}\n")

print(f"Ingestion complete! Successfully baked {len(matches)} records into optimized root target: {output_path}")