# Android checkout with Maestro

[Versão em português](README.md)

Five flows against [Sauce Labs My Demo App Android 2.3.0](https://github.com/saucelabs/my-demo-app-android/releases/tag/2.3.0). The APK comes from the official release; this repository does not implement the application under test.

## Run

Install Java 21, [Maestro CLI 2.11.0](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli) and Android SDK. Start an Android 34 emulator with an English locale. On Windows, follow the CLI documentation's WSL setup.

```bash
cp .env.example .env
python -m pip install -r requirements.txt
python -c "from dotenv import load_dotenv; import os, urllib.request; load_dotenv(); urllib.request.urlretrieve(os.environ['APP_URL'], 'app.apk')"
adb install app.apk
python run_tests.py
```

The runner loads `.env`; process variables take precedence. Maestro reads `MAESTRO_*` variables from the environment, keeping credentials out of YAML. Example users are public demo accounts. Address and card data are fictitious and limited to this demo.

## Coverage

| Flow | Expected result |
| --- | --- |
| Checkout | Correct product, USD 29.99 subtotal, USD 35.98 including delivery, confirmation and empty cart. |
| Quantity | Two items total USD 59.98; reducing to one restores USD 29.99. |
| Removal | Removing the last item displays the empty state. |
| Blocked account | Blocking message; shipping form remains absent. |
| Required address | Empty form does not open payment and reports the missing name. |

Each flow stops the app before clearing state. `flows/helpers/` contains repeated cart and login steps. Selectors use resource IDs and accessibility descriptions from the pinned app's public source, without coordinates or fixed sleeps. Tapping the product image follows its actual click target.

## QA material and evidence

[Test strategy and exploratory charter](docs/test-strategy.md), [Xray import cases](docs/xray-tests.csv), [fictional defect example](docs/defect-example.md) and [Actions runs and artifacts](https://github.com/brunobaccari/maestro-android-checkout/actions).

GitHub Actions installs the APK in an Android 34 emulator. Open the run under **Actions**: **Summary** displays counts and step status; **Artifacts** contains `android-results` with JUnit, flow logs, available screenshots and a copy of the summary. Retention is seven days, including failed test runs. A missing report is marked as unconfirmed execution, never as a pass.

All five flows passed in the recorded CI run. No automatic flow retries. iOS, physical devices and a commercial backend are outside this result; the demo app simulates purchases. The exploratory charter and Xray import have not been executed in a tenant.

References: [official app source](https://github.com/saucelabs/my-demo-app-android/tree/2.3.0), [Maestro parameters](https://docs.maestro.dev/maestro-flows/flow-control-and-logic/parameters-and-constants) and [CI emulator action](https://github.com/ReactiveCircus/android-emulator-runner).

Commit dates in this portfolio were reorganized retroactively; Actions runs retain their actual execution dates.
