# Reusable code

### Open new terminal

```
osascript -e 'tell app "Terminal" to do script "/tmp/task_scheduler.sh event"'

```

### Definig a cron job
```
0 */4 * * * /tmp/task_scheduler.sh event &> /tmp/script_log
```

### Work with images
- Start appium with images plugin

```
appium --use-plugins images
```

- Update capabilities to work with images

```
driver.update_settings({"getMatchedImageResult": True})
```

- Example of how to load an image

```
def load_image():
    with open(r".\images\enter_btn.png", "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
```
- Find image element with explicit wait

```
wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=image_base64))
```

```
close_btn = wait.until(lambda x: x.find_element(by=AppiumBy.IMAGE, value=close_btn_img))
```

