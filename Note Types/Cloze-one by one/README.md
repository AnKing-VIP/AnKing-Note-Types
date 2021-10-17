## Example
<p align="center"><img src="https://raw.githubusercontent.com/AnKingMed/AnKing-Note-Types/master/screenshots/Cloze-one%20by%20one.gif?raw=true" style="width:700px;"></p>

## Features Unique to this Note Type
- One by one clozes will work with c2, c3, etc as well
- `Alt+click` reveals one word at a time. `click` to reveal one cloze or word at a time depending on setting
- `Click` to reveal or press `Reveal Next` Button
  <details><summary>Customize Reveal Word vs Cloze <i>(Back template)</i></summary>
    <p>

    ```
    // Changes how "Reveal Next" and clicking behaves. Either "cloze" or "word". 
    var revealNextMode = "cloze" 
    ```
    </p>
  </details>

- `n` to reveal one cloze/word at a time, `shift + n` to reveal one word at a time 
  <details><summary>Customize Shortcuts <i>(Back template)</i></summary>
    <p>

    ```
    var revealClozeShortcut = "N" // Shortcut to reveal next cloze
    var revealClozeWordShortcut = "Shift + N" // Shortcut to reveal next cloze word
    ```
    </p>
  </details>

- <b>Occlusion Images or Symbol</b>
  <details><summary>Customize occlusion method <i>(Back template)</i></summary>
    <p>

    ```
    // What cloze is hidden with
    var clozeHidden = (elem) => "👑"
    /* 
    You can replace the above line with below examples. '█' or '_' works well for hiding clozes.

    // Fixed length  (default):
    var clozeHidden = (elem) => "███"
    // Replace all characters with "█":
    var clozeHidden = (elem) => "█".repeat(elem.textContent.length)
    // Show whitespaces:
    var clozeHidden = (elem) => "[" + elem.textContent.split(" ").map((t) => "_".repeat(t.length)).join(" ") + "]"
    // Color-filled box (doesn't hide images):
    var clozeHidden = (elem) => `<span style="background-color: red; color: transparent;">${elem.innerHTML}</span>`
    */
    ```
    </p>
  </details>

- <b>Autoflip to back</b> _(only works on desktop version, not mobile)_
  <details><summary>Toggle autoflip on/off <i>(Front template)</i></summary>
    <p>

    ```
    // ############## USER CONFIGURATION START ##############
    var autoflip = false // auto flip to back if cloze has no hints. Does not work for AnkiMobile.
    ```
    </p>
  </details>

## Changelog:
2021-08: Initial Release
2021-10-17: Significant overhaul of styling, buttons, formatting and more

## TODO
Ideas for additional features: https://github.com/thiswillbeyourgithub/Clozolkor



***

### If you like these, please consider donating to this project

<p align="center">
<a href="https://www.ankingmed.com" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/AnKingSmall.png?raw=true"></a><a href="https://www.ankingmed.com" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/TheAnKing.png?raw=true"></a>
  <br>
  <a href="https://www.facebook.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/FB.png?raw=true"></a>     <a href="https://www.instagram.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Instagram.png?raw=true"></a>     <a href="https://www.youtube.com/theanking" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/YT.png?raw=true"></a>     <a href="https://www.tiktok.com/@ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/TikTok.png?raw=true"></a>     <a href="https://www.twitter.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Twitter.png?raw=true"></a>
  <br>
<a href="https://www.ankipalace.com/membership" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/Patreon.jpg?raw=true"></a>
<br>
<b>Check out our Anki Mastery Course! (The source of funding for this project)</b><br>
          <a href="https://courses.ankipalace.com/?utm_source=anking_bg_add-on&amp;utm_medium=anki_add-on_page&amp;utm_campaign=mastery_course" rel="nofollow">https://courses.ankipalace.com</a>
<a href="https://courses.ankipalace.com/?utm_source=anking_bg_add-on&amp;utm_medium=anki_add-on_page&amp;utm_campaign=mastery_course" rel="nofollow">
  <br>
  <img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/AnkiPalace.png?raw=true"></a></p>