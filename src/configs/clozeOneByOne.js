<%#

# Parameters
- clozeHider: string
_%>
<%_
  var clozeHider = clozeHider === undefined ? "👑" : clozeHider
_%>

// ##############  CLOZE ONE BY ONE  ##############
var revealNextShortcut = "N" 
var revealNextWordShortcut = "Shift + N"
var toggleAllShortcut = ","

// Changes how "Reveal Next" and clicking behaves. Either "cloze" or "word".
// "word" reveals word by word. 
var revealNextClozeMode = "cloze" 

// What cloze is hidden with
var clozeHider = (elem) => "<%- clozeHider %>"
/* 
You can replace the above line with below examples. '█' or '_' works well for hiding clozes.

// Fixed length:
var clozeHider = (elem) => "███"
// Replace each character with "█":
var clozeHider = (elem) => "█".repeat(elem.textContent.length)
// Show whitespaces:
var clozeHider = (elem) => "[" + elem.textContent.split(" ").map((t) => "█".repeat(t.length)).join(" ") + "]"
// Color-filled box (doesn't hide images):
var clozeHider = (elem) => `<span style="background-color: red; color: transparent;">${elem.innerHTML}</span>`
*/