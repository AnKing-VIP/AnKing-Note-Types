# AnKing Note Types
For simplicity and ease-of-use, I have uploaded all of my note types here. This will allow for better tracking of changes and better tutorials.

## How to Use These Note Types
**To download a note type,** find the latest version in the [Releases](https://github.com/AnKingMed/AnKing-Note-Types/releases) tab

**To learn how to use and customize a note type,** watch [this video](https://youtu.be/NYUhNMyAZNs).  For written instructions, open the [Note Types Folder](https://github.com/AnKingMed/AnKing-Note-Types/tree/master/Note%20Types). Each Folder has it's own README file that explains the note and it's features

**To install the AnKing Note Types add-on,** (allows for very easy and user-friendly customization) visit this page: https://ankiweb.net/shared/info/952691989

## How to Update These Note Types
There are two methods to update if you already have any of these notes in your collection

##### Method 1 (Preferred)
1. Download the [AnKing Note Types (Easy Customization)](https://ankiweb.net/shared/info/952691989) add-on from AnkiWeb. Be sure to restart Anki after installing.
2. Go to the AnKing->AnKing Note Types menu and then select `Update Note Types` in the dialog

##### Method 2 
1. Download the latest file from the [Releases](https://github.com/AnKingMed/AnKing-Note-Types/releases) tab
2. Install the [Special Fields add-on](https://ankiweb.net/shared/info/1102281552) (restart Anki after installing)
3. Go to Tools->Special Fields
4. Click the `Update Settings` button and then `Save`
5. Import the downloaded file. This should update the note styling
_After importing, we recommended that you go back to Tools->Special Fields and click the `Import Tags Settings` button to prevent any future updates from altering note styling_

##### Method 3
NOTE: This method is less preferred because updates may be in progress and incomplete.
1. Locate the appropriate file in the [Note Types Folder](https://github.com/AnKingMed/AnKing-Note-Types/tree/master/Note%20Types)
2. Copy the text from the file into the Front Template, Back Template and Styling of the note type
   - You can click the `Copy Raw Content` (box on top of a box) button in the top right to easily copy everything _(it's just left of the pencil icon)_ 

## Thank You
Huge thank you to @BlueGreenMagick, @Kleinerpirat, @RisingOrange, u/Ankiphil, and u/holythesea who have helped significantly with the development of these notes over the last few years. Also thank you to u/passwordisnotaco who posted the [initial version](https://www.reddit.com/r/Anki/comments/pia8e5/how_to_incrementally_reveal_an_image_occlusion/?utm_source=share&utm_medium=ios_app&utm_name=iossmf) of the IO-one by one note type.

## How to Use & Customize These Note Types
- <a href="https://www.youtube.com/watch?v=HgKDRTTTnh4&t=37s">This video</a> goes over how to customize card styling (including basic html/css)
- <a href="https://www.youtube.com/watch?v=4Q6Ll5k412U&t=1s">This video</a> goes into specifics of the AnKingMaster-v2+ updates to the card styling

### Features Used In These Note Types
All note types in this repo use many or all of the features listed below. Some will appear slightly different as they have been customized to work with each individual style. Features unique to a note type are listed in the README file of that note type within the Note Types Folder
- <b>Invisible countdown timer</b> on the front
  <details><summary>Set timer length <i>(Front template)</i></summary>
    <p>

    ```
    // Timer config (timer length, timer finished message)
    var minutes = 0
    var seconds = 9
    var timeOverMsg = "<span style='color:#CC5B5B'>!<br/>!<br/>!<br/>!<br/>!<br/>!</span>"
    ```
    </p>
  </details>
  <details><summary>Turn timer on/off <i>(Styling)</i></summary>
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

    Default is `C`
    ```
    // ##############  TAG SHORTCUT  ##############
    var toggleTagsShortcut = "C";
    ```
    </p>
  </details>

- <b>Editable fields</b> - (For use with the <a href="">Edit Field During Review (Cloze)</a> add-on)
  <details><summary>To enable/disable editable fields <i>(Back template)</i></summary>
    <p>

    1. Make sure that the correct add-on is installed (NOT `Edit Field During Review`)
    2. The config of `Edit Field During Review (Cloze)` allows for click to edit or ctrl+click to edit
    3. In order to make a field editable, change `{{Field Name}}` to `{{edit:Field Name}}`. 
    <u>For cloze fields:</u>
    Change `<div class="editcloze id="text"">{{cloze:Text}}</div>` to `<div class="editcloze" id="text">{{edit:cloze:Text}}</div>`
    Do NOT change `<div class="clozefield">{{cloze:Text}}</div>` (This is set for mobile to avoid errors)

    </p>
  </details>

- <b>Wikipedia searches in reviewer</b>
  - Highlight text and then use the shortcut `w` (if nothing shows up, it's because your search returned no results in wikipedia)

- <b>Button shortcuts and/or hint hotkeys add-on</b> (need Refocous Cards when Reviewing add-on unless on Anki 2.1.36+)
  - The Hint Hotkeys add-on is no longer necessary
  <details><summary>Individual shortcuts can be customized <i>(Back template)</i></summary>
    <p>

    ```
    // ##############  HINT REVEAL SHORTCUTS  ##############
    // All shortcuts will also open with "H" if using the Hint Hotkeys add-on 
    var ButtonShortcuts = {
        "Lecture Notes" : "Alt + 1",
        "Missed Questions" : "Alt + 2",
    }
    var ToggleAllButtons = "'"
    var ToggleNextButtonShortcut = "H";
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
    <details><summary>Old Version <i>(Back template)</i></summary>
    <p>

    <img src="/screenshots/Auto-open-hint.jpg" style="width:600px">
    </p>
  </details>
  <details><summary>Current Version <i>(Back template)</i></summary>
    <p>

    ```
    // ##############  SHOW HINTS AUTOMATICALLY  ##############
    var ButtonAutoReveal = {
        "Lecture Notes" : false,
        "Missed Questions" : false,
    }
    ```
    </p>
  </details>
    <details><summary>Auto open only on certain notes</summary>
    <p>

    Add the tag `autoopen::Field_Name` to a note and that Field will open automatically just on that note (use `_` in place of spaces and ensure the same spelling)
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

    `active` will cause images to zoom on click. `hover` will cause images to zoom on hover. Some Note Types have specific zoom scales for specific fields
    ```
    /*Image hover zoom*/ 
    img:active {
      transform: scale(1.2);
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
  
- <b>Dynamic Table Formatting</b>
  <details><summary>How automatic default formatting works <i>(Styling)</i></summary>
    <p>

  When inserting HTML tables into note types, the following features are included: 
  1. Alternating rows will automatically format to a white/light grey color scheme for readability
  2. Any row that spans an entire column through merged cells will automatically be formatted as a primary header
  3. Any cell that is formatted with a <th> tag will automatically be formatted as a secondary header
  4. All styles can be overridden by specifying inline styles through addons such as T5
    
    </p>
  </details>

## TODO
- [ ] 

## Contributing

All files in `/Note Types` are generated from files in `/src`. DO NOT edit the files in `/Note Types`!
We use [ejs](https://ejs.co/) to reduce duplicate code across various note types.

To generate the files, [Node.js](https://nodejs.org/en/download/) needs to be installed, and `npm` added to PATH.

After editing the files in `/src`, run `npm run build` to generate the files. Always run `npm run build` before opening a Pull Request.

If you get a `Permission denied` message, you may need to run `sudo chmod 755 ./build` to make the `/build` file executable.

The json files for the note types (for example https://github.com/AnKingMed/AnKing-Note-Types/blob/master/Note%20Types/AnKing/AnKing.json) are how Anki stores models / note types internally. The scheme is described in the AnkiDroid wiki https://github.com/ankidroid/Anki-Android/wiki/Database-Structure#models-jsonobjects. The [AnKing Notes Add-on](https://github.com/AnKingMed/anking_notes_addon) combines such a json file with a front template, a back template and the styling information and loads the resulting note type into Anki.

***

### If you like these, please consider donating to this project

<p align="center">
<a href="https://www.ankingmed.com" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/AnKingSmall.png?raw=true"></a><a href="https://www.ankingmed.com" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/TheAnKing.png?raw=true"></a>
  <br>
  <a href="https://www.facebook.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/FB.png?raw=true"></a>     <a href="https://www.instagram.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Instagram.png?raw=true"></a>     <a href="https://www.youtube.com/theanking" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/YT.png?raw=true"></a>     <a href="https://www.tiktok.com/@ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/TikTok.png?raw=true"></a>     <a href="https://www.twitter.com/ankingmed" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/Social/Twitter.png?raw=true"></a>
  <br>
<a href="https://www.theanking.com/anking-memberships" rel="nofollow"><img src="https://raw.githubusercontent.com/AnKingMed/My-images/master/AnKing/Patreon.jpg?raw=true"></a>
<br>
<b>Check out our <a href="https://www.theanking.com/anki-mastery-course/?utm_source=anking_notetypes&amp;utm_medium=anki_add-on_page&amp;utm_campaign=mastery_course" rel="nofollow">Anki Mastery Course</a>! (The source of funding for this project)</b><br></p>
