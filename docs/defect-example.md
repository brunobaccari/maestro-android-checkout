# Defect report example — fictional, not an observed finding

**Summary:** Cart badge retains one item after removing the last product.

**Environment:** My Demo App Android 2.3.0; Android 34 emulator; English; clean app state.

**Precondition:** One Sauce Labs Backpack in the cart.

1. Open My Cart.
2. Tap Remove Item.
3. Observe the empty state and cart badge.

**Expected:** No Items is displayed and the badge no longer indicates an item.

**Hypothetical actual result:** No Items is displayed but the badge still shows 1.

**Impact / severity:** Medium: cart information is inconsistent; purchase is not demonstrated to be blocked. Priority should be agreed during triage.

**Evidence to attach:** Build, device details, recording from clean launch, before/after screenshots and reproduction frequency. Do not attach credentials or customer data.

**Retest:** Repeat removal, navigate back to the catalog and reopen the cart; confirm badge and item list agree. Run quantity and checkout regression. This example must not be reported as a real app defect without reproduction.
