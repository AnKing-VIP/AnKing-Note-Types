## Instructions:
1. Download the latest version of the note type in the [Releases](https://github.com/AnKingMed/AnKing-Note-Types/releases) tab
2. When creating the new I/O card, make sure you are using the note template called `IO-one by one`. Paste your image into the 'image' field.
3. Click the icon in the toolbar that looks like a blue/red box in a box. The image should outline with a red dotted border when you click that button.
   <img src="/screenshots/Closet button.png" style="width:400px;">
4. Draw your occlusions in the order you want them revealed. You want each occlusion to say 'rect1' inside of it. **If you need to delete a rectangle**, hold shift while clicking on that box.
5. Once you have all of your occlusions made, right click on the image (don't right click over an occlusion though) and select 'accept occlusions'
   - You will see the 'I0' field auto populate. At that point you are good to add the card by clicking "Add" at the bottom
6. When reviewing, you will see all boxes occluded at once, however the first box will be highlighted. Click or use `n` to reveal a box, and the subsequent box will become highlighted. Use `,` to reveal all at once. Continue until all boxes are revealed. You can use `h` (requires the "Hint Hotkeys" add-on installed) or click to reveal the buttons. Use `'` to reveal all buttons at once. _(These shortcuts can all be customized in the Back Template)_
7. **To edit occlusions in an existing card**, click the icon in the toolbar that looks like a blue/red box in a box.

This note type **will** work on Anki iOS and AnkiDroid.

## Features Unique to this Note Type
- <b>Autoflip to back</b> _(only works on desktop version, not mobile)_
  <details><summary>Toggle autoflip on/off <i>(Front template)</i></summary>
    <p>

    ```
    // ############## USER CONFIGURATION START ##############
    var autoflip = true // auto flip to back. Does not work for AnkiMobile.
    // ############## USER CONFIGURATION END ##############
    ```
    </p>
  </details>

- <b>Occlusion Shortcuts</b>
  <details><summary>Customize Reveal and Toggle All <i>(Back template)</i></summary>
    <p>

    ```
    // ##############  OCCLUSION SHORTCUTS  ##############
    var RevealIncremental = "N";
    var ToggleAllOcclusions = ",";
    ```
    </p>
  </details>

- <b>Occlusion Box Colors</b>
  <details><summary>Change colors and borders <i>(Styling)</i></summary>
    <p>

    ```
    /* OCCLUSION RECTANGLE COLORS */
    --rect-bg: moccasin;
    --rect-border: olive;
    --active-rect-bg: salmon;
    --active-rect-border: yellow;
    ```
    </p>
  </details>

## Screen recordings
### Card creation
<img src="/screenshots/Creating IO one by one.gif" style="width:600px;">

### Function
<img src="/screenshots/IO one by one.gif" style="width:600px;">

## Changelog:
2021-09-05: Initial Release on <a href="https://www.reddit.com/r/Anki/comments/pia8e5/how_to_incrementally_reveal_an_image_occlusion/?utm_source=share&utm_medium=ios_app&utm_name=iossmf">reddit</a> by someone else
2021-10-17: Significant overhaul of styling, buttons, formatting and more

## TODO
- [ ] 

***

### If you like these, please consider donating to this project

<center><div style="vertical-align:middle;"><a href="https://www.theanking.com"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/TheAnKing-New.png?raw=true"></a></div></center>

<center>&nbsp;<a href="https://www.facebook.com/ankingmed"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/FB.png?raw=true"></a>
<a href="https://www.instagram.com/ankingmed"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Instagram.png?raw=true"></a>
<a href="https://www.youtube.com/theanking"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/YT.png?raw=true"></a>
<a href="https://www.tiktok.com/@ankingmed"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/TikTok.png?raw=true"></a>
<a href="https://www.twitter.com/ankingmed"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Twitter.png?raw=true"></a></center>

<div><center><a href="https://www.theanking.com/vip"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/Patreon.jpg?raw=true"></a></center></div>



<div><center><a href="https://courses.theanking.com"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/MasteryCourse.png?raw=true"></a></center></div>
