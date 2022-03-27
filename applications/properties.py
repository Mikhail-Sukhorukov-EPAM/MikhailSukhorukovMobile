class Properties:
    PATH_TO_APK = '/Users/mikhail_sukhorukov/'
    ANDROID_APK = {
        "app": f"{PATH_TO_APK}ContactManager.apk"
    }
    IOS_APP = {
        "app": f"{PATH_TO_APK}Aspiration.app"
    }
    ANDROID_EMULATOR = {
        "deviceName": "Google Pixel 3 GoogleAPI Emulator",
        "udid": "emulator-5554",
        "deviceOrientation": "portrait",
        "platformName": "Android",
        "app": ANDROID_APK["app"]
    }
    ANDROID_PHYSICAL = {
        "deviceName": "iMito",
        "udid": "0123456789ABCDEF",
        "deviceOrientation": "tablet",
        "platformName": "Android",
        "app": IOS_APP["app"]
    }
    IOS_SIMULATOR = {
        "deviceName": "iPhone XR Simulator",
        "deviceOrientation": "portrait",
        "platformName": "iOS",
        "platformVersion": "12.0"
    }
    IOS_PHYSICAL = {
        "deviceName": "iPhone XR Simulator",
        "deviceOrientation": "portrait",
        "platformName": "iOS",
        "platformVersion": "12.0"
    }
