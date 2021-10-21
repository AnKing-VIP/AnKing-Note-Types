# Physeo Note Type
This is a Cloze style note type designed by <a href="https://www.ankingmed.com">The AnKing</a> for use in all Physeo-made decks. 

**Open the Note Types Folder to see html/css design.**
**Download the latest version of the Note Type from the <a href="https://github.com/AnKingMed/Physeo-Note-Type/releases">Releases</a> tab**

## How to Use & Customize This Note Type
- <a href="https://www.youtube.com/watch?v=HgKDRTTTnh4&t=37s">This video</a> goes over how to customize card styling (including basic html/css)
- <a href="https://www.youtube.com/watch?v=4Q6Ll5k412U&t=1s">This video</a> goes into specifics of the AnKingMaster-v2+ updates to the card styling which are somewhat similar to this card

### Features
- <b>Invisible countdown timer</b> on the front
  <details><summary>Set timer length <i>(Front template)</i></summary>
    <p>

    ```
    //############## TIMER CONFIGURATION START ##############
    //Set Timer Length
    var minutes = 0
    var seconds = 9
    //############## TIMER CONFIGURATION END ##############
    ```
    </p>
  </details>
  <details><summary>Turn timer off <i>(Styling)</i></summary>
    <p>

    ```
    /* TIMER ON/OFF */
    .timer {
      display: block; /* ‘none’ or ‘block’ */
    }
    ```
    </p>
  </details>

- <b>Clickable tags</b> (must have <a href="">Clickable Tags</a> add-on installed for them to be clickable, but they will still display without the add-on)
  <details><summary>Turn on/off by default and adjust for compatibility with No Distractions add-on <i>(Styling)</i></summary>
    <p>

    ```
    /* TAGS ON/OFF DESKTOP & MOBILE*/
    #tags-container {
      display: block; /* ‘none’ or ‘block’ */
    }

    .mobile #tags-container {
      display: none; /* ‘none’ or ‘block’ */
    }

    /* MOVE TAGS UP FOR 'NO-DISTRACTIONS' ADD-ON */
    #tags-container {
      padding-bottom: 0px; /* 0 normal, 55 to move up */
    }
    ```
    </p>
  </details>
  <details><summary>Toggle on/off with shortcut <i>(Back template)</i></summary>
    <p>

    Default is `c`
    ```
    // ##############  TAG SHORTCUT  ##############
    // Visit https://keycode.info/ to get the number/letter for the key you want to assign. 
    var ToggleTags = "67"; // c
    ```
    </p>
  </details>

- <b>Editable fields</b> - (For use with the <a href="">Edit Field During Review (Cloze)</a> add-on)
  <details><summary>To enable editable fields <i>(Back template)</i></summary>
    <p>

    1. Make sure that the correct add-on is installed (NOT `Edit Field During Review`)
    2. The config of `Edit Field During Review (Cloze)` allows for click to edit or ctrl+click to edit
    3. In order to make a field editable, change `{{Personal Notes}}` to `{{edit:Personal Notes}}`. 
    <u>For cloze fields:</u>
    Change `<div class="editcloze">{{cloze:Text}}</div>` to `<div class="editcloze">{{edit:cloze:Text}}</div>`
    Do NOT change `<div class="clozefield">{{cloze:Text}}</div>` (This is set for mobile to avoid errors)

    </p>
  </details>
