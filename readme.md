# Plug n dont Play me — Raw Master Data

An immutable, high-fidelity local Data Lake preserving the absolute factory-default configuration states of Windows 11 services. This repository serves as the centralized backend data pipeline for the **Plug n dont Play me** client application.

## 🎯 Project Philosophy & Modern Paradigm Shift

### The Legacy Concept: "Plug and Play" (PnP)
Traditionally, the "Plug and Play" standard revolutionized computing by removing configuration barriers for the end-user:

```text
;GTRANSLATE LEGACY DEFINITION:
;Plug and play / pləɡ (ə)n ˈplā
;[Adjective] denoting or relating to software or devices that are intended to work 
;perfectly when first used or connected, without reconfiguration or adjustment by the user.

The Modern Reality: Weaponized Automation
In today's computing ecosystem, this hands-off automation has been structurally twisted. "Working perfectly without user intervention" has devolved into silent background service inflation, unvetted telemetry nodes, aggressive third-party updater daemons, and permanent administrative configuration drift. Modern software abuses the PnP philosophy to silently "play" with system privileges, bloated registries, and background execution lines without explicit user consent.

The Evolution: Plug n dont Play me (PndPm)
Plug n dont Play me is a critical security and hygiene upgrade to the modern PnP paradigm. Its foundational axiom is strict: Software may install, but it must not play in the background without explicit, audited administrative validation. By utilizing the compiled AutoHotkey binary (PndPm.exe), the system transitions from a passive host into a rigid sentinel—freezing, auditing, and enforcing baseline compliance against unauthorized modern software drift.

⚙️ Application Integration & Usage (PndPm.exe)
The compiled AutoHotkey binary (PndPm.exe) consumes the dataset hosted here to audit the host machine's system health.

Ingestion Flow
Bootstrap Update: On demand or during initialization, PndPm.exe performs an asynchronous HTTP GET request to pull the latest flat database file from the optimized distribution layer.

Agnostic Normalization: Windows dynamically appends random hexadecimal suffixes to per-user services (e.g., changing NPSMSvc into NPSMSvc_1768de on active sessions). Because these suffixes are stripped during this repository's ingestion phase, PndPm.exe executes a local Regex matching sequence (_[a-fA-F0-9]+$) to normalize active local service keys before cross-referencing.

Delta Auditing: The application maps the active startup states against the pristine configurations defined in native_base.map to detect unauthorized drift, unexpected privilege escalations, or disabled critical security flags.

🚀 Optimized Distribution Layer
To ensure ultra-low latency execution and eliminate nested routing overhead when the client application downloads updates from the cloud, the database flat-file is delivered through an optimized single-tier storage layer located directly at the repository root.

Production applications (PndPm.exe) can stream the immutable asset directly from the public CDN endpoint:
https://raw.githubusercontent.com/danbussoni/plug-n-dont-play-me-raw-data/main/native_base.map

📊 Native Taxonomy Specification
The ledger is persisted within a flat pipe-delimited (|) file system to prevent syntax collisions with Windows execution flags, directory structures, and Security Descriptor Definition Language (SDDL) strings. Normalization, string cleansing, and type-casting are decoupled from this storage tier and handled natively downstream by the application logic.

;ServiceName|DisplayName|ImagePath|StartupType|LogOnAs|Permissions

Field Definitions
ServiceName: The absolute registry subkey identifier from HKLM\SYSTEM\CurrentControlSet\Services (Sanitized/Agnostic version without per-user hexadecimal tails).

DisplayName: The local administrative friendly name assigned to the Service Control Manager interface.

ImagePath: The exact command-line string execution path including binary mappings and host parameters.

StartupType: The native textual startup behavior token (e.g., Manual (Triggered), Auto, Disabled, Automatic (Delayed Start)).

LogOnAs: The security principal identity context assigned to run the thread (e.g., LocalSystem, NT AUTHORITY\LocalService).

Permissions: The raw Security Descriptor Definition Language sequence governing access rights, security identifiers (SIDs), DACLs, and SACLs.

