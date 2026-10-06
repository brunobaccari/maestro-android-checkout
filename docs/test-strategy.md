# Mobile test strategy

Target: Sauce Labs My Demo App Android 2.3.0, Android 34 emulator, English locale. This is a portfolio exercise. iOS and physical devices are outside the verified scope.

## Risk and selection

| Risk | Technique | Automated check | Manual follow-up |
| --- | --- | --- | --- |
| Wrong cart amount | Boundary/state transition: one → two → one | quantity.yaml, including background/resume | Rapid taps, upper quantity bound, rotation, process death. |
| Lost or duplicated order | End-to-end state transition | checkout.yaml | Background/resume on review; repeated submit. |
| Incomplete address accepted | Invalid equivalence partition | required-shipping.yaml | Whitespace, Unicode names, keyboard navigation. |
| Blocked account proceeds | Account-state partition | locked-user.yaml | Resume a saved session after blocking. |
| Last item leaves stale cart | Boundary at zero items | remove-item.yaml | Back navigation and process restart. |

## Exploratory charter — 25 minutes

Explore cart and checkout continuity while changing app state. Use only fictitious data. Start with one product; change quantity, rotate the emulator, background/resume, press Android Back, then kill and relaunch. Compare displayed totals and selected items after every transition. Check font scaling, TalkBack names and reachability of the payment action with the keyboard open. Record build, Android API, device, steps, expected/actual behavior and a screenshot or recording. This charter is prepared, not claimed as executed.

## Release decision for this exercise

All five flows must pass against the pinned APK and retain their reports. An infrastructure failure is not a product defect or a pass. Triage unexpected behavior against the pinned source and reproduce it before changing an assertion. Accessibility, rotation and process-death exploration remain separate from the automated background/resume check.

## Defect lifecycle

Record → reproduce and triage → fix proposed → retest the reproduction → run related regression → close if evidence matches the agreed expectation; reopen otherwise. Severity describes user impact; priority describes scheduling. This repository does not require a live Jira board.

## Xray

`xray-tests.csv` uses one row per step with repeated Test Case Identifier. In Xray Cloud Test Case Importer, map Test Case Identifier, Summary, Test Type, Action, Data and Expected Result to the corresponding fields. Choose an existing project and review the preview before import. Project keys, priorities and required fields depend on the Jira configuration. Import has not been executed in a tenant. [Importer documentation](https://docs.getxray.app/display/XRAYCLOUD/Importing+Tests+using+Test+Case+Importer).

## Status update example

“The automated scope covers cart totals, required shipping data, blocked accounts and checkout completion on Android 34. See the linked CI run for execution results. Physical devices, iOS and the exploratory charter are not included in that result.”
