## Instructions:
1. Download Closet For Anki addon (272311064), close out of anki, restart anki
2. Download card template here: <a href="https://github.com/AnKingMed/AnKing-Note-Types/blob/master/Apkg/IO-one_by_one.apkg">IO-one by one</a>
3. When creating the new I/O card, make sure you are using the note template called `IO-one by one`. Paste your image into the 'image' field.
4. Click the icon in the toolbar that looks like a blue/red box in a box. The image should outline with a red dotted border when you click that button.
5. Draw your occlusions in the order you want them revealed. You want each occlusion to say 'rect1' inside of it. **If you need to delete a rectangle**, hold shift while clicking on that box.
6. Once you have all of your occlusions made, right click on the image (don't right click over an occlusion though) and select 'accept occlusions'
- You will see the 'I0' field auto populate. At that point you are good to add the card by clicking "Add" at the bottom
7. When reviewing, you will see all boxes occluded at once, however the first box will be highlighted. Click or use `n` to reveal a box, and the subsequent box will become highlighted. Use `,` to reveal all at once. Continue until all boxes are revealed. You can use `h` (requires the "Hint Hotkeys" add-on instealled) or click to reveal the buttons. Use `'` to reveal all buttons at once. _(These shortcuts can all be customized)_
8. **To edit occlusions in an existing card**, click the icon in the toolbar that looks like a blue/red box in a box.

This note type **will** work on Anki iOS and AnkiDroid.

## Screen recordings
### Card creation
<img src="/screenshots/Creating IO one by one.gif" style="width:600px;">

### Function
<img src="/screenshots/IO one by one new.gif" style="width:600px;">

## How to Customize This Note Type
- <a href="https://www.youtube.com/watch?v=HgKDRTTTnh4&t=37s">This video</a> goes over how to customize card styling (including basic html/css)
- <a href="https://www.youtube.com/watch?v=4Q6Ll5k412U&t=1s">This video</a> goes into specifics of the AnKingMaster-v2+ updates to the card styling which is somewhat similar to this card

## Changelog:
2021-09-05: Initial Release on <a href="https://www.reddit.com/r/Anki/comments/pia8e5/how_to_incrementally_reveal_an_image_occlusion/?utm_source=share&utm_medium=ios_app&utm_name=iossmf">reddit</a>

## Thank you:
Huge thank you to Phil (u/Ankiphil), RisingOrange & all others who have contributed to this note type

## TODO
- [X] Make it so the incremental review is on the backside of the note type, not the front (I found that I accidentally flipped it with the space bar multiple times)
- [X] Make it so there’s a hotkey that can open them incrementally (i.e. hitting the letter ‘n’)
- [X] Making it customizable a tad like my anking note types have been :tada: (Nick cleanup code)
- [X] Make it so any can be clicked, but the red box is an incremental process
- [X] Fix on mobile (add a button that reveals them so you don't have to type? Remove the ability to tap them?)
- [X] Fix reveal code shortcuts to keycodes so there are more options (current method for incremental and reveal all only works on every other card)
- [X] Fix reveal code for the clickable tags reveal (similar problem as above)
- [X] Add feature to put the occlusions back after revealing all of them.  Need to update for mobile. Add back reset button?
- [X] scroll to hint not working (scrolls when closing button instead of opening)
- [X] Simple way to auto-reveal buttons instead of complicated method. (Make a variable and set to true/false and if true auto trigger opening the field or something like that?)
     ```
    var showLecture = true;
    if (showLecture == true){
      toggleHint('button-ln', 'hint-ln');
    }
    ```
- [X] Remove css styling from buttons (i.e. `style="background:#ababab; color:black!important; font-weight:bold; width:50%!important;"`) and put in the .button-revealed css (from AnKingMasterv3 note type)
- [x] Fix button revealed style
- [ ] Update note type on Github and make release. (Add bottom field about our team)
- [ ] Update readme


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
