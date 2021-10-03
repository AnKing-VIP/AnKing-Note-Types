## How to Use & Customize This Note Type
- <a href="https://www.youtube.com/watch?v=HgKDRTTTnh4&t=37s">This video</a> goes over how to customize the card styling (including basic html/css)
- <a href="https://www.youtube.com/watch?v=4Q6Ll5k412U&t=1s">This video</a> goes into specifics of the AnKingMaster-v2+ updates to the card styling

## Features
- <b>Invisible countdown timer</b> on the front
  <details><summary>Set timer length <i>(on front template)</i></summary>
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
  <details><summary>Turn timer off <i>(in styling)</i></summary>
    <p>

    ```
    /* TIMER ON/OFF */
    .timer { display: block; } /* 'none' or 'block' */
    ```
    </p>
  </details>
- <b>Clickable tags</b> (must have <a href="">Clickable Tags</a> add-on installed for them to be clickable, but they will still display without the add-on)
  <details><summary>Turn on/off by default and adjust for compatibility with No Distractions add-on <i>(in styling)</i></summary>
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
  
    - toggle on/off with the shortcut `c`

- <b>Editable fields</b> - (For use with the <a href="">Edit Field During Review (Cloze)</a> add-on)
- <b>Wikipedia searches in reviewer</b>
  - Highlight text and then use the shortcut `w` (if nothing shows up, it's because your search returned no results in wikipedia)
- <b>Field shortcuts and/or hint hotkeys add-on</b> (need Refocous Cards when Reviewing add-on unless on Anki 2.1.36+)
- <b>Auto scroll to hint that is opened</b> (can be toggled off)
- <b>Auto open hints</b>:
  -  <img src="/screenshots/Auto-open-hint.jpg" style="width:600px">
- <b>TTS</b>
- <b>Med Shamim styling available</b>
- <b>Images will zoom with click (used to be hover)</b>
- <b>Highlight any tags containing the word "xxxyyyzzz"</b>

## Changelog:
AnKingMaster-v1 notetype was introduced to provide the same note for all cards in the AnKing Overhaul Deck for Step 1 and Step 2. It combined fields from the AnKingMed and AnKingSketchy Note Types
AnKingMaster-v2 note type added the Physeo and Pixorize fields
AnKingMaster-v3 note type added the OME field

2021-09-03: Initial Release on Github

## TODO
- [ ] upload changes made over time
- [X] upload 2 card type video links
- [X] instructions on features including wikipedia, c to reveal tags, alt+# to reveal things, H for hint hotkeys, how to reveal hints automatically, etc
- [ ] Update buttons script and html to new version
- [ ] Remove css styling from buttons (i.e. `style="background:#ababab; color:black!important; font-weight:bold; width:50%!important;"`) and put in the .button-revealed css (from AnKingMasterv3 note type)
- [ ] Update Tags script and update var at top for hotkey switching on and off


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
