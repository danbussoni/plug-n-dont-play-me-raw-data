# Plug-n-Don't-Play me — Raw Master Data (win_default_services_config.map)

An immutable, high-fidelity local Data Lake preserving the absolute factory-default configuration states of Windows 11 services. 
This repository serves as the centralized backend data pipeline for the **Plug n dont Play me** client application.

## 🎯 Project Philosophy & Modern Paradigm Shift

### The Legacy Concept: "Plug and Play" (PnP)
Traditionally, the "Plug and Play" standard revolutionized computing by removing configuration barriers for the end-user:

GTRANSLATE LEGACY DEFINITION:
Plug and play / pləɡ (ə)n ˈplā

"[Adjective] denoting or relating to software or devices that are intended to work 
perfectly when first used or connected, without reconfiguration or adjustment by the user."

"[Substantive] a standard for the connection of peripherals to personal computers, whereby a device only needs to be connected to a 
computer in order to be configured to work perfectly, without any action by the user."

The Modern Reality: 

In today's computing ecosystem, this hands-off automation has been structurally twisted.
"Working perfectly without user intervention" has devolved into silent background service inflation, 
unvetted telemetry nodes, aggressive third-party updater daemons, and permanent administrative configuration drift.
Modern software abuses the PnP philosophy to silently "play" with system privileges, bloated registries, and background 
execution lines without explicit user consent.

## ⚙️ About this repo:
The application maps the active startup states against the pristine configurations defined in win_default_services_config.map.
When implementing a feature to disable non-PPL services—thereby exposing various behaviors of the current PnP stack—it is essential to follow 
industry best practices to avoid catching users off guard and to mitigate the risk of catastrophic failures. 
Since there is no persistent record of each service's default state (other than the official installation of a specific Windows 11 version), 
maintaining a table to revert services to their default state is necessary.

Source of extraction of this Master Data:
"https://web.archive.org/web/20250918014956/https://www.winhelponline.com/blog/windows-11-default-services-configuration/"

The production application (PndPm.exe) must ingest the immutable table directly from the public CDN endpoint, 
using the default service configuration as a baseline for any runtime changes. This data staging component remains cloud-resident, 
adhering to industry best practices by consuming a validated engineering table from a trusted source:
https://raw.githubusercontent.com/danbussoni/plug-n-dont-play-me-raw-data/main/win_default_services_config.map

## 📊 Native Taxonomy Specification

The ledger is persisted within a flat pipe-delimited (|) file system to prevent syntax collisions.
Normalization, string cleansing, and type-casting are decoupled from this storage tier and handled natively downstream by the application logic.
Agnostic Normalization: Windows dynamically appends random hexadecimal suffixes to per-user services (e.g., changing NPSMSvc into NPSMSvc_1768de on active sessions).
These suffixes are stripped during this repository's ingestion phase for cross-referencing.

;ServiceName|DisplayName|ImagePath|StartupType|LogOnAs|Permissions

Field Definitions
ServiceName: The absolute registry subkey identifier from HKLM\SYSTEM\CurrentControlSet\Services (Sanitized/Agnostic version without per-user hexadecimal tails).

DisplayName: The local administrative friendly name assigned to the Service Control Manager interface.

ImagePath: The exact command-line string execution path including binary mappings and host parameters.

StartupType: The native textual startup behavior token (e.g., Manual (Triggered), Auto, Disabled, Automatic (Delayed Start)).

LogOnAs: The security principal identity context assigned to run the thread (e.g., LocalSystem, NT AUTHORITY\LocalService).

Permissions: The raw Security Descriptor Definition Language sequence governing access rights, security identifiers (SIDs), DACLs, and SACLs.
 

