
document.getElementById('check').innerHTML=`<div></div>
<div></div>
<div></div>
<div></div>
<div><img id="check_img" src='static/loader/logo2.ico'></div>
<div></div>
<div></div>
<div></div>
<div></div>`;
function a(){

document.getElementById("check").style="display:grid;";

}
var intervalID=setInterval(a,1000);

window.onload=setTimeout(function() {clearInterval(intervalID);
  document.getElementById("check_img").style="display:none;";
   document.getElementById("check").style="display:none;";},2000);

