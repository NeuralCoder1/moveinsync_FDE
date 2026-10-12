# MoveInSync Help Center — Failure Mode Documentation

- Help Center: https://helpcenter.moveinsync.com/
- Collected: 2026-10-12
- Coverage note: the Help Center landing page and article-search pages were initially inaccessible to the retrieval tool, so category completeness is not established. On 2026-10-12, the integrated browser search for `GPS` returned 17 results and the GPS-loss article below was opened and verified. Screenshot: [helpcenter_gps_screenshot.png](helpcenter_gps_screenshot.png).

## Article: Mobile App Issues
- URL: https://helpcenter.moveinsync.com/support/solutions/articles/1070000136108-mobile-app-issues
- Documented issues:
  - Mobile login failure, refresh loop, and login errors including invalid credentials, user not found, non-subscription access, and login timeout.
  - SMS/email OTP not received, OTP screen hanging, and login failing after OTP entry.
  - App crash or app closing during use.
  - App not launching, or remaining on the splash/loading screen.
  - Opt-in/opt-out control not visible.
  - Slow/no response, network errors, or an unreachable server.
  - Stuck loading, “Dinosaur”/“Something went wrong” messages, and blank or unresponsive pages.
- Troubleshooting steps:
  - Login: verify active subscription and registered phone/email; check app/browser version; clear cache/cookies; verify app permissions in the Employee Profile.
  - OTP: confirm the registered contact information and Employee Profile permissions; check signal/network and SMS availability; wait or resend the OTP.
  - Login errors: identify the error; verify credentials or reset the password; confirm app access is enabled in the Employee Profile; escalate timeouts/server issues.
  - Crashes: update the app, clear app cache/data, restart the device, reinstall if needed, then collect logs and escalate if it continues.
  - Launching: restart the device, clear cache, reinstall from the app store, and check minimum device requirements.
  - Opt-in/out: check role/group eligibility, organization-admin configuration, and recent profile/team changes.
  - Network/page loading: switch between Wi-Fi and mobile data, restart the router or toggle airplane mode, and check access to other sites/apps.
  - Server/page failures: refresh or relaunch; gather the time and screenshots; check whether other users are affected.
- Key finding: this accessible article documents multiple distinct access, OTP, crash, launch, network, and server/page failure modes and gives support procedures for them. One article does not establish how often they occur or that they are chronic.

## Article: How to identify in the system if a trip has faced GPS loss
- URL: https://helpcenter.moveinsync.com/support/solutions/articles/1070000086664-how-to-identify-in-the-system-if-a-trip-has-faced-gps-loss-
- Verified: 2026-10-12 in the Help Center search and article page.
- Modified: 2025-02-24.
- Key diagnostic points:
  - Search by trip ID and open View Route; in legacy trip view, enable the Speed toggle to visualize GPS loss on the route. If on modern trip view, switch to legacy view first.
  - From the trip sheet, open Device Health, select the trip time range, and inspect the relevant time logs.
  - Check whether `IsGPSOn` is true. GPS coordinate accuracy should be under 50 meters; unavailable accuracy or a value of 50 meters or more is treated by the article as inaccurate.
  - Check for time-log gaps and an `Application started at` entry, which can indicate the driver killed the MoveInSync Driver application during the trip.
  - For billing remediation, open Billing > Flagged Vehicles (Data incomplete), choose a vendor and affected trips, then use Resolve Issues or an individual Fix action to select a recovery option for GPS loss and lost kilometers.
  - The article also lists GPS fluctuation causes including multipath interference, atmospheric conditions, satellite geometry, obstructions, receiver quality, signal blockage/interference, configuration or user error, and environmental factors.

## Other Help Center articles and requested categories
- “Mobile App” and other category indexes could not be fully enumerated, so a complete list of titles cannot be verified.
- OTP and login guidance is documented in the “Mobile App Issues” article; the GPS loss and Device Health workflow is documented in the GPS article above. A separate sync-delay article was not verified.