- <b>Wikipedia searches in reviewer</b>
  - Highlight text and then use the shortcut `w` (if nothing shows up, it's because your search returned no results in wikipedia)
- <b>Field shortcuts and/or hint hotkeys add-on</b> (need Refocous Cards when Reviewing add-on unless on Anki 2.1.36+)
  - The Hint Hotkeys add-on will open buttons with `h`
  <details><summary>Individual shortcuts can be customized <i>(Back template)</i></summary>
    <p>

    ```
    // ##############  BUTTON REVEAL SHORTCUTS  ##############
    // Visit https://keycode.info/ to get the number/letter for the key you want to assign. 
    // The shortcuts are  Alt  +  the number/letter below
    // All shortcuts will also open with "H" if using the Hint Hotkeys add-on 
    var ButtonShortcuts = {
        "Personal Notes" : '49', // alt + 1
        "Missed Questions" : '50', // alt + 2
    }

    var ToggleAllButtons = '222' // '
    ```
    </p>
  </details>
- <b>Auto scroll to button that is opened</b> (can be toggled off)
  <details><summary>Turn on/off by default and adjust for compatibility with No Distractions add-on <i>(in styling)</i></summary>
    <p>

    Change `true` to `false` to turn off the auto scroll
    ```
    var ScrollToButton = true;
    ```
    </p>
  </details>
- <b>Auto open hints</b>:
  <details><summary>Version 11 <i>(Back template)</i></summary>
    <p>

    ```
    // ##############  SHOW BUTTON HINTS AUTOMATICALLY  ##############
    var ButtonAutoReveal = {
        "Personal Notes": false,
        "Missed Questions": false,
    }
    ```
    </p>
  </details>
- <b>TTS</b> - watch <a href="https://www.youtube.com/watch?v=5QFDrY7PDUk&t=4s">this video</a> for more details
  <details><summary>How to enable <i>(Front and back template)</i></summary>
    <p>

    ## Front template:
    ```
    <!-- ##############  Text-to-speech  ##############
    replace the arrows/dashes from the statement below with double brackets-->

    <!--tts en_US voices=Apple_Samantha speed=1.4:cloze:Text-->
    ```
    <u>change to look like:</u>
    ```
    <!-- ##############  Text-to-speech  ##############
    replace the arrows/dashes from the statement below with double brackets-->

    {{tts en_US voices=Apple_Samantha speed=1.4:cloze:Text}}
    ```
    ## Back template:
    ```
    <!-- ##############  TEXT-TO-SPEECH ##############
    replace the arrows/dashes from the statement below with double brackets-->

    <!--tts en_US voices=Apple_Samantha speed=1.4:cloze-only:Text-->
    ```
    <u>change to look like:</u>
    ```
    <!-- ##############  TEXT-TO-SPEECH ##############
    replace the arrows/dashes from the statement below with double brackets-->

    {{tts en_US voices=Apple_Samantha speed=1.4:cloze-only:Text}}
    ```
    </p>
  </details>
- <b>Images will zoom with click (or hover)</b>
  <details><summary>Change the transform scale or method <i>(Back Template)</i></summary>
    <p>

    `active` will cause images to zoom on click. `hover` will cause images to zoom on hover. We recommend leaving the .mobile portion untouched as images are default 100% on mobile and the zoom does not work well with touchscreens. 
    ```
    /*Image hover zoom*/
    #extra img:active,
    #notes img:active,
    #missed img:active,
    #imagefield img:active {
      transform: scale(1.5);
    }

    .mobile img:active {
      transform: scale(1.0) !important;
    }
    ```
    </p>
  </details>
- <b>Highlight all tags with a red background when there is a tag containing the text "xxxyyyzzz"</b>
  <details><summary>Change tagID <i>(Front and Back Template)</i></summary>
    <p>

    ```
    //ENTER THE TAG TERM WHICH, WHEN PRESENT, WILL TRIGGER A RED BACKGROUND
    var tagID = "XXXYYYZZZ"
    ```
    </p>
  </details>

## PHYSEO COLORS
light green = `#56868a`
slightly lighter green = `#588f96`
dark navy = `#1b2855`
not official logo even lighter green (for nightmode) = `#78c0ca`

## TODO general
- [X] Add feature list to README
- [ ] Update TTS settings
- [ ] Setup so that you can do left-jusified mnemonics
- [X] Change tag colors?
- [ ] Img width
- [ ] Style the day mode

***

<p align="center">
<b>Note type designed by:</b>
<br>
<a href="https://www.ankingmed.com" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/AnKingSmall.png?raw=true"></a><a href="https://www.ankingmed.com" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/TheAnKing.png?raw=true"></a>
  <br>
  <a href="https://www.facebook.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/FB.png?raw=true"></a>     <a href="https://www.instagram.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Instagram.png?raw=true"></a>     <a href="https://www.youtube.com/theanking" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/YT.png?raw=true"></a>     <a href="https://www.tiktok.com/@ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/TikTok.png?raw=true"></a>     <a href="https://www.twitter.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Twitter.png?raw=true"></a>
  <br>
<a href="https://www.ankipalace.com/membership" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/Patreon.jpg?raw=true"></a>
