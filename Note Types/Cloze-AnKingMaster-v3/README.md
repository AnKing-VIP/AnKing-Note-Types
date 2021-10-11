## How to Use & Customize This Note Type
- <a href="https://www.youtube.com/watch?v=HgKDRTTTnh4&t=37s">This video</a> goes over how to customize the card styling (including basic html/css)
- <a href="https://www.youtube.com/watch?v=4Q6Ll5k412U&t=1s">This video</a> goes into specifics of the AnKingMaster-v2+ updates to the card styling

## Features
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
    .timer { display: block; } /* 'none' or 'block' */
    ```
    </p>
  </details>

- <b>Clickable tags</b> (must have <a href="">Clickable Tags</a> add-on installed for them to be clickable, but they will still display without the add-on)
  <details><summary>Turn on/off by default and adjust for compatibility with No Distractions add-on <i>(Styling)</i></summary>
    <p>

    ```
    /* TAGS ON/OFF DESKTOP & MOBILE*/
       #tags-container { display: none; }  /* ‘none’ or ‘block’ */
    .mobile #tags-container { display: none; } /* ‘none’ or ‘block’ */
    /* MOVE TAGS UP FOR 'NO-DISTRACTIONS' ADD-ON */
    #tags-container{ padding-bottom: 0px; } /* 0 normal, 55 to move up */
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

    var lecturenotes = '49'; // alt + 1
    var missedQ = '50'; // alt + 2
    var pathoma = '51'; // alt + 3
    var bnb = '52'; // alt + 4
    var firstaid = '53'; // alt + 5
    var sketchy = '54'; // alt + 6
    var pixorize = '55'; // alt + 7
    var physeo = '56'; // alt + 8
	  var ome= '112'; // alt + f1
    var additional = '57'; // alt + 9
    var OpenCloseAll = '222'; // '
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
    <details><summary>Version 10 <i>(Back template)</i></summary>
    <p>

    <img src="/screenshots/Auto-open-hint.jpg" style="width:600px">
    </p>
  </details>
  <details><summary>Version 11 <i>(Back template)</i></summary>
    <p>

    ```
    // change values from false to true to have the fields revealed from the start
    var ShowLectureNotes = false;
    var ShowMissedQuestions = false;
    var ShowPathoma = false;
    var ShowBoards = false;
    var ShowFirstAid = false;
    var ShowSketchy = false;
    var ShowPixorize = false;
    var ShowPhyseo = false;
    var ShowFirstAid = false;
    var ShowOME = false;
    var ShowAdditional = false;
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
- <b>Med Shamim styling available</b> <a href="/Note Types/Cloze-AnKingMaster-v3/Shamim Customize styling.css">here</a>
  <details><summary>Replace the customizable portion with the contents of the link above <i>(in styling)</i></summary>
    <p>

    <u>The customizable portion begins and ends as shown below:</u>
    ```
    /*~~~~~~~~USER CUSTOMIZATION START~~~~~~~~~*/
    ...
    contents
    ...
    /* ~~~~~~~~END CUSTOMIZATION~~~~~~~~ */
    ```
    </p>
  </details>
- <b>Images will zoom with click (or hover)</b>
  <details><summary>Change the transform scale or method <i>(Back Template)</i></summary>
    <p>

    `active` will cause images to zoom on click. `hover` will cause images to zoom on hover. We recommend leaving the .mobile portion untouched as images are default 100% on mobile and the zoom does not work well with touchscreens. 
    ```
    /*Image hover zoom*/
    #extra img:active, #lecture img:active, #missed img:active, #pathoma img:active, #bnb img:active { transform:scale(1.2); }
    #firstaid img:active, #sketchy img:active, #pixorize img:active, #physeo img:active, #additional img:active { transform:scale(1.5); }
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

## Changelog:
<b>AnKingMaster-v1</b> notetype was introduced to provide the same note for all cards in the AnKing Overhaul Deck for Step 1 and Step 2. It combined fields from the AnKingMed and AnKingSketchy Note Types
<b>AnKingMaster-v2</b> note type added the Physeo and Pixorize fields
<b>AnKingMaster-v3</b> note type added the OME field
Detailed changelog over time has been noted <a href="https://www.ankipalace.com/deck-updates-log">here</a>

2021-09-03: Initial Release on Github

## TODO
- [x] upload changes made over time
- [X] upload 2 card type video links
- [X] instructions on features including wikipedia, c to reveal tags, alt+# to reveal things, H for hint hotkeys, how to reveal hints automatically, etc
- [X] Update buttons script and html to new version
- [X] Remove css styling from buttons (i.e. `style="background:#ababab; color:black!important; font-weight:bold; width:50%!important;"`) and put in the .button-revealed css (from AnKingMasterv3 note type)
- [X] Update Tags script and update var at top for hotkey switching on and off
- [X] Change to "curly brackets" on all note types
- [X] explain var tagID on all note types
- [X] Fix change from lecture-notes id to lecture
- [x] Maybe fix Image hover zoom - needs to be 1.0 on mobile (maybe just a simple important class?)
- [x] Fix custom images for buttons


<b>Please consider checking out our:</b>
<br>
<a href="https://www.youtube.com/theanking/playlists" rel="nofollow">YouTube Channel</a>- <i>How to use Anki for beginners and advanced users.</i> 
<br>
<a href="https://www.instagram.com/ankingmed" rel="nofollow">Instagram</a>/<a href="https://www.facebook.com/ankingmed" rel="nofollow">Facebook</a>: <i>@Ankingmed</i>
<br>
<a href="https://www.ankingmed.com" rel="nofollow">www.AnKingMed.com</a>- <i>Recommended add-ons, tutorials and more including <b>how to download 40+ add-ons in &lt; 5min</b></i>
<br>
<a href="https://www.ankipalace.com/membership" rel="nofollow">Patreon</a>- <i>Support our work and <b>get individualized Anki help!</b></i><br>

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
