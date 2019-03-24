customElements.whenDefined('card-tools').then(() => {
let cardTools = customElements.get('card-tools');
window.LovelaceBrowserCommander = window.LovelaceBrowserCommander || (function() {

  const event_name = "browser_command";

  cardTools.hass.connection.subscribeEvents((event) => {
    if(!cardTools.lovelace) return;
    if(event.event_type != event_name) return;
    const data = event.data;
    if(data.id) {
      if(Array.isArray(data.id)) {
        if(!data.id.includes(cardTools.deviceID)) return;
      } else{
        if(data.id != cardTools.deviceID) return;
      }
    }
    if(!data.command) return;

    switch(data.command) {
      case "debug":
        let message = document.createElement('ha-card');
        message.innerHTML = `${cardTools.deviceID}`;
        message.style.padding = '10px';
        cardTools.popUp('Device id', message);
        break;
      case "popup":
        if(!data.title) return;
        if(!data.card) return;
        var card = cardTools.createCard(data.card);
        card.hass = cardTools.hass;
        var moreInfo = cardTools.popUp(data.title, card, data.large || false);
        // Style popup
        if(data.style) {
          let oldStyle = {};
          for(var k in data.style) {
            oldStyle[k] = moreInfo.style[k];
            moreInfo.style.setProperty(k, data.style[k]);
          }
          setTimeout(() => {
            let interval = setInterval(() => {
              if(moreInfo.getAttribute('aria-hidden')) {
                for(var k in oldStyle)
                  moreInfo.style.setProperty(k, oldStyle[k]);
                clearInterval(interval);
              }
            }, 100);
          }, 1000);
        }
        break;
      case "navigate":
        if(!data.navigation_path) return;
        history.pushState(null, "", data.navigation_path);
        cardTools.fireEvent("location-changed");
        break;
      case "more-info":
        if(!data.entity_id) return;
        cardTools.moreInfo(data.entity_id);
        document.querySelector("home-assistant")._moreInfoEl.large = false;
        if(data.large)
          document.querySelector("home-assistant")._moreInfoEl.large = true;
        break;
      case "lovelace-reload":
        cardTools.fireEvent("config-refresh");
        break;
      case "close-popup":
        cardTools.closePopUp()
        break;
      case "set-theme":
        if(!data.theme) return;
        cardTools.fireEvent("settheme", data.theme);
        break;

    };
  });

  return true;

}());
});

window.setTimeout(() => {
  if(window.LovelaceBrowserCommander) return;
  console.error(`%cCARD-TOOLS NOT FOUND
  %cSee https://github.com/thomasloven/lovelace-card-tools`,
  "color: red; font-weight: bold",
  "");
}, 2000);
