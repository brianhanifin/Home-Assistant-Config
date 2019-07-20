function GetNotifyCount() {
  const hass = document.querySelector("home-assistant").hass;
  let notifications = 0;

  for (state in hass.states) {
    if (state.startsWith("persistent_notification.")) notifications += 1;
  }
  return notifications;
}

function UpdateFavicon() {
  let count = GetNotifyCount();
  const favurl = "/static/icons/favicon.ico";

  // Modified from https://medium.com/@alperen.talaslioglu/building-dynamic-favicon-with-javascript-223ad7999661
  const favicon = parent.document.querySelector("link[rel=icon]");
  const faviconSize = 16;
  const canvas = document.createElement("canvas");
  canvas.width = faviconSize;
  canvas.height = faviconSize;
  const context = canvas.getContext("2d");
  const img = document.createElement("img");
  img.src = favicon.href;

  img.onload = () => {
    // Draw Original Favicon as Background
    context.drawImage(img, 0, 0, faviconSize, faviconSize);
    if (count > 0) {
      // Draw Notification Circle
      context.beginPath();
      context.arc(
        canvas.width - faviconSize / 3,
        faviconSize / 3,
        faviconSize / 3,
        0,
        2 * Math.PI
      );
      context.fillStyle = "#FF0000";
      context.fill();

      // Draw Notification Number
      context.font = '10px "helvetica", sans-serif';
      context.textAlign = "center";
      context.textBaseline = "middle";
      context.fillStyle = "#FFFFFF";
      context.fillText(count, canvas.width - faviconSize / 3, faviconSize / 3);
      // Replace favicon
      favicon.href = canvas.toDataURL("image/png");
    } else {
      favicon.href = favurl;
    }
  };
}

let prevCount;
window.setInterval(function() {
  if (prevCount !== GetNotifyCount()) {
    UpdateFavicon();
    prevCount = GetNotifyCount()
  }
}, 1000);